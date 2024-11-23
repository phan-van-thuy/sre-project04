# Log Management Automation Script
# This script is designed to handle log rotation and archiving automatically
import os
import shutil
from datetime import datetime
# Define the directory paths
LOG_DIR = "/home/sre/course4"  # Directory where logs are stored
ARCHIVE_DIR = "/home/sre/course4/archive"  # Directory where archived logs are saved
# Define the storage threshold percentage
MAX_STORAGE_THRESHOLD = 80  # If storage exceeds 80%, logs will be archived
def check_storage():
    """
    Checks the disk usage of the log directory.
    Returns:
        float: The percentage of disk space used in the log directory.
    """
    usage = shutil.disk_usage(LOG_DIR)
    percent_used = (usage.used / usage.total) * 100
    return percent_used

def archive_logs():
    """
    Archives the log files by compressing them into a zip file and moving them to the archive directory. Deletes original logs after successful archiving.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Current timestamp for unique archive name
    archive_path = os.path.join(ARCHIVE_DIR, f"logs_{timestamp}.zip")
    shutil.make_archive(archive_path.replace(".zip", ""), 'zip', LOG_DIR)
    
    # Delete the original log files after archiving
    for log_file in os.listdir(LOG_DIR):
        if log_file.endswith(".log"):
            os.remove(os.path.join(LOG_DIR, log_file))

if __name__ == "__main__":
    """
    Main execution block:
    - Checks storage usage of the log directory.
    - If usage exceeds the defined threshold, archives the logs.
    """
    if check_storage() > MAX_STORAGE_THRESHOLD:
        archive_logs()
        print("Logs archived successfully.")
