# config/settings.py

import os

# Blackboard Credentials (GitHub Secrets or .env for local testing)
BLACKBOARD_USER = os.getenv("BLACKBOARD_USER")
BLACKBOARD_PASSWORD = os.getenv("BLACKBOARD_PASSWORD")

# Blackboard details
BLACKBOARD_URL = "https://bsuonline.blackboard.com/ultra/courses"

# Paths
SAVE_PATH = "data/assignments.json"
LOG_PATH = "logs/scraper.log"

# Google API
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "config/credentials.json"

# Google Calendar settings
CALENDAR_ID = "primary"
TIMEZONE = "America/New_York"