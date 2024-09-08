import speech_recognition as sr
import os
import subprocess
import psutil
import pyttsx3 as ts
from time import sleep
import keyboard



def speak(audio): #Função para a fala do nexy
    Nexy = ts.init('sapi5') # Configura o Nexy
    Nexy.say(audio)
    Nexy.runAndWait()

def getCommand(): # Receber comando por voz
    recoginizer = sr.Recognizer() # Reconhecedor de voz
    with sr.Microphone(1) as microphone:
        recoginizer.adjust_for_ambient_noise(microphone) # Ajusta o microfone para com o ruído ambiente
        # os.system('cls')
        # speak('Nexy Ouvindo, como posso lhe ajudar?')
        print('✅✅ Nexy pronto para ouvir! ✅✅\n')
        recoginizer.pause_threshold = 0.5
        audio = recoginizer.listen(microphone) #Ativa o listening do microfone

    try: # Caso tudo esteja funcionando corretamente, continua
        command = recoginizer.recognize_google(audio, language="pt-BR")
        command = command.replace('nexi','Nexy').replace('next','Nexy').replace('alex','Nexy')
        command = command.lower()
        print(f'O usuário falou: {command}')
    except Exception as e:
        print(e)
        speak('Não entendi sua mensagem!')
        return ''
    return command


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
    subprocess.Popen([chrome_path, url], shell=True)


def verify_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

open = ['abrir','abre','abra'] # Palavras chave para abrir um programa
close = ['fechar','fecha','feche','encerre','encerrar'] # Palavras chave para fechar um programa

def check_words(word_list, command): # Função para verificar se uma palavra da lista está na mensagem
    return any(word in command for word in word_list)

