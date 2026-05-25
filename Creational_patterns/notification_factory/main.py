from factory import NotificationFactory


email = NotificationFactory.create_notification("email")
email.send("Welcome via Email!")

sms = NotificationFactory.create_notification("sms")
sms.send("OTP sent via SMS!")

push = NotificationFactory.create_notification("push")
push.send("You received a new alert!")