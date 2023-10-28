
import email_client
import qkd_service

def main():
    # Initialize the email client
    client = email_client.EmailClient()

    # Set up the QKD service
    qkd = qkd_service.QKDService()

    # Configure the email client with the QKD service
    client.set_qkd_service(qkd)

    # Run the email client
    client.run()

if __name__ == "__main__":
    main()

