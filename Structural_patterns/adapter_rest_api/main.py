from Structural_patterns.adapter_rest_api.external_api import ExternalUserAPI
from Structural_patterns.adapter_rest_api.adapter import UserAdapter


external_api = ExternalUserAPI()

adapter = UserAdapter(external_api)

user = adapter.get_user()

print(user)