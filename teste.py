import subprocess
import psutil
from time import sleep

url = "https://www.youtube.com/"
url_canal = "https://www.youtube.com/@Neeexy"
whatsapp_path = r'"C:\\Program Files\WindowsApps\\5319275A.WhatsAppDesktop_2.2435.4.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"'
chrome_path = r'"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"'


def open_program(path):
    subprocess.Popen(path, shell=True)

open_program(whatsapp_path)

def verify_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

sleep(3)

if verify_process('WhatsApp.exe'):
    print('zap aberto')
else:
    print('não')