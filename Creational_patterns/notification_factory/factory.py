from notifications import (
    EmailNotification,
    SMSNotification,
    PushNotification
)


class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type.lower() == "email":
            return EmailNotification()

        elif notification_type.lower() == "sms":
            return SMSNotification()

        elif notification_type.lower() == "push":
            return PushNotification()

        else:
            raise ValueError("Invalid notification type")