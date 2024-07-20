import os

# Retrieve the Zendesk user email from the environment variable
ZENDESK_USER_EMAIL = os.getenv('ZENDESK_USER_EMAIL')

if ZENDESK_USER_EMAIL is None:
    print("Error: The environment variable ZENDESK_USER_EMAIL is not set.")
else:
    print(f"The Zendesk user email is: {ZENDESK_USER_EMAIL}")

# You can now use ZENDESK_USER_EMAIL in your application, for example:
# zendesk_api = ZendeskAPI(email=ZENDESK_USER_EMAIL, token=ZENDESK_API_TOKEN)
