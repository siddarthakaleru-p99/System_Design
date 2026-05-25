from functools import wraps


def authenticate(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        is_authenticated = True

        if not is_authenticated:
            print("Access Denied: User not authenticated")
            return

        print("Authentication successful")

        return func(*args, **kwargs)

    return wrapper