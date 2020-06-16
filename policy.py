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
        "addUserDisabled": True,
        "factoryResetDisabled": True,
        # "installAppsDisabled": True, # this has to be disabled when first setting up a device
        "mountPhysicalMediaDisabled": True,
        "modifyAccountsDisabled": True,
        "uninstallAppsDisabled": True,
        "keyguardDisabled": True,  # lock screen related stuff
        "statusReportingSettings": {
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
        "bluetoothContactSharingDisabled": True,
        # "wifiConfigDisabled": True,
        "bluetoothConfigDisabled": True,
        "cellBroadcastsConfigDisabled": True,
        "credentialsConfigDisabled": True,
        "mobileNetworksConfigDisabled": True,
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
        # "debuggingFeaturesAllowed": True, #temporarily removed to enable debugging while testing
        "funDisabled": True,
        "appAutoUpdatePolicy": "ALWAYS",
        "kioskCustomization": {
            "powerButtonActions": "POWER_BUTTON_BLOCKED",
            "systemErrorWarnings": "ERROR_AND_WARNINGS_ENABLED",
            "systemNavigation": "NAVIGATION_DISABLED",
            "statusBar": "NOTIFICATIONS_AND_SYSTEM_INFO_DISABLED",
            "deviceSettings": "SETTINGS_ACCESS_BLOCKED"
        },
    }

    # Write the new policy:
    result = androidmanagement.enterprises().policies().patch(
        name=policy_name,
        body=policy
    ).execute()

    prettyprint(result)

    return result
