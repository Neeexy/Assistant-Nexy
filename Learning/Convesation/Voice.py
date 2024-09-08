# Trabalhando com a Voz do Nexy (respostas, confirmações e etcétera)

import speech_recognition as sr
import os
import subprocess
import psutil
import pyttsx3 as ts
from time import sleep

recoginizer = sr.Recognizer()

# Paths 

chrome_path = r'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
whatsapp_path = r'"C:\\Program Files\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"'
github_desktop_path = r'"C:\\Users\\Gabriel\AppData\\Local\\GitHubDesktop\\app-3.4.3\\GitHubDesktop.exe"'
spotify_path = r'"C:\\Users\\Gabriel\\AppData\\Roaming\\Spotify\\Spotify.exe"'

# URL's

url = "https://www.youtube.com/"
url_channel = "https://www.youtube.com/@Neeexy"


def open_program(path):
    subprocess.Popen(path, shell=True)

def close_program(program_name):
    try:
        subprocess.run(f'taskkill /IM {program_name} /F', shell=True)
        print(f'{program_name} encerrado com sucesso')
    except Exception as e:
        print(f'Erro ao encerrar {program_name}: {e}')

def open_url(url):
    chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    subprocess.Popen([chrome_path,'--new-tab', url], shell=True)


def verify_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

open = ['abrir','abre','abra'] # Palavras chave para abrir um programa
close = ['fechar','fecha','feche','encerre','encerrar'] # Palavras chave para fechar um programa

def check_words(word_list, message): # Função para verificar se uma palavra da lista está na mensagem
    return any(word in message for word in word_list)

Nexy = ts.init()

Nexy.say('Juliana deixe meu docinho em paz')
Nexy.runAndWait