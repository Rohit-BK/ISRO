
import smtplib
import qkd_service
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class EmailServer:
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

    def receive_email(self):
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_address, self.password)
            messages = server.get_messages()
            server.quit()
            return messages
        except Exception as e:
            print("Failed to receive email:", str(e))

    def decrypt_messages(self, messages):
        decrypted_messages = []
        for message in messages:
            encrypted_message = message.get_body()
            decrypted_message = self.qkd_service.decrypt_message(encrypted_message)
            decrypted_messages.append(decrypted_message)
        return decrypted_messages

    def run(self):
        self.configure_smtp_server("smtp.example.com", 587)
        self.configure_email_account("your_email@example.com", "your_password")
        self.set_qkd_service(qkd_service.QKDService())

        received_messages = self.receive_email()
        decrypted_messages = self.decrypt_messages(received_messages)

        print("Decrypted Messages:")
        for message in decrypted_messages:
            print(message)

