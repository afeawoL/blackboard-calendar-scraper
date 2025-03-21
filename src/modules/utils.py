import logging
import os

# Define log file path
LOG_FILE = "logs/scraper.log"

# Ensure logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_message(message):
    """Logs a message to the log file and prints it to the console."""
    logging.info(message)
    print(message)


