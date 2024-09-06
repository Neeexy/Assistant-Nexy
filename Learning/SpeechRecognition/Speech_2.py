# A meta agora é fazer com que a comunicação seja recíproca. 
# A primeiro momento, apenas idententificar elementos nas mensagens

import speech_recognition as sr
import os
from time import sleep

recoginizer = sr.Recognizer()

# Paths 

chrome_path = r'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'
url = "https://www.youtube.com/"
url_channel = "https://www.youtube.com/@Neeexy"
url_spotify = "https://open.spotify.com/intl-pt"
whatsapp_path = r'"C:\\Program Files\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"'

with sr.Microphone(1) as microphone:
    recoginizer.adjust_for_ambient_noise(microphone)
    os.system('cls')
    print('✅✅ Nexy pronto para ouvir! ✅✅')
    audio = recoginizer.listen(microphone)
    message = recoginizer.recognize_google(audio, language="pt-BR")
    message = message.replace('nexi','Nexy').replace('next','Nexy')
    print(message)

    message = message.lower()
    
    # Compliments

    if 'boa noite' in message:
        print('\nBoa noite!!')
    elif 'boa tarde' in message:
        print('\nBoa tarde!!')
    elif 'bom dia' in message:
        print('\nBom dia!!')
    
    # Commands

    if 'limpar' and 'terminal' in message:
        os.system('cls')
        print('Terminal limpo')
        sleep(2)
        os.system('cls')

    if 'google' in message:
        print('Abrindo o Google')
        sleep(1)
        os.system(f'{chrome_path}')
    
    if 'spotify' in message:
        print('Abrindo o Spotify')
        sleep(1)
        os.system(f'{chrome_path} {url_spotify}')
    
    if 'meu' and 'canal' and 'youtube' in message:
        print('Abrindo seu canal!')
        os.system(f'{chrome_path} {url_channel}')

    if 'whatsapp' in message:
        print('Abrindo Whatsapp')
        os.system(f'{whatsapp_path}')