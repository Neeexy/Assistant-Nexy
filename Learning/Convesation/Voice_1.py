# Trabalhando com a Voz do Nexy (respostas, confirmações e etcétera)
from Functions import *
import wikipedia
import webbrowser

wikipedia.set_lang('pt')
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
positive = ['sim', 'aceito', 'concordo', 'claro', 'certamente', 'positivo', 'afirmativo']
negative = ['não', 'recuso', 'discordo', 'negativo', 'nunca', 'jamais','nada']


while True:
    speak('Nexy Ouvindo...')
    command = getCommand()

    if 'Olá Nexy' in command:
        speak('Olá')
        # programas

    # Spotify
    elif check_words(open, command) and 'spotify' in command: # Abrir Spotify
        if verify_process('Spotify.exe'):
            speak('O Spotify já está aberto. Você quer abrir da mesma forma, ou fechá-lo?')

            affirm = getCommand()

            if check_words(positive, affirm):  # Verifica palavras positivas na resposta do usuário
                speak('Abrindo Spotify')
                open_program(spotify_path)
            elif check_words(negative, affirm):  # Verifica palavras negativas na resposta do usuário
                speak('Entendido')
            elif 'fechar' in affirm or 'encerrar' in affirm:
                speak('Fechando Spotify')
                close_program('Spotify.exe')
            else:
                speak('Não entendi sua mensagem, tente novamente!')

        else:
            speak('Abrindo Spotify')
            open_program(spotify_path)
    
    elif check_words(close, command) and 'spotify' in command: # Fechar o Spotify

        if verify_process('Spotify.exe'):
            speak('Fechando o Spotify')
            close_program('Spotify.exe')

        else:
            speak('O Spotify não está aberto.')

    # Chrome
    elif check_words(open, command) and 'navegador' in command: # Abrir chrome
        if verify_process('chrome.exe'):
            speak('O chrome já está aberto. Você quer abrir da mesma forma, ou fechá-lo?')

            affirm = getCommand()

            if check_words(positive, affirm):  # Verifica palavras positivas na resposta do usuário
                speak('Abrindo Navegador Google Chrome')
                open_program(chrome_path)
            elif check_words(negative, affirm):  # Verifica palavras negativas na resposta do usuário
                speak('Entendido')
            elif 'fechar' in affirm or 'encerrar' in affirm:
                speak('Fechando Navegador Google Chrome')
                close_program('chrome.exe')
            else:
                speak('Não entendi sua mensagem, tente novamente!')

        else:
            speak('Abrindo Navegador Google Chrome')
            open_program(chrome_path)
    
    elif check_words(close, command) and 'navegador' in command: # Fechar o chrome

        if verify_process('chrome.exe'):
            speak('Fechando o Navegador Google Chrome')
            close_program('chrome.exe')

        else:
            speak('O Navegador Google Chrome não está aberto.')
    
    #WhatsApp
    elif check_words(open, command) and 'whatsapp' in command: # Abrir WhatsApp
        if verify_process('WhatsApp.exe'):
            speak('O WhatsApp já está aberto. Você quer abrir da mesma forma, ou fechá-lo?')

            affirm = getCommand()

            if check_words(positive, affirm):  # Verifica palavras positivas na resposta do usuário
                speak('Abrindo WhatsApp')
                open_program(whatsapp_path)
            elif check_words(negative, affirm):  # Verifica palavras negativas na resposta do usuário
                speak('Entendido')
            elif 'fechar' in affirm or 'encerrar' in affirm:
                speak('Fechando WhatsApp')
                close_program('WhatsApp.exe')
            else:
                speak('Não entendi sua mensagem, tente novamente!')

        else:
            speak('Abrindo WhatsApp')
            open_program(whatsapp_path)
    
    elif check_words(close, command) and 'whatsapp' in command: # Fechar o WhatsApp

        if verify_process('WhatsApp.exe'):
            speak('Fechando o WhatsApp')
            close_program('WhatsApp.exe')

        else:
            speak('O WhatsApp não está aberto.')
    
    #GitHub
    elif check_words(open, command) and 'github' in command: # Abrir GitHubDesktop
        if verify_process('GitHubDesktop.exe'):
            speak('O GitHubDesktop já está aberto. Você quer abrir da mesma forma, ou fechá-lo?')

            affirm = getCommand()

            if check_words(positive, affirm):  # Verifica palavras positivas na resposta do usuário
                speak('Abrindo GitHubDesktop')
                open_program(github_desktop_path)
            elif check_words(negative, affirm):  # Verifica palavras negativas na resposta do usuário
                speak('Entendido')
            elif 'fechar' in affirm or 'encerrar' in affirm:
                speak('Fechando GitHubDesktop')
                close_program('GitHubDesktop.exe')
            else:
                speak('Não entendi sua mensagem, tente novamente!')

        else:
            speak('Abrindo GitHubDesktop')
            open_program(github_desktop_path)
    
    elif check_words(close, command) and 'github' in command: # Fechar o GitHubDesktop

        if verify_process('GitHubDesktop.exe'):
            speak('Fechando o GitHubDesktop')
            close_program('GitHubDesktop.exe')

        else:
            speak('O GitHubDesktop não está aberto.')
    
        # Pages
    #Youtube
    elif check_words(open, command) and 'youtube' in command:
        speak('Abrindo uma guia para o youtube!')
        open_url("https://www.youtube.com/")


    # System Commands
    elif 'desligar a máquina' in command: # Desligar Pc
        speak('Desligando a máquina mais poderosa de todas as galáxias já existentes e que ainda vão cogitar existir.')
        os.system("shutdown /s /f /t 0")
    
    elif 'avançar música' in command or 'próxima música' in command or 'pular música' in command: #Avançar música
        speak('Avançando para a próxima música')
        keyboard.send("next track")

    elif 'voltar música' in command or 'música anterior' in command: #Retroceder Música
        speak('Voltando para a música anterior')
        keyboard.send("previous track")

    elif 'pausar música' in command: #Pausar música
        keyboard.send("play/pause media")
        speak('Música pausada')

    elif 'retomar música' in command or 'continuar música' in command: #Retomar música
        speak('Retomando Música')
        keyboard.send("play/pause media")


    # Leave
    elif 'obrigado' in command or 'tchau' in command or 'até logo' in command:
        speak('Até logo.')
        os.system('cls')
        break

    