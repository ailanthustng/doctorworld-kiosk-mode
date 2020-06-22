import pprint

prettyprint = pprint.PrettyPrinter(indent=4).pprint


def patch_policy(androidmanagement, enterprise_name, web_app_name):
    policy_name = enterprise_name + '/policies/kiosk_mode'

    policy = {
        "applications": [
            {
                "packageName": web_app_name,
                "installType": "KIOSK",
                "defaultPermissionPolicy": "GRANT"
            },
            {
                "packageName": "com.android.chrome",
                "installType": "FORCE_INSTALLED",
                "managedConfiguration": {
                    "URLBLacklist": ["*"],
                    "URLWhitelist": ["web.app.url"]
                },
                "defaultPermissionPolicy": "GRANT"
            }
        ],
        "installAppsDisabled": True,  # has to be False during setup
        "mobileNetworksConfigDisabled": True,  # has to be False during setup
        "wifiConfigDisabled": False,  # has to be False during setup
        "kioskCustomization": {  # customize the KIOSK mode here
            "powerButtonActions": "POWER_BUTTON_BLOCKED",
            "systemErrorWarnings": "ERROR_AND_WARNINGS_ENABLED",
            "systemNavigation": "NAVIGATION_DISABLED",
            "statusBar": "NOTIFICATIONS_AND_SYSTEM_INFO_DISABLED",
            "deviceSettings": "SETTINGS_ACCESS_BLOCKED"
        },
        "statusReportingSettings": {  # customize the status report from list_devices
            "applicationReportsEnabled": True,
            "deviceSettingsEnabled": True,
            "softwareInfoEnabled": True,
            "memoryInfoEnabled": True,
            "networkInfoEnabled": True,
            "displayInfoEnabled": True,
            "powerManagementEventsEnabled": True,
            "hardwareStatusEnabled": True,
            "systemPropertiesEnabled": True,
            "applicationReportingSettings": {
                "includeRemovedApps": True
            }
        },
        "addUserDisabled": True,
        "factoryResetDisabled": True,
        "mountPhysicalMediaDisabled": True,
        "modifyAccountsDisabled": True,
        "uninstallAppsDisabled": True,
        "keyguardDisabled": True,  # lock screen related stuff
        "bluetoothContactSharingDisabled": True,
        "bluetoothConfigDisabled": True,
        "cellBroadcastsConfigDisabled": True,
        "credentialsConfigDisabled": True,
        "tetheringConfigDisabled": True,
        "vpnConfigDisabled": True,
        "createWindowsDisabled": True,
        "networkResetDisabled": True,
        "outgoingCallsDisabled": True,
        "removeUserDisabled": True,
        "smsDisabled": True,
        "unmuteMicrophoneDisabled": True,  # do we need this?
        "usbFileTransferDisabled": True,
        "stayOnPluggedModes": [
            "USB"
        ],
        "dataRoamingDisabled": True,
        "locationMode": "HIGH_ACCURACY",
        "networkEscapeHatchEnabled": True,
        # If a network connection can't be made at boot time, the escape hatch prompts the user to temporarily connect
        # to a network in order to refresh the device policy. After applying policy, the temporary network will be
        # forgotten and the device will continue booting. This prevents being unable to connect to a network if there
        # is no suitable network in the last policy and the device boots into an app in lock task mode, or the user is
        # otherwise unable to reach device settings.
        "bluetoothDisabled": True,
        "debuggingFeaturesAllowed": False,
        "funDisabled": True,
        "appAutoUpdatePolicy": "ALWAYS",
    }

    # Write the new policy:
    result = androidmanagement.enterprises().policies().patch(
        name=policy_name,
        body=policy
    ).execute()

    prettyprint(result)

    return result
