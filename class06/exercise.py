from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

    def send(self, message):
        print(f" The message {message} was successfully sent to {self.email}")
        
class SMSNotifcation(Notification):
    def __init__(self, sms):
        self.sms = sms

    def send(self, message):
        print(f"The SMS  {message} was sent to {self.sms}")
        
def notify(notification, message):
  
    notification.send(message)
        
email = EmailNotification("abc@gmail.com")
sms = SMSNotifcation("123454")

notify(email, "Welcome to the website!")
notify(sms, "Your verification code is 1234")
