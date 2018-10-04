import time
import PIL
from PIL import ImageGrab
import os
from unipath import Path

repertoire = "D:\OurDocuments\Alexandre\Documents\Programme\Test"

os.chdir(repertoire)

l = time.localtime()
year = l.tm_year
month = l.tm_mon
monday = l.tm_mday

jour = str(year)+'-'+str(month)+'-'+str(monday)

if Path.exists(jour):
    print("Dossier déjà existant")
else:
    os.mkdir(jour)
    print("Dossier créé")

dossier = repertoire + '\\' + jour
os.path.normpath(dossier)
os.chdir(dossier)


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
    
    print("Les captures d'écran sont lancées")
    time.sleep(30)