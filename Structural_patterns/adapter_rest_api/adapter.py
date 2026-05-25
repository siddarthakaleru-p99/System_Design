from Structural_patterns.adapter_rest_api.external_api import ExternalUserAPI


class UserAdapter:

    def __init__(self, external_api):
        self.external_api = external_api

    def get_user(self):

        data = self.external_api.get_user_data()

        return {
            "name": data["user_name"],
            "email": data["user_email"]
        }