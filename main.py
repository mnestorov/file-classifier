import os
import shutil
import time
import re
import logging
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config import (download_folder, classification_rules, GREEN, RESET, log_filename, DAYS_BEFORE_ARCHIVE, ARCHIVE_ACTION, ARCHIVE_FOLDER)
from datetime import timedelta

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to determine the folder to move the file to based on its extension
def classify_file(file, rules):
    file_extension = os.path.splitext(file)[1]
    
    for folder, extensions in rules.items():
        if file_extension in extensions:
            return folder
    
    return None

# Function to check if a file is a duplicate based on its name pattern
def is_duplicate(file):
    file_name, file_extension = os.path.splitext(file)
    duplicate_pattern = re.compile(r'^(.+)\s\(\d+\)$')
    match = duplicate_pattern.match(file_name)
    
    if match:
        original_file_name = match.group(1) + file_extension
        return original_file_name
    else:
        return None
    
def get_date_folder(file_path):
    last_modified = os.path.getmtime(file_path)
    date = datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d')
    return date    

# Function to classify and move existing files in the download folder
def classify_existing_files():
    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)
        
        if os.path.isfile(file_path):
            target_folder = classify_file(file, classification_rules)
            
            if target_folder:
                date_folder = get_date_folder(file_path)
                target_path = os.path.join(download_folder, target_folder, date_folder, file)
                
                if not os.path.exists(os.path.dirname(target_path)):
                    os.makedirs(os.path.dirname(target_path))
                
                shutil.move(file_path, target_path)
                print(f'{GREEN}Moved {file} to {target_folder}/{date_folder}{RESET}')
                logging.info(f'Moved {file} to {target_folder}/{date_folder}')
                
                # Check if the file is a duplicate and delete it if the original exists
                original_file = is_duplicate(file)
                if original_file:
                    original_file_path = os.path.join(download_folder, target_folder, date_folder, original_file)
                    if os.path.exists(original_file_path):
                        os.remove(target_path)
                        print(f'{GREEN}Deleted duplicate file {file}{RESET}')
                        logging.info(f'Deleted duplicate file {file}')

# Check folders for old files and either move them 
# to an archive folder or delete them based on user preferences
def folder_cleanup():
    current_time = datetime.now()

    for folder, extensions in classification_rules.items():
        folder_path = os.path.join(download_folder, folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getmtime(file_path) < (current_time - timedelta(days=DAYS_BEFORE_ARCHIVE)).timestamp():
                    if ARCHIVE_ACTION == "move":
                        archive_path = os.path.join(download_folder, ARCHIVE_FOLDER)
                        if not os.path.exists(archive_path):
                            os.makedirs(archive_path)

                        shutil.move(file_path, os.path.join(archive_path, file))
                        print(f'{GREEN}Moved old file {file} to {ARCHIVE_FOLDER}{RESET}')
                        logging.info(f'Moved old file {file} to {ARCHIVE_FOLDER}')

                    elif ARCHIVE_ACTION == "delete":
                        os.remove(file_path)
                        print(f'{GREEN}Deleted old file {file}{RESET}')
                        logging.info(f'Deleted old file {file}')


# Custom event handler to handle file creation events
class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        file = event.src_path
        if os.path.isfile(file):
            target_folder = classify_file(file, classification_rules)
            
            if target_folder:
                date_folder = get_date_folder(file)
                target_path = os.path.join(download_folder, target_folder, date_folder, os.path.basename(file))
                
                if not os.path.exists(os.path.dirname(target_path)):
                    os.makedirs(os.path.dirname(target_path))
                
                shutil.move(file, target_path)
                print(f'{GREEN}Moved {file} to {target_folder}/{date_folder}{RESET}')
                logging.info(f'Moved {file} to {target_folder}/{date_folder}')
                
                # Check if the file is a duplicate and delete it if the original exists
                original_file = is_duplicate(os.path.basename(file))
                if original_file:
                    original_file_path = os.path.join(download_folder, target_folder, date_folder, original_file)
                    if os.path.exists(original_file_path):
                        os.remove(target_path)
                        print(f'{GREEN}Deleted duplicate file {os.path.basename(file)}{RESET}')
                        logging.info(f'Deleted duplicate file {os.path.basename(file)}')

def main():
    # Create the necessary folders if they don't exist
    for folder in classification_rules.keys():
        folder_path = os.path.join(download_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
    # Also ensure the ARCHIVE_FOLDER exists if the action is set to "move"
    if ARCHIVE_ACTION == "move":
        archive_path = os.path.join(download_folder, ARCHIVE_FOLDER)
        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

    # Classify existing files in the directory
    classify_existing_files()

    # Create and start the observer to monitor the download folder
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=download_folder, recursive=False)
    observer.start()

    last_cleanup_time = time.time()

    try:
        while True:
            # If 24 hours have passed since the last cleanup
            if time.time() - last_cleanup_time >= 86400:
                folder_cleanup()
                last_cleanup_time = time.time()

            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()
