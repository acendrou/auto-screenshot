import time
import PIL
from PIL import ImageGrab

x = 1
while True:
    image = PIL.ImageGrab.grab()
    t = time.localtime()
    year = t.tm_year
    month = t.tm_mon
    monday = t.tm_mday
    hour = t.tm_hour
    minute = t.tm_min
    second = t.tm_sec

    image.save(str(year) + '-' + str(month) + '-' + str(monday) + '-' + str(hour) + '_' + str(minute) + '-' + str(
        second) + '.png', 'png')
    x = x + 1
    print(x)
    time.sleep(30)
