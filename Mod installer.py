from threading import Thread
from playsound import playsound
from zipfile import ZipFile
from tqdm import tqdm
from os import path
import requests
import zipfile
import shutil
import time
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

## Starten? \/
time.sleep(1.5)
delay_print("Möchtest du die Installation der mods starten. Dabei werden alle alten mods gelöscht (buschstabe+ENTER) \n")
time.sleep(0.5)
while input("[j/n]") == "j":
    delay_print("Starte Prozess\n")
    break
## Starten? /\


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)

## localosiere minecraft mods ordner \/
delay_print("Suche minecraft Pfad \n")

delay_print(os.getcwd())
delay_print("\n")
path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
delay_print(os.getcwd())
delay_print("\n")
os.chdir('AppData\Roaming\.minecraft')
delay_print(os.getcwd())
delay_print("\n")


## Lösche mods ordner \/
shutil.rmtree('mods')
delay_print ("alte mods gelöscht")
## Lösche mods ordner /\

time.sleep(0.5)
delay_print("\n")


## Erstelle mods ordner \/
os.mkdir('mods')
delay_print ("mods Ordner wurde ersstellt")
delay_print("\n")
## Erstelle mods ordner /\

os.chdir('mods')
delay_print(os.getcwd())
delay_print("\n")
## localosiere minecraft mods ordner /\


time.sleep(3)
os.system('cls')

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

chunk_size = 1024

## musik link direct \/
def func1():
    playsound('https://***.mp3')
## musik link direct /\

def func2():
    time.sleep(1.5)
    delay_print("Vielen dank für die verwendung des Installers >_<\nMöchtest du fortfahren dann gebe Ja(j) oder Nein(n) ein.\n")
    time.sleep(0.5)
    while input("[j/n]") == "j":
        delay_print("Download Startet\n")
    
    

## Direkter Download link
        url = "https://***/mods.zip"
## Direkter Download link

        req = requests.get(url, stream = True)
        total_size = int(req.headers['content-length'])
        with open("mods.zip", "wb") as file:
           for data in tqdm(iterable=req.iter_content(chunk_size=chunk_size), total = total_size/chunk_size, unit='KB'):
              file.write(data)
        delay_print("Download Abgeschlossen\nExtraktion läuft\n")
        my_zipfile = zipfile.ZipFile("mods.zip", mode='r')
        delay_print("Extrahiere alle dateien\n")
        my_zipfile.extractall()
       # delay_print("Abgeschlossen\n")


## stop
        wait = input("Du kannst das Terminal jetzt schließen alle mods wurden erfolgreich installiert.")
        exit()

        
        


if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()

time.sleep(3) # Sleep for 3 seconds