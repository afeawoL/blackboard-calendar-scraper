
import sys
import os

# Ensure src/ is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.modules.blackboard_scraper import main as scrape_blackboard
from src.modules.calendar_manager import add_event

def main():
    """Orchestrates the Blackboard scraper and Google Calendar sync."""
    print("Starting Blackboard Scraper...")
    assignments = scrape_blackboard()

    print("Syncing with Google Calendar...")
    for assignment in assignments:
        add_event(
            summary=f"{assignment['title']} - {assignment['course']}",
            start_time=assignment['dueDate'],
            end_time=assignment['dueDate'],
            description=f"Assignment link: {assignment['link']}"
        )

    print("All assignments have been synced with Google Calendar!")

if __name__ == "__main__":
    main()


