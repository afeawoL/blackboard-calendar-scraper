# Blackboard Calendar Scraper

This script scrapes assignments from Blackboard and syncs them with Google Calendar.

## 🚀 Setup & Installation

### **1️⃣ Clone the Repository**
```bash
git clone <repo-url>
cd blackboard_calendar_scraper
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Up Google API Credentials**
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the **Google Calendar API**.
4. Generate a service account key and download `credentials.json`.
5. Place `credentials.json` inside the `config/` folder.
6. Share your Google Calendar with the service account email (found in `credentials.json`).

### **4. Run the Script**
```bash
./run.sh
```

Current Features
- Scrapes assignments from Blackboard  
- Saves data in JSON format  
- Automatically syncs to Google Calendar  

In-Progress Features
- 
- 
- 

---
**Author:** github.com/afeawoL
