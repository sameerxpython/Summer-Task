import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@example.com"
password = "your_app_password"  # Use App Password if 2FA is on

# Create the email
subject = "Test Email from Python"
body = "Hello, this is a test email sent using Python."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Attach the email body
message.attach(MIMEText(body, "plain"))

try:
    # Connect to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
