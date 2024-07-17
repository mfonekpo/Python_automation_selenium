from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv()

def fill_google_form():
    # Setup WebDriver (Chrome in this case)
    driver = webdriver.Chrome()
    driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

    # Wait for the form to load
    time.sleep(3)


    # Get the needed fields
    full_name = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    contact_number = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    email_id = driver .find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    full_address = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
    pincode = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
    dob = driver.find_elements(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
    
    
    gender = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
    captcha = driver.find_element(By.XPATH, '//*[@id="i30"]/span[1]/b')



    # Capture the second screenshot (bottom part)
    driver.save_screenshot("bottom_screenshot.png")
    

    # fill the form with the values
    full_name.send_keys(os.getenv("FULL_NAME"))
    contact_number.send_keys(os.getenv("CONTACT_NUMBER"))
    email_id.send_keys(os.getenv("EMAIL_ID"))
    full_address.send_keys(os.getenv("FULL_ADDRESS"))

        # Capture the first screenshot (top part)
    driver.save_screenshot("./screenshots/top_screenshot.png")
    pincode.send_keys(os.getenv("PIN_CODE"))
    dob[0].send_keys(os.getenv("DOB"))
    gender.send_keys(os.getenv("GENDER"))
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(captcha.text)

    # capture the bottom part
    driver.save_screenshot('./screenshots/bottom_screenshot.png')

    # Submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_button.click()

    # capture a screenshot of the submitted form
    driver.save_screenshot('./screenshots/submission_screenshot.png')

    # Wait for confirmation page to load and take a screenshot
    time.sleep(3)

    # Close the browser
    driver.quit()

fill_google_form()
