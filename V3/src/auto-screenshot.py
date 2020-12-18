import time
import os
from mss import mss
from pynput.keyboard import Listener, Key
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

marche = True;

def sur_appui(touche):
    print("Touche presse : {0}".format(touche))
    if touche is Key.pause:
        print("Appui pause !")
        global marche
        if  marche:
            print(marche)
            marche = False
        else:
            print(marche)
            marche = True



def sur_relache(touche):
    print("Touche relache : {0}".format(touche))



listener = Listener(on_press=sur_appui, on_release=sur_relache)
listener.start()

repertoireGeneral = config['BASE']['repertoireGeneral']
print(repertoireGeneral)

if os.path.exists(repertoireGeneral):
    print("Ok le dossier existe")
else:
    print("Création du dossier")
    os.mkdir("capture-ecran")

os.chdir(repertoireGeneral)
cheminRepertoire = os.getcwd()

while True:

    # Récupération de la date du jour (année, mois et numéro du jour)
    dateJour = time.localtime()
    nomJour = str(dateJour.tm_year) + '-' + str(dateJour.tm_mon) + '-' + str(dateJour.tm_mday)

    nomJourComplet =  os.path.join(cheminRepertoire,nomJour)

    if os.path.exists(nomJourComplet):
        print("Dossier du jour déjà existant")
    else:
        os.mkdir(nomJourComplet)
        print("Dossier du jour créé")

    os.chdir(nomJourComplet)

    if marche:
        sct = mss()

        datePhoto = time.localtime()
        nom = str(datePhoto.tm_year) + '-' + str(datePhoto.tm_mon) + '-' + str(datePhoto.tm_mday) + '-' + str(datePhoto.tm_hour) + '_' + str(datePhoto.tm_min) + '-' + str(datePhoto.tm_sec) + '.png'

        sct.shot(mon=-1,output=nom)

    time.sleep(30)