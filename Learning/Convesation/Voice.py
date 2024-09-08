# Trabalhando com a Voz do Nexy (respostas, confirmações e etcétera)

import speech_recognition as sr
import os
import subprocess
import psutil
import pyttsx3 as ts
from time import sleep
from Functions import *

# Paths 
chrome_path = r'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
whatsapp_path = r'"C:\\Program Files\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"'
github_desktop_path = r'"C:\\Users\\Gabriel\AppData\\Local\\GitHubDesktop\\app-3.4.3\\GitHubDesktop.exe"'
spotify_path = r'"C:\\Users\\Gabriel\\AppData\\Roaming\\Spotify\\Spotify.exe"'

# URL's
url_channel = "https://www.youtube.com/@Neeexy"

# Palavras Chave
open = ['abrir','abre','abra'] # Palavras chave para abrir um programa
close = ['fechar','fecha','feche','encerre','encerrar'] # Palavras chave para fechar um programa

recoginizer = sr.Recognizer() # Reconhecedor de voz


Nexy = ts.init("sapi5") 

voices = Nexy.getProperty('voices')

for voice in voices:
    print(f"ID: {voice.id}")
    print(f"Nome: {voice.name}")
    print(f"Idiomas: {voice.languages}")
    print(f"Gênero: {voice.gender}")
    print(f"Idade: {voice.age}")
    print("-" * 20) 

# Nexy.say('Olá')
# Nexy.runAndWait()
