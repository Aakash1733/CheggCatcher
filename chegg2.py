from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import chegg_mail

# Initialize Chrome driver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://expert.chegg.com/qna/authoring/answer")

# Wait for the user to log in
input("Please log in and press enter to continue...")

# Get the initial page source
default_text = 'Hello, Expert!'
# Refresh the page and check for changes every 5 seconds
while True:
    # Wait for 5 seconds
    time.sleep(5)

    # Refresh the page
    driver.refresh()
    time.sleep(5)
    # Check if the page source has changed
    retry_count=0
    max_retry=3
    current_text="Lul"
    while retry_count<max_retry:
        try:
            current_heading=driver.find_element(By.TAG_NAME,'h4')
            current_text = current_heading.text
            print(current_text)
            break
        except:
            retry_count +=1
            time.sleep(5)
            print("Retrying")
    if current_text != default_text:
        print("Page has changed!")
        chegg_mail.mailkaro()
        input("Press enter to continue again")
        # Update the initial page source to the current page source
