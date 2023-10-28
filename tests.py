
import unittest
from unittest.mock import patch
from email_client import EmailClient

class TestEmailClient(unittest.TestCase):
    def setUp(self):
        self.client = EmailClient()
        self.client.configure_smtp_server("smtp.example.com", 587)
        self.client.configure_email_account("your_email@example.com", "your_password")

    @patch('builtins.input', side_effect=["recipient@example.com", "Test Subject", "Test Message"])
    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp, mock_input):
        self.client.send_email("recipient@example.com", "Test Subject", "Test Message")
        mock_smtp.assert_called_once_with("smtp.example.com", 587)
        mock_smtp.return_value.starttls.assert_called_once()
        mock_smtp.return_value.login.assert_called_once_with("your_email@example.com", "your_password")
        mock_smtp.return_value.sendmail.assert_called_once_with("your_email@example.com", "recipient@example.com", mock_smtp.return_value.sendmail.call_args[0][2].as_string())
        mock_smtp.return_value.quit.assert_called_once()

    @patch('builtins.input', side_effect=["recipient@example.com", "Test Subject", "Test Message"])
    @patch('smtplib.SMTP', side_effect=Exception("Failed to send email"))
    def test_send_email_failure(self, mock_smtp, mock_input):
        with patch('builtins.print') as mock_print:
            self.client.send_email("recipient@example.com", "Test Subject", "Test Message")
            mock_print.assert_called_once_with("Failed to send email:", "Failed to send email")

if __name__ == "__main__":
    unittest.main()

