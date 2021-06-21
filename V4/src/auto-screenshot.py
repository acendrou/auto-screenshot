import time
import os
from mss import mss
from pynput.keyboard import Listener, Key
import configparser
from win10toast import ToastNotifier

# read configuration file : path of the wanted location for the screenshots
config = configparser.ConfigParser()
config.read('config.ini')

screenshotActive = True


def notifier(announce):
    toaster = ToastNotifier()
    toaster.show_toast("auto-screenshot", announce, duration=2, threaded=True)

    # Wait for threaded notification to finish
    while toaster.notification_active():
        time.sleep(0.1)


def on_key_pressed(key):
    print("Key pressed : {0}".format(key))
    if key is Key.pause:
        print("Key pause pressed !")
        global screenshotActive
        if screenshotActive:
            print("Screenshotting halted !")
            notifier("Screenshotting halted !")
            screenshotActive = False
        else:
            print("Screenshotting started !")
            notifier("Screenshotting started !")
            screenshotActive = True


def on_key_released(key):
    print("Key released : {0}".format(key))


def init():
    base_folder = config['BASE']['baseFolder']
    print(f"Base Folder : {base_folder}")
    notify_interval = int(config['BASE']['notifyInterval'])
    print(f"Notifications Interval : {notify_interval}")

    # go to the base folder and create if necessary a folder to store all the screenshots
    if os.path.exists(base_folder):
        print("The folder exists : OK")
    else:
        print("Folder creation")
        os.mkdir("capture-ecran")

    os.chdir(base_folder)
    folder_path = os.getcwd()

    # keyboard init for control
    listener = Listener(on_press=on_key_pressed, on_release=on_key_released)
    listener.start()

    return folder_path, notify_interval


def main(folder_name, interval):
    count_number_pictures = 0

    while True:

        # retrieve the current date of the day and create a folder for the day if necessary
        day_date = time.localtime()
        day_date = str(day_date.tm_year) + '-' + str(day_date.tm_mon) + '-' + str(day_date.tm_mday)

        name_day_date = os.path.join(folder_name, day_date)

        if os.path.exists(name_day_date):
            print("folder of the day already here !")
        else:
            os.mkdir(name_day_date)
            print("folder of the day created !")

        os.chdir(name_day_date)

        if screenshotActive:

            sct = mss()

            photo_date = time.localtime()
            nom = str(photo_date.tm_year) + '-' + str(photo_date.tm_mon) + '-' + str(
                photo_date.tm_mday) + '-' + str(
                photo_date.tm_hour) + '_' + str(photo_date.tm_min) + '-' + str(photo_date.tm_sec) + '.png'

            # screenshot that include all the displays that are currently in use
            sct.shot(mon=-1, output=nom)
            print("Screenshot taken !")
            print(f"Count : {count_number_pictures}")

            count_number_pictures = count_number_pictures + 1
            # display toast notification only once an hour
            if count_number_pictures > (interval * 2):
                notifier("Screenshot taken !")
                count_number_pictures = 0

        # wait for 30 sec before taking another pictures
        time.sleep(30)


if __name__ == "__main__":
    path_name, notify = init()
    main(path_name, notify)
