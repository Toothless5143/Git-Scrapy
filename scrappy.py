from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the path to your chromedriver
cdp = "/Users/ryan/Desktop/developer/chromedriver"
driver = webdriver.Chrome(executable_path=cdp)

# Prompt the user to enter the username
username = input("Enter the GitHub username: ")

url = f"https://github.com/{username}"
driver.get(url)

# Wait for the page to load (optional)
# time.sleep(2)

# Find all elements with class name "repo"
repos = driver.find_elements(By.CLASS_NAME, "repo")

# Wait for the elements to load (optional)
# time.sleep(2)

links = []

def get_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME, "js-permalink-replaceable-link")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    if "password" in html:
        print(f"Found password on {second_page}")

def loop(next_page):
    global links
    # Do something with the next page
    links.append(next_page)

# Call the functions or perform the desired actions here