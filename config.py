# Set the path to your downloads folder
download_folder = '/path/to/your/downloads/folder'

# Define the classification rules
classification_rules = {
    'Images': ['.jpg', '.jpeg', '.png', '.svg', '.webp'],
    'Videos': ['.mp4'],
    'Datasets': ['.csv', '.xlsx', '.json', '.sql'],
    'PDFs': ['.pdf'],
    'Archives': ['.zip', '.rar']
}

# Automatic folder cleanup
DAYS_BEFORE_ARCHIVE = 30  # You can change this value based on your requirement
ARCHIVE_ACTION = "move"  # "move" or "delete"
ARCHIVE_FOLDER = "Archived"

# ANSI escape code for green text
GREEN = '\033[32m'
RESET = '\033[0m'

# Log filename
log_filename = 'app.log'