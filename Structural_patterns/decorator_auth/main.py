from auth_decorator import authenticate


@authenticate
def get_user_profile():

    print("Fetching user profile data...")


get_user_profile()