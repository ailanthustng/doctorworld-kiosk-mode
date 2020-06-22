import pprint
import base64
import urllib.request

prettyprint = pprint.PrettyPrinter(indent=4).pprint


def create_webapp(androidmanagement, enterprise_name):
    # Icon goes here
    icon_url = 'https://developer.android.com/images/brand/Android_Robot.png'
    web_app_url = 'https://raffles-e-kiosk.doctorworld.co/'
    display_mode = 'FULL_SCREEN'  # other modes: STANDALONE, MINIMAL_UI

    icon_raw_data = urllib.request.urlopen(icon_url).read()
    icon_encoded_data = base64.urlsafe_b64encode(icon_raw_data).decode("utf-8")

    web_app = {
        "title": "Doctor World",
        "startUrl": web_app_url,
        "displayMode": display_mode,
        "icons": [
            {
                "imageData": icon_encoded_data
            }
        ]
    }

    result = androidmanagement.enterprises().webApps().create(
        parent=enterprise_name,
        body=web_app
    ).execute()

    web_app_name = web_app['name']

    prettyprint(result)
    print("Webapp created!")
    print("Your webapp name is:", web_app_name)

    return result


def list_webapps(androidmanagement, enterprise_name):
    webapps = androidmanagement.enterprises().webApps().list(
        parent=enterprise_name
    ).execute()

    prettyprint(webapps)


def delete_webapp(androidmanagement, web_app_name):
    androidmanagement.enterprises().webApps().delete(
        name=web_app_name
    ).execute()
