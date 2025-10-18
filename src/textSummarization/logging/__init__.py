import os
import sys
import logging

# Define log message format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create a "logs" folder in the root directory if it doesn’t exist
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create the log file path
log_filepath = os.path.join(log_dir, "running_logs.log")

# Set up basic logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),   # save logs to file
        logging.StreamHandler(sys.stdout)    # print logs to terminal
    ]
)

# Create the logger instance
logger = logging.getLogger("textSummarizationLogger")