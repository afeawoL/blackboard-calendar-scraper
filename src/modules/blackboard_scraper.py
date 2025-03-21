import json
import dateparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from config.settings import BLACKBOARD_USER, BLACKBOARD_PASSWORD

def init_driver():
    """Initializes and returns a Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver

def login_blackboard(driver):
    """Logs into Blackboard using stored credentials."""
    driver.get(BLACKBOARD_URL)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_id")))

    # Input username and password securely
    driver.find_element(By.ID, "user_id").send_keys(BLACKBOARD_USER)
    driver.find_element(By.ID, "password").send_keys(BLACKBOARD_PASSWORD)

    driver.find_element(By.ID, "entry-login").click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "course-menu")))
    print("Logged into Blackboard")


def scrape_assignments(driver):
    """Scrapes assignments from Blackboard and returns them as a list of dictionaries."""
    assignments = []
    driver.get(BLACKBOARD_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#div_25_1 a")))
    course_links = driver.find_elements(By.CSS_SELECTOR, 'div#div_25_1 > div > ul > li > a')
    
    for course in course_links:
        course_name = course.text
        course.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul#content_listContainer")))
        items = driver.find_elements(By.CSS_SELECTOR, 'ul#content_listContainer > li')
        
        for item in items:
            try:
                title = item.find_element(By.CSS_SELECTOR, 'span[style]').text
                due_date_text = item.find_element(By.CSS_SELECTOR, 'div.details').text
                due_date = dateparser.parse(due_date_text)
                
                assignments.append({
                    'title': title,
                    'course': course_name,
                    'dueDate': due_date.isoformat(),
                    'link': driver.current_url,
                    'submitted': False
                })
            except Exception as e:
                print(f"Error parsing an item: {e}")
    
    return assignments

def save_assignments(assignments):
    """Saves assignments to a JSON file."""
    with open(SAVE_PATH, 'w') as file:
        json.dump(assignments, file, indent=2)
    print("Assignments saved!")

def main():
    """Main function to execute scraping."""
    driver = init_driver()
    login_blackboard(driver)
    assignments = scrape_assignments(driver)
    save_assignments(assignments)
    driver.quit()
    return assignments

if __name__ == "__main__":
    main()
