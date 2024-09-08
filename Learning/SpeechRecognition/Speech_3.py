# Apenas uma versão melhorada do 'Speech_2' implementando um sistema de verificação (espero que eu consiga)

# A meta agora é fazer com que a comunicação seja recíproca. 
# A primeiro momento, apenas idententificar elementos nas mensagens

import speech_recognition as sr
import os
import subprocess
import psutil
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

# A ideia é vincular uma I.A com o Nexy para que ele identifique o que fazer por sí só, mas por enquanto eu quero aprender o manual

with sr.Microphone(1) as microphone:
    recoginizer.adjust_for_ambient_noise(microphone)
    os.system('cls')
    print('✅✅ Nexy pronto para ouvir! ✅✅\n')
    audio = recoginizer.listen(microphone)
    message = recoginizer.recognize_google(audio, language="pt-BR")
    message = message.replace('nexi','Nexy').replace('next','Nexy')
    print(message)

    message = message.lower()
    
    # Compliments

    if 'boa noite' in message:
        print('\nBoa noite!!')
    if 'boa tarde' in message:
        print('\nBoa tarde!!')
    if 'bom dia' in message:
        print('\nBom dia!!')
    
    # Commands


    if 'limpar' and 'terminal' in message:
        os.system('cls')
        print('Terminal limpo')
        sleep(2)
        os.system('cls')

    if check_words(open,message) and 'whatsapp' in message: # Abrir o WhatsApp
        if verify_process('WhatsApp.exe'):
            print('O WhatsApp já está aberto')
        else:
            print('Abrindo o WhatsApp')
            open_program(whatsapp_path)

    elif check_words(close,message) and 'whatsapp' in message: #Fechar o Wwhastapp
        if verify_process('WhatsApp.exe'):
            close_program('WhatsApp.exe')
        else:
            print('O WhatsApp não está aberto.')

    if check_words(open,message) and 'github' in message: # Abrir o GitHub-Desktop
        if verify_process('GitHubDesktop.exe'):
            print('O GitHub Desktop já está aberto')
        else:
            print('Abrindo o GitHub Desktop')
            open_program(github_desktop_path)

    elif check_words(close, message) and 'github' in message: # Fechar o GitHub
        if verify_process('GitHubDesktop.exe'):
            close_program('GitHubDesktop.exe')
        else:
            print('O GitHub Desktop não está aberto.')

    if check_words(open,message) and 'spotify' in message: # Abrir o Spotify
        if verify_process('Spotify.exe'):
            print('O Spotify já está aberto')
        else:
            print('Abrindo o Spotify')
            open_program(spotify_path)

    if check_words(open,message) and 'google' in message: # Abrir o Google
        if verify_process('chrome.exe'):
            print('O Google Chrome já está aberto.')
        else:
            print('Abrindo o Google')
            open_program(chrome_path)

    elif check_words(close, message) and 'google' in message: # Fechar o Google
        if verify_process('chrome.exe'):
            close_program('chrome.exe')
        else:
            print('O Google Chrome não está aberto.')

    if  'youtube' in message:
        print('Abrindo seu canal!')
        open_url("https://www.youtube.com/")
    
    if 'desligar a máquina' in message:
        os.system("shutdown /s /f /t 0")



#  Objetivo atingido

# Ideia para o proximo passo (Reciprocidade), quando um aplicativo já estiver aberto, perguntar se o usuário quer fecha-lo