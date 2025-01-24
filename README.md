# LeidenUniv-AuthScript
A automated script that fetches the 2FA Verification Code from your mail and displays it in terminal / copies it


This Python script automates the process of retrieving verification codes sent to your Gmail account by Leiden University. It simplifies authentication by scanning your inbox for recent emails, extracting the verification code, and copying it to your clipboard—all in one click!

**Features**

    Automated Email Search: Scans your Gmail inbox for emails with the subject "Verification code for Leiden University".
    Time Filtering: Only processes emails received within the last 10 minutes for security.
    Verification Code Extraction: Extracts the numeric code from the email content.
    Clipboard Integration: Copies the extracted code to your clipboard for quick use.

**Prerequisites**

    Python: Make sure Python 3.7 or higher is installed on your machine.
    Gmail IMAP Access:
        Enable IMAP in your Gmail account settings (instructions here).
        Generate an App Password to use with the script.
    Dependencies: Install the required Python packages using pip:

    pip install pyperclip imapclient pyzmail36

**Installation**

    Clone this repository to your local machine:

git clone https://github.com/yourusername/leiden-auth-script.git

Navigate to the project folder:

    cd leiden-auth-script

**Configuration
**
    Open the script file (main.py) in your favorite editor.
    Update the following variables with your Gmail credentials:

    EMAIL = "your_email@gmail.com"
    APP_PASSWORD = "your_app_password"

**Usage**

    Run the script:

python main.py

If a recent email is found with the verification code, the script will:

    Display the code in the terminal.
    Copy the code directly to your clipboard.

If no email is found within the past 10 minutes, you'll see a message:

    No recent verification email found.  

**Example Output**

    Code Found:

Verification code copied to clipboard: 123456  

No Email Found:

    No recent verification email found.  

**Troubleshooting
**
    Deprecation Warning: If you see warnings related to datetime.utcnow(), ensure you are using the latest script version where timezone-aware datetime is used.
    IMAP Errors: Double-check that IMAP access is enabled in your Gmail account, and ensure your App Password is correct.
    No Emails Found: Ensure the subject line of the email matches "Verification code for Leiden University" exactly.
