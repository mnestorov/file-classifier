![File_Classifier](images/file-classifier.png)

# File Classifier

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## Support The Project

Your support is greatly appreciated and will help ensure the project's continued development and improvement. Thank you for being a part of the community!

[![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)](https://buy.stripe.com/7sI6qagF4cQV4xy5kk) [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.me/mnestorov)

## Overview

The File Classifier is a Python script that monitors a specified directory (typically the Downloads folder) and automatically organizes files into different folders based on their file types and the date they were created or last modified. It can also identify and delete duplicate files.

## Prerequisites

**To run the File Classifier, you need:**

- Python 3.6 or later
- The watchdog package for monitoring the directory

**You can install the watchdog package using the following command:**

```
pip install watchdog
```

## Installation

Download the main script file `main.py` and the configuration file `config.py`.

Open the `config.py` file and modify the **download_folder** variable to the path of the directory you want to monitor (e.g., your Downloads folder).

In the same file, you can also modify the **classification_rules** dictionary to customize the folders and file types used for classification. The key is the folder name, and the value is a list of file extensions.

Optionally, you can customize the **GREEN** and **RESET** variables in `config.py` to change the color of the printed messages.

## Usage

Open a terminal or command prompt, navigate to the folder containing the `main.py` and `config.py` files.

**Run the script using the following command:**

```
python main.py
```

The script will start monitoring the specified directory. When a new file is added or an existing file is modified, the script will automatically move the file to the appropriate folder based on its file type and date.

If a duplicate file is detected, the script will delete it, provided that it has the same name as the original file plus a number in parentheses (e.g., "invoice (1).pdf").

**To stop the script, press** `Ctrl+C`.

## Bash Command

To use bash command to run the script, first make sure that the Python script file `main.py` is executable. 

**You can do this by running the following command in your terminal:**

```
chmod +x main.py
```

**Also, make the bash script executable by running:**

```
chmod +x start.sh
```

## Customization

- To add more file types or folders for classification, edit the **classification_rules** dictionary in the `config.py` file.

- To change the date format used for organizing files, modify the strftime format string in the **get_date_folder** function within the `main.py` file.

## Run the script at startup

To run the script at startup on Ubuntu, you have a few options.

**One common approach is to add an entry to the "Startup Applications" tool:**

- Open the **"Startup Applications"** tool by searching for it in the Activities overview or running `gnome-session-properties` in the terminal.
- Click the **"Add"** button.
- Fill in the **"Name"** field (e.g., **"Start File Classifier"**).
- In the **"Command"** field, enter the full path to the start_services.sh script (e.g., `/home/YOUR_USERNAME/path/to/script/start.sh`).
- Click **"Add"** and close the **"Startup Applications"** tool.

Now, the bash script will run automatically when you log in to your Ubuntu system.

**Note:** Please note that this approach will only work when you log in with a graphical environment, as it relies on the GNOME startup applications feature. If you need to run the script in a non-GUI environment or before user login, you may need to use a different method, such as a systemd service or a cron job.

## TODOs

- **_File size-based classification_**: Classify files based on their size (e.g., create separate folders for small, medium, and large files) in addition to their file type.

- [x] **_Date-based classification_**: ~~Organize files into folders based on the date they were created or last modified~~.

- **_File content-based classification_**: For specific file types, such as text files or code files, classify them based on their content (e.g., programming language, presence of specific keywords).

- **_User-defined classification_**: Allow users to define their own custom classification rules, such as regular expressions or other matching criteria, to create a more personalized organization system.

- [x] **_Logging_**: ~~Keep a log of all actions performed by the script, such as files moved or deleted, for better traceability and understanding of the changes made~~.

- **_Undo functionality_**: Implement an undo feature that allows users to revert the script's actions if they accidentally move or delete a file.

- [x] **_Automatic folder cleanup_**: ~~Periodically check the folders for old files and either move them to an archive folder or delete them based on user preferences~~.

- **_Notifications_**: Send notifications to the user when certain events occur, such as the creation of new files or the detection of duplicate files.

- **_File integrity check_**: Perform a file integrity check (e.g., using checksums) to ensure that duplicate files are not only similar in name but also identical in content before deleting them.

- **_GUI_**: Develop a graphical user interface (GUI) for the script, making it more user-friendly and easier to configure and monitor.

## Support The Project

If you find this script helpful and would like to support its development and maintenance, please consider the following options:

- **_Star the repository_**: If you're using this script from a GitHub repository, please give the project a star on GitHub. This helps others discover the project and shows your appreciation for the work done.

- **_Share your feedback_**: Your feedback, suggestions, and feature requests are invaluable to the project's growth. Please open issues on the GitHub repository or contact the author directly to provide your input.

- **_Contribute_**: You can contribute to the project by submitting pull requests with bug fixes, improvements, or new features. Make sure to follow the project's coding style and guidelines when making changes.

- **_Spread the word_**: Share the project with your friends, colleagues, and social media networks to help others benefit from the script as well.

- **_Donate_**: Show your appreciation with a small donation. Your support will help me maintain and enhance the script. Every little bit helps, and your donation will make a big difference in my ability to keep this project alive and thriving.

[![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)](https://buy.stripe.com/7sI6qagF4cQV4xy5kk) [![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://www.paypal.me/mnestorov)

Your support is greatly appreciated and will help ensure the project's continued development and improvement. Thank you for being a part of the community!

---

## License

This project is licensed under the MIT License.
