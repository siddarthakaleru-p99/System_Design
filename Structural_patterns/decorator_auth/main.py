from auth_decorator import authenticate


@authenticate
def get_user_profile(user_authenticated):

    print("Fetching user profile data...")


print("Testing with authenticated user:")
get_user_profile(True)
print()

print("Testing with unauthenticated user:")
get_user_profile(False)