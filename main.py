import random
import time
import pygame
from tkinter import Tk, Button, DISABLED
from tkinter import Label

#inisialisasi pygame
pygame.init()

#memuat file musik
pygame.mixer.music.load ('beksond.mp3')

#memutar musik loop
pygame.mixer.music.play(-1)

#tombol ditekan
button_sound = pygame.mixer.Sound ('sfxclick.mp3')


#membuat fungsi untuk menampilkan simbol pada tombol 
def show_symbol(x,y):
    global first
    global previousx, previousy
    buttons[x,y]['text'] = button_symbols[x,y]
    buttons[x,y].update_idletasks()
    button_sound.play()
    

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy !=y:
        if buttons[previousx, previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text']= ''
            buttons[x,y]['text'] = ''
        else:
            buttons[previousx, previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

#membuat tampilan window dengan tkinter
win = Tk()
win.title('Game cocok cocok-in biar jodoh')
win.resizable(width=False,height=False)

#menambahkan  label "ayo bermain" pada window
win_label = Label(win, text="Semoga kamu berhasil ya! - @anggorostyn")
win_label.grid(row=6, columnspan=6)

#inisialisasi
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
           u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
           u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
           u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']


random.shuffle(symbols)

#membuat tombol-tombol permainan
for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x, y=y: show_symbol(x,y),width=10,height=8)
        button.grid(column=x,row=y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

#memulai loop 
win.mainloop()

#aplikasi ditutup, musik berhenti
win.protocol("WM_DELETE_WINDOW", pygame.quit)