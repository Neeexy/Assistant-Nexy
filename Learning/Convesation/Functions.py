import subprocess
import psutil

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

def check_words(word_list, message): # Função para verificar se uma palavra da lista está na mensagem
    return any(word in message for word in word_list)