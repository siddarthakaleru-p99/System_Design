from abc import ABC, abstractmethod


class Subscriber(ABC):

    @abstractmethod
    def update(self, message):
        pass


class UserSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received notification: {message}")


class YouTubeChannel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_subscribers(self, message):

        for subscriber in self.subscribers:
            subscriber.update(message)

    def upload_video(self, title):

        print(f"\nNew Video Uploaded: {title}")

        self.notify_subscribers(
            f"New video uploaded: {title}"
        )