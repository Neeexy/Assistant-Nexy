'''Primeiros passos:
- Instalar a biblioteca SpeechRecognition e PyAudio (SR para reconhecer minhas palavras e PA (Versão correta para o meu sistema operacional) para interligar meu microfone com o programa)
Obs: Eu não sei se o essas bibliotecas vão ser compatíveis com o android mas de qualquer forma eu tenho que aprender a usar elas.
- 
'''
import speech_recognition as sr
from time import sleep

recognizer = sr.Recognizer() 

print(sr.Microphone.list_microphone_names())
'''with sr.Microphone(3) as microphone: # Usando o caixa como microfone kkkkk
    recognizer.adjust_for_ambient_noise(microphone)
    print('Pode falar')
    audio = recognizer.listen(microphone)
    text = recognizer.recognize_google(audio, language="pt-BR")
    print(text)'''