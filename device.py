import pprint

prettyprint = pprint.PrettyPrinter(indent=4).pprint


def list_devices(androidmanagement, enterprise_name):
    devices = androidmanagement.enterprises().devices().list(
        parent=enterprise_name
    ).execute()

    prettyprint(devices)


def delete_device(androidmanagement, device_name):
    androidmanagement.enterprises().devices().delete(
        name=device_name
    ).execute()


def device_issue_command(androidmanagement, device_name, command):
    result = androidmanagement.enterprises().devices().issueCommand(
        name=device_name,
        body={
            "type": command,
            "duration": "30s",
            # "newPassword": "hello",
            # "resetPasswordFlags": [
            #     "LOCK_NOW",
            #     "REQUIRE_ENTRY"
            # this means that whenever the tablet is rebooted, a password is required to use the
            # ]
        }
    ).execute()

    prettyprint(result)