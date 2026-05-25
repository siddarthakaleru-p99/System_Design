class User:

    def __init__(
        self,
        name,
        age=None,
        email=None,
        city=None,
        phone=None
    ):
        self.name = name
        self.age = age
        self.email = email
        self.city = city
        self.phone = phone

    def __str__(self):
        return (
            f"User(\n"
            f"  name={self.name}, \n"
            f"  age={self.age}, \n"
            f"  email={self.email}, \n"
            f"  city={self.city}, \n"
            f"  phone={self.phone}\n"
            f")"
        )


class UserBuilder:

    def __init__(self, name):
        self.name = name
        self.age = None
        self.email = None
        self.city = None
        self.phone = None

    def set_age(self, age):
        self.age = age
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_city(self, city):
        self.city = city
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def build(self):
        return User(
            self.name,
            self.age,
            self.email,
            self.city,
            self.phone
        )