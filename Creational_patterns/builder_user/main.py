from user import UserBuilder


user = (
    UserBuilder("Siddartha")
    .set_age(21)
    .set_email("siddartha@gmail.com")
    .set_city("Hyderabad")
    .set_phone("9876543210")
    .build()
)

print(user)