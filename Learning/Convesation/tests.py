from Functions import * 
def speak(audio): #Função para a fala do nexy
    Nexy = ts.init('sapi5') # Configura o Nexy
    Nexy.say(audio)
    Nexy.runAndWait()
positive = [
    'sim', 'aceito', 'concordo', 'claro', 'certamente', 'positivo', 'afirmativo'
]

negative = [
    'não', 'recuso', 'discordo', 'negativo', 'nunca', 'jamais'
]
def getCommand(): # Receber comando por voz
    recoginizer = sr.Recognizer() # Reconhecedor de voz
    with sr.Microphone(1) as microphone:
        recoginizer.adjust_for_ambient_noise(microphone) # Ajusta o microfone para com o ruído ambiente
        # os.system('cls')
        # speak('Nexy Ouvindo, como posso lhe ajudar?')
        print('✅✅ Nexy pronto para ouvir! ✅✅\n')
        recoginizer.pause_threshold = 1
        audio = recoginizer.listen(microphone) #Ativa o listening do microfone

    try: # Caso tudo esteja funcionando corretamente, continua
        command = recoginizer.recognize_google(audio, language="pt-BR")
        command = command.replace('nexi','Nexy').replace('next','Nexy')
        command = command.lower()
        print(f'O usuário falou: {command}')
    except Exception as e:
        print(e)
        speak('Não entendi sua mensagem!')
        return ''
    return command
spotify_path = r'"C:\\Users\\Gabriel\\AppData\\Roaming\\Spotify\\Spotify.exe"'

command = getCommand()
if check_words(open,command) and 'spotify' in command:
        if verify_process('Spotify.exe'):
            speak('O spotify já está aberto. Você quer abrir da mesma forma, ou fechá-lo?') # Pergunta ao usuário (por voz) se ele quer abrir o programa, e a resposta tem que ser pelo microfone.
        
            affirm = getCommand()
            if check_words(positive, command) and 'Spotify' in affirm:
                speak('Abrindo Spotify')
                open_program(spotify_path)

            elif check_words(negative, command) and 'Spotify' in affirm:
                speak('Entendido')

            elif 'fechar' or 'encerrar' in affirm:
                speak('Fechando Spotify')
                close_program('Spotify.exe')

            else:
                speak('Não entendi sua menssagem, tente novamente!')

        else:
            speak('Abrindo Spotify')
            open_program(spotify_path)