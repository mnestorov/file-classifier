# File Classifier

## Overview

The File Classifier is a Python script that monitors a specified directory (typically the Downloads folder) and automatically organizes files into different folders based on their file types and the date they were created or last modified. It can also identify and delete duplicate files.

## Prerequisites

To run the File Classifier, you need:

- Python 3.6 or later
- The watchdog package for monitoring the directory

**You can install the watchdog package using the following command:**

```
pip install watchdog
```

## Installation

Download the main script file `file_classifier.py` and the configuration file `config.py`.

Open the `config.py` file and modify the **download_folder** variable to the path of the directory you want to monitor (e.g., your Downloads folder).

In the same file, you can also modify the classification_rules dictionary to customize the folders and file types used for classification. The key is the folder name, and the value is a list of file extensions.

Optionally, you can customize the **GREEN** and **RESET** variables in `config.py` to change the color of the printed messages.

## Usage

Open a terminal or command prompt, navigate to the folder containing the `file_classifier.py` and `config.py` files.

**Run the script using the following command:**

```
python file_classifier.py
```

The script will start monitoring the specified directory. When a new file is added or an existing file is modified, the script will automatically move the file to the appropriate folder based on its file type and date.

If a duplicate file is detected, the script will delete it, provided that it has the same name as the original file plus a number in parentheses (e.g., "invoice (1).pdf").

**To stop the script, press** `Ctrl+C`.

## Bash Command

To use bash command to run the script, first make sure that the Python script file `file_classifier.py` is executable. 

**You can do this by running the following command in your terminal:**

```
chmod +x file_classifier.py
```

**Also, make the bash script executable by running:**

```
chmod +x file_classifier.sh
```

## Customization

- To add more file types or folders for classification, edit the **classification_rules** dictionary in the `config.py` file.

- To change the date format used for organizing files, modify the strftime format string in the **get_date_folder** function within the `file_classifier.py` file.

## TODO


- **_File size-based classification_**: Classify files based on their size (e.g., create separate folders for small, medium, and large files) in addition to their file type.

- [x] **_Date-based classification_**: ~~Organize files into folders based on the date they were created or last modified~~.

- **_File content-based classification_**: For specific file types, such as text files or code files, classify them based on their content (e.g., programming language, presence of specific keywords).

- **_User-defined classification_**: Allow users to define their own custom classification rules, such as regular expressions or other matching criteria, to create a more personalized organization system.

- [x] **_Logging_**: ~~Keep a log of all actions performed by the script, such as files moved or deleted, for better traceability and understanding of the changes made~~.

- **_Undo functionality_**: Implement an undo feature that allows users to revert the script's actions if they accidentally move or delete a file.

- **_Automatic folder cleanup_**: Periodically check the folders for old files and either move them to an archive folder or delete them based on user preferences.

- **_Notifications_**: Send notifications to the user when certain events occur, such as the creation of new files or the detection of duplicate files.

- **_File integrity check_**: Perform a file integrity check (e.g., using checksums) to ensure that duplicate files are not only similar in name but also identical in content before deleting them.

- **_GUI_**: Develop a graphical user interface (GUI) for the script, making it more user-friendly and easier to configure and monitor.