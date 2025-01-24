import imaplib
import email
from datetime import datetime, timedelta, timezone
import pyperclip

#gmail credentials
EMAIL = "youremail@gmail.com"
APP_PASSWORD = "skib idid opdo pye syes"    #gottabe an app password you have to set yourself: https://support.google.com/accounts/answer/185833?hl=en


def get_verification_code():
    try:
        #connect to Gmail IMAP, if this fails turn it on in gmail settings
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, APP_PASSWORD)
        mail.select("inbox")

        #time limit: how long ago max the authentication mail has to be send, its 0 here
        time_limit = (datetime.now(timezone.utc) - timedelta(minutes=10)).strftime("%d-%b-%Y")
        search_query = f'SINCE {time_limit} SUBJECT "Verification code for Leiden University"'  #change if they change the mail format

        
        result, data = mail.search(None, search_query)      #Search for emails

        if result == "OK" and data[0]:
            
            latest_email_id = data[0].split()[-1]
            result, email_data = mail.fetch(latest_email_id, "(RFC822)")        #fetch the latest one
            
            if result == "OK":
                raw_email = email_data[0][1]
                msg = email.message_from_bytes(raw_email)

                #Extract mail content
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                # Find the verification code
                start = body.find("Verification code for Leiden University additional authentication is:")
            
                if start != -1:
                    code = body[start:].split(":")[1].strip().split()[0]
                    pyperclip.copy(code)
                    print(f"Verification code copied to clipboard: {code}")
                    return

        print("No recent verification email found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Is IMAP turned on? Correct email? Did you set up an app password: https://support.google.com/accounts/answer/185833?hl=en ")
    finally:
        mail.logout()


if __name__ == "__main__":
    get_verification_code()


