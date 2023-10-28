
class EmailTemplates:
    @staticmethod
    def welcome_email(name):
        return f"Dear {name},\n\nWelcome to QuMail! We are excited to have you as a user of our secure email client."

    @staticmethod
    def password_reset_email(name, reset_link):
        return f"Dear {name},\n\nPlease click on the following link to reset your password: {reset_link}"

    @staticmethod
    def subscription_confirmation_email(name):
        return f"Dear {name},\n\nThank you for subscribing to QuMail Plus! Your subscription is now active."

    @staticmethod
    def subscription_expiry_warning_email(name, days_left):
        return f"Dear {name},\n\nYour QuMail Plus subscription will expire in {days_left} days. Please renew your subscription to continue enjoying the benefits."

    @staticmethod
    def subscription_expired_email(name):
        return f"Dear {name},\n\nYour QuMail Plus subscription has expired. Please renew your subscription to continue using the premium features."

    @staticmethod
    def new_message_notification_email(name, sender):
        return f"Dear {name},\n\nYou have received a new message from {sender}. Please log in to your QuMail account to read it."

    @staticmethod
    def account_deletion_confirmation_email(name):
        return f"Dear {name},\n\nYour QuMail account has been successfully deleted. We are sorry to see you go."

    @staticmethod
    def account_deactivation_confirmation_email(name):
        return f"Dear {name},\n\nYour QuMail account has been deactivated. If you wish to reactivate it, please contact our support team."

    @staticmethod
    def account_reactivation_confirmation_email(name):
        return f"Dear {name},\n\nYour QuMail account has been reactivated. Welcome back!"

    @staticmethod
    def account_upgrade_confirmation_email(name):
        return f"Dear {name},\n\nCongratulations! Your QuMail account has been upgraded to QuMail Plus. Enjoy the enhanced features and benefits."

    @staticmethod
    def account_downgrade_confirmation_email(name):
        return f"Dear {name},\n\nYour QuMail Plus subscription has been downgraded. Please note that some features may no longer be available."

    @staticmethod
    def account_update_notification_email(name):
        return f"Dear {name},\n\nYour QuMail account information has been updated. If you did not make these changes, please contact our support team immediately."

    @staticmethod
    def account_verification_email(name, verification_link):
        return f"Dear {name},\n\nThank you for signing up for QuMail. Please click on the following link to verify your email address: {verification_link}"

