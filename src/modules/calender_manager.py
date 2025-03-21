from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from config.settings import SERVICE_ACCOUNT_FILE, SCOPES, CALENDAR_ID, TIMEZONE

def load_calendar_service():
    """Loads the Google Calendar API service."""
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

def add_event(summary, start_time, end_time, description=""):
    """Adds an event to Google Calendar."""
    service = load_calendar_service()
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': TIMEZONE},
        'end': {'dateTime': end_time, 'timeZone': TIMEZONE},
        'description': description
    }
    created_event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print(f"Event created: {created_event.get('htmlLink')}")
    return created_event

def list_upcoming_events(max_results=10):
    """Lists upcoming events from Google Calendar."""
    service = load_calendar_service()
    events_result = service.events().list(
        calendarId=CALENDAR_ID, maxResults=max_results, singleEvents=True,
        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    if not events:
        print("No upcoming events found.")
        return []
    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"{start}: {event['summary']}")
    
    return events
