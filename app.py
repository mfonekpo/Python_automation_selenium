from flask import Flask, request
import yagmail
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/submit_form', methods=['GET'])
def submit_form():
    send_email()
    return "Email Sent"

def send_email():
    fromaddr = os.getenv("EMAIL_ID")
    toaddr = "tech@themedius.ai"
    cc = "hr@themedius.ai"

    subject = f"Python (Selenium) Assignment - {os.getenv('FULL_NAME')}"

    body = """
    Please find the attached files for the assignment submission.

    1. Screenshot of the form filled via code (as mentioned in STEP 3 of the assignment).
    2. Github Source code: https://github.com/mfonekpo/Python_automation_selenium
    3. Brief documentation of your approach:
    In this Python automation project, my initial step was to thoroughly understand the problem and define the expected deliverables. 
    Once I had a clear grasp of the requirements and identified the appropriate tools to achieve them, 
    I proceeded to set up my Python environment and install the necessary libraries.
    Given that this was a web automation project, I conducted a comprehensive analysis of the target URL. 
    This reconnaissance allowed me to identify key elements to focus on, thereby streamlining the automation process. 
    After completing the web analysis, I moved on to the next phase, which involved submitting the results via email. 
    Upon ensuring that all deliverables were met and verified, the project was successfully concluded.
    4. Resume attached accordingly
    5. Past projects:
       1. https://github.com/mfonekpo/ELT-pipeline/blob/main/ELT_pipeline/data_pipeline_mod.py
       2. https://github.com/mfonekpo/Interesting-sights-in-Nigeria
       3. https://github.com/mfonekpo/Dev-Career
       4. https://github.com/mfonekpo/Sentiment-Analysis
       5. https://github.com/mfonekpo/NER-Project
    6. Yes, I will be available for a full-time role for the next 3-6 months.
    """

    filenames = [
        './screenshots/top_screenshot.png',
        './screenshots/bottom_screenshot.png',
        './screenshots/submission_screenshot.png',
        './Mfon Ekpo.pdf'
    ]

    yag = yagmail.SMTP(fromaddr, os.getenv("EMAIL_PWD"))
    yag.send(
        to=[toaddr, cc],
        subject=subject,
        contents=body,
        attachments=filenames
    )

    print("Email sent successfully.")

if __name__ == '__main__':
    app.run(debug=True)