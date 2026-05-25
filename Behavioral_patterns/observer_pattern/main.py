from Behavioral_patterns.observer_pattern.observer import (
    YouTubeChannel,
    UserSubscriber
)


channel = YouTubeChannel()

user1 = UserSubscriber("Siddartha")
user2 = UserSubscriber("Sushank")
user3 = UserSubscriber("Shiva Ram")

channel.subscribe(user1)
channel.subscribe(user2)
channel.subscribe(user3)

channel.upload_video("Observer Pattern in Python")