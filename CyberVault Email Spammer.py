import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import pyfiglet


def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        # Close the connection
        server.quit()

def main():
    sender_email = 'Email' #Enter in the email address of the desired sender
    sender_password = 'Password' #Enter in the email password of the desired sender
    print(pyfiglet.figlet_format("CyberVault Email Spammer", font='big'))  # Print CyberVault in big letters
    print("Welcome to CyberVault's Email Spammer!")

    while True:
        receiver_email = input("Enter recipient's email address: ")
        subject = input("Enter email subject: ")
        body = input("Enter email body: ")

        print("Sending email every 1 second...")

        email_count = 0
        while True:
            send_email(sender_email, sender_password, receiver_email, subject, body)
            email_count += 1

            if email_count % 10 == 0:
                print("Select an option:")
                print("1. Continue sending emails")
                print("2. Enter a new email address")
                print("3. Exit")
                choice = input("Enter your choice (1, 2, or 3): ").upper()
                if choice == '3':
                    return
                elif choice == '2':
                    break

            time.sleep(1)  # Sleep for 1 second between emails

if __name__ == "__main__":
    main()
