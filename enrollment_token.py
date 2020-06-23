import pprint
from urllib.parse import urlencode

prettyprint = pprint.PrettyPrinter(indent=4).pprint


def create_enrollment_token(androidmanagement, enterprise_name, policy):

    policy_name = policy['name']

    enrollment_token = androidmanagement.enterprises().enrollmentTokens().create(
        parent=enterprise_name,
        body={"policyName": policy_name}
    ).execute()

    prettyprint(enrollment_token)

    # QR Code
    image = {
        'cht': 'qr',
        'chs': '500x500',
        'chl': enrollment_token['qrCode']
    }

    qrcode_url = 'https://chart.googleapis.com/chart?' + urlencode(image)
    print('Please visit this URL to scan the QR code:', qrcode_url)

    # Link
    # enrollment_link = 'https://enterprise.google.com/android/enroll?et=' + enrollment_token['value']
    # print('Please open this link on your device:', enrollment_link)

