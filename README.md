# Google Form Auto-Fill and Email Submission

This project automates the process of filling a Google Form using Selenium and sending an email with the submission details using a Flask web application. The email submission includes required files as attachments.

## Features
- Automatically fills a specified Google Form.
- Captures a screenshot of the form's confirmation page.
- Sends an email with the screenshot and other required attachments.

## Prerequisites
- Python 3.x
- Google Chrome browser
- ChromeDriver
- Selenium
- Flask
- smtplib for sending emails

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mfonekpo/Python_automation_selenium.git
   ```
2. **Install dependencies**
   ```bash
   python3 -m pip install -r requirements.txt
   ```

3. **Download ChromeDriver**
    Ensure you have the Chrome browser installed. Download the ChromeDriver and place it in the project directory.

## Usage

1. **Fill the Google Form and Capture Screenshot**
    - Modify the `fill_form.py` script to match the selectors and fields of your Google Form.
    - Run the `fill_form.py` script to fill the form and capture the confirmation screenshots.

2. **Run the Flask Application**
    - The Flask application will run the `form-filling` script and send an email with the required attachments.
    - Run the code" `python app.py`

3. **Access the Flask Endpoint**
    - Open your browser and navigate to http://127.0.0.1:5000/submit_form to trigger the form submission and email sending process.

## Project Structure

```md
.
├── fill_form.py              # Script to fill the Google Form and capture the screenshot
├── app.py                    # Flask application to trigger form filling and send email
├── README.md                 # Project documentation
├── requirements.txt          # List of dependencies
├── confirmation.png          # Screenshot of the confirmation page (generated after running fill_form.py)
├── source_code.zip           # Zip file of the source code
├── resume.pdf                # Your resume
├── projects.pdf              # Links to past projects/work samples
└── availability.txt          # Confirmation of your availability
```

## Configuration
  - **Email Configuration:** Update the `app.py` file with your email credentials and modify the recipients and subject as required.
  
    ```md
        fromaddr = "your_email@example.com"
        toaddr = "tech@themedius.ai"
        cc = "hr@themedius.ai"
    ```