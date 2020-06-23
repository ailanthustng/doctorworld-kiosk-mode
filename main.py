import pprint
from apiclient.discovery import build
from enterprise import create_enterprise
from policy import patch_policy
from enrollment_token import create_enrollment_token
from webapp import *
from device import *


prettyprint = pprint.PrettyPrinter(indent=4).pprint


# API Reference:
# https://developers.google.com/android/management/reference/rest


def main():
    androidmanagement = build('androidmanagement', 'v1')
    print("Successfully build androidmanagement instance!")

    # =================================== ENTERPRISE RELATED ==================================
    # Create enterprise if no enterprise
    # cloud_project_id = 'android-kiosk-test-280419'
    # create_enterprise(androidmanagement, cloud_project_id)
    # Enter the enterprise name here
    enterprise_name = 'enterprises/LC03o3xgx8'

    # ==================================== WEB APP RELATED ====================================
    # Edit web app in webapp.py
    # Comment in if want to create / update webapp
    # web_app = create_webapp(androidmanagement, enterprise_name)
    # web_app_name = web_app['name']

    # list_webapps(androidmanagement, enterprise_name)

    # Use list_webapps to get web_app_name
    # web_app_name = ''
    # delete_webapp(androidmanagement, web_app_name)

    # ===================================== POLICY RELATED ====================================
    # Edit policy in policy.py
    # Web app name should be in the form of 'com.google.enterprise.webapp.****'
    # web_app_name = 'com.google.enterprise.webapp.x8026d764ae48f7d4'
    # policy = patch_policy(androidmanagement, enterprise_name, web_app_name)

    # ================================ ENROLLMENT TOKEN RELATED ===============================
    # Default: QR Code (edit in enrollment_token.py if want URL)
    # create_enrollment_token(androidmanagement, enterprise_name, policy)

    # ===================================== DEVICE RELATED ====================================
    # list_devices(androidmanagement, enterprise_name)

    # Use list devices to get device name
    # device_name = 'enterprises/LC03o3xgx8/devices/3790f81e0a0fef76'
    # delete_device(androidmanagement, device_name)

    # Command can be 'REBOOT', 'LOCK', 'RESET_PASSWORD',
    # 'LOCK' means lock the screen
    # If using 'RESET_PASSWORD', edit newPassword and resetPasswordFlags
    # device_name = 'enterprises/LC03o3xgx8/devices/3b5fabf3c7961efe'
    # command = 'REBOOT'
    # password = ''  # leave blank for no password (no need to authenticate when restarting tablet)
    # device_issue_command(androidmanagement, device_name, command, password)


main()
