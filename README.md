# Setting up and Maintenance Guide

- [Android Management API Reference](https://developers.google.com/android/management/reference/rest?authuser=1)
- [Android Management Google API Python Client Documentation](http://googleapis.github.io/google-api-python-client/docs/dyn/androidmanagement_v1.html)

## Setting up

### Create Cloud Project
1. Go to the [Cloud Console](https://console.cloud.google.com).
2. Click **CREATE PROJECT**.
3. Enter your project details, and then click **CREATE**.
4. Take note of the *project ID* and add it into `enterprise.py`.

### Enable Android Enterprise API
1. **Getting started** > **Explore and enable APIs** > **Library** > 
**Search for Android Management API** > **Enable**

### Create Service Account
1. In the Cloud Console, go to the **Create service account key page**.
2. From the Service account list, select **New service account**.
3. In the Service account name field, enter a *name*.
4. From the **Role list**, select **Project** > **Owner**.
5. Click **Create**. A JSON file that contains your key will be downloaded to your computer.
6. If JSON file does not download automatically, under **Keys**, click **Add Key** > **Create new key**. 
Save the JSON.

### Setting up the virtualenv
1. In your terminal:
    1. `pip install virtualenv`
    2. `virtualenv doctorworld`
    3. `source doctorworld/bin/activate`
    4. `pip install google-api-python-client`
2. Download [start.sh](start.sh) and put JSON file in same folder as `start.sh`.
3. Edit the path in `start.sh`.
4. `chmod +x start.sh`.
5. `source start.sh`.
6. Check if env variable has been set correctly: `echo $GOOGLE_APPLICATION_CREDENTIALS`.

### Create Enterprise
1. Enter `cloud_project_id`
2. Run program: `python main.py`
3. Take note of `enterprise_name`
4. Enter `enterprise_name` into `main.py`

### Create Webapp
1. Input `icon`
2. Input `web_app_url`
3. Input `display_mode`
4. Run program: `python main.py`

### Create / Update Policy
1. Input `web_app_name`
2. Things to take note:
    1. has to be `False` during setup:
        1. `installAppsDisabled` (to allow for tablet to install Chrome)
        2. `mobileNetworksConfigDisabled` (to allow for tablet to connect to LTE)
        3. `wifiConfigDisabled` (to allow for tablet to connect to Wifi)
    2. `kioskCustomization`
        - `powerButtonActions`:
            - `POWER_BUTTON_AVAILABLE`
            - `POWER_BUTTON_BLOCKED` *(default)*
        - `systemErrorWarnings`:
            - `ERROR_AND_WARNINGS_ENABLED` *(default)*
            - `ERROR_AND_WARNINGS_MUTED`
        - `systemNavigation`:
            - `NAVIGATION_ENABLED`
            - `NAVIGATION_DISABLED` *(default)*
            - `HOME_BUTTON_ONLY`
        - `statusBar`:
            - `NOTIFICATIONS_AND_SYSTEM_INFO_ENABLED`
            - `NOTIFICATIONS_AND_SYSTEM_INFO_DISABLED` *(default)*
            - `SYSTEM_INFO_ONLY`
        - `deviceSettings`:
            - `SETTINGS_ACCESS_ALLOWED`
            - `SETTINGS_ACCESS_BLOCKED` *(default)*
    3. `statusReportingSettings` (status report for enrolled devices when using `list_devices`)
3. Run program: `python main.py`

### Create Enrollment Token (to enroll the device when first setting up)
1. Comment in `web_app_name`, `policy` and `create_enrollment_token`.
2. Default time to live for token is **1hr** from creation.
3. Run program: `python main.py`

### Enrolling the device
1. Prerequisites:
    - Factory reset device
    - Enrollment token created
2. At the login screen: enter `afw#setup` as username. 
This allows the device to install **Android Device Policy**.
3. Device will prompt you to encrypt device. Tap **Encrypt**.
4. After encryption, device will prompt you to set up. Tap **Next** until screen to scan QR Code.
5. Scan the Enrollment Token QR Code.
6. Let device install everything.
7. Done!

--- 

## Maintenance

### `device_issue_command`
Send a command to the device.

1. Input `device_name` (get from `list_devices`)
2. Input `command`
    - `REBOOT` (sends a command to restart the device)
    - `LOCK` (sends a command to lock the screen)
    - `RESET_PASSWORD` (sends a command to lock device with a password only active after reboot)
- `RESET_PASSWORD`
    - Leave password *empty* if you do not want authentication when restarting tablet.
    - Having a password means having to authenticate whenever the device is rebooted.
3. Run program: `python main.py`


### `delete_device` 
> WARNING: deleting a device means **factory resetting** the device, 
> as well as **removing the device** from your enterprise.

1. Input `device_name`
2. Run program: `python main.py`

### `list_devices` 
Retrieve the list of enrolled devices and their statuses.
 
- Things to look out for:
    1. `displays`:
        - `state`: should be `ON`
    2. `memoryEvents`:
        - Should not have any external storage detected.
    3. `securityPosture`:
        - `devicePosture`
    4. `powerManagementEvents`:
        - `batteryLevel`

1. Run program: `python main.py`