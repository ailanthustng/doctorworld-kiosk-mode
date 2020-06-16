import pprint
from apiclient.discovery import build

androidmanagement = build('androidmanagement', 'v1')

def create_enterprise():
    cloud_project_id = 'android-kiosk-test-280419'

    # Solution retrieved from Android Management API Quickstart:
    # https://colab.research.google.com/github/google/android-management-api-samples/blob/master/notebooks/quickstart.ipynb

    CALLBACK_URL = 'https://storage.googleapis.com/android-management-quick-start/enterprise_signup_callback.html'

    # Generate a signup URL where the enterprise admin can signup with a Gmail
    # account.
    signup_url = androidmanagement.signupUrls().create(
        projectId=cloud_project_id,
        callbackUrl=CALLBACK_URL
    ).execute()

    print('Please visit this URL to create an enterprise:', signup_url['url'])

    enterprise_token = input('Enter the code: ')

    # Complete the creation of the enterprise and retrieve the enterprise name.
    enterprise = androidmanagement.enterprises().create(
        projectId=cloud_project_id,
        signupUrlName=signup_url['name'],
        enterpriseToken=enterprise_token,
        body={}
    ).execute()

    enterprise_name = enterprise['name']

    print('\nYour enterprise name is', enterprise_name)

    return enterprise_name
