import time
import PIL
from PIL import ImageGrab
x=1
while True:
    image = PIL.ImageGrab.grab()
    image.save(str(time.localtime()) + '.png', 'png')
    x = x+1
    print(x)
    time.sleep(30)



