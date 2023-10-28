
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class EmailClient:
    def __init__(self):
        self.smtp_server = None
        self.smtp_port = None
        self.email_address = None
        self.password = None
        self.qkd_service = None

    def set_qkd_service(self, qkd_service):
        self.qkd_service = qkd_service

    def configure_smtp_server(self, smtp_server, smtp_port):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def configure_email_account(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def send_email(self, recipient, subject, message):
        encrypted_message = self.qkd_service.encrypt_message(message)

        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = recipient
        msg['Subject'] = Header(subject, 'utf-8')

        msg.attach(MIMEText(encrypted_message, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_address, self.password)
            server.sendmail(self.email_address, recipient, msg.as_string())
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print("Failed to send email:", str(e))

    def run(self):
        recipient = input("Enter recipient email address: ")
        subject = input("Enter email subject: ")
        message = input("Enter email message: ")
        self.send_email(recipient, subject, message)
