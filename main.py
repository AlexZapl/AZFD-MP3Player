from tkinter import *
from pygame import mixer

from tkinter import messagebox as mb
from tkinter import filedialog as fd
import time

from PIL import ImageTk, Image

lmode15 = "gray15"
lmode12 = "gray12"
lmode25 = "gray25"
textcol = "white"
light_mode = 0

# bgimgpath = 'mp3bg.png'

mixer.init()
root = Tk()


# image2 = Image.open(bgimgpath)
# image1 = ImageTk.PhotoImage(image2)

def lightModeClick():
    global light_mode, lmode15, lmode12, lmode25, textcol
    if light_mode == 1:
        light_mode = 0
        lmode15 = "gray15"
        lmode12 = "gray12"
        lmode25 = "gray25"
        textcol = "white"
        print(light_mode)
    else:
        light_mode = 1
        lmode15 = "white"
        lmode12 = "white"
        lmode25 = "white"
        textcol = "black"
        print(light_mode)
    time.sleep(0.25)


# lightModeClick()
master_frame = Frame(root, background=lmode25)
master_frame.pack()
root.title("AZFD MP3")


def openfile():
    song = fd.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    song_box.insert(END, song)


def openfiles():
    song = fd.askopenfilenames(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    for file in range(len(song)):
        song_box.insert(END, song[file])


def pause():
    mixer.music.pause()


def play():
    if song_state['text'] == "Воспроизведение":
        mixer.music.unpause()
    else:
        song_box.selection_set(0, last=None)
        song = song_box.get(ACTIVE)
        mixer.music.load(song)
        mixer.music.play()
        song_state['text'] = "Воспроизведение"


def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = "Остановлено"


def prev_song():
    next_s = song_box.curselection()
    next_s = next_s[0] - 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)


def next_song():
    next_s = song_box.curselection()
    next_s = next_s[0] + 1
    song = song_box.get(next_s)
    mixer.music.load(song)
    mixer.music.play()
    song_box.selection_clear(0, END)
    song_box.activate(next_s)
    song_box.selection_set(next_s, last=None)


info_frame = Frame(master_frame, background=lmode25)
info_frame.grid(row=0, column=0)

song_state = Label(info_frame, width=60, text="Остановлено", font="Arial 8 bold", background=lmode25, fg=textcol)
song_state.grid(row=0, column=0)

song_box = Listbox(info_frame, width=60, selectbackground="blue", background=lmode15, fg=textcol)
song_box.grid(row=1, column=0)

controls_frame = Frame(master_frame, background=lmode12)
controls_frame.grid(row=1, column=0)

back_button = Button(controls_frame, text="<", width=5, command=prev_song, background=lmode12, font='Times 8',
                     fg=textcol)
forward_button = Button(controls_frame, text=">", width=5, command=next_song, background=lmode12, font='Times 8',
                        fg=textcol)
play_button = Button(controls_frame, text="▶", width=5, command=play, background=lmode12, font='Times 8', fg=textcol)
pause_button = Button(controls_frame, text="||", width=5, command=pause, background=lmode12, font='Times 8', fg=textcol)
stop_button = Button(controls_frame, text="Stop", width=5, command=stop, background=lmode12, font='Times 8', fg=textcol)
lmodetext = ''
if light_mode == 1:
    lmodetext = "Тёмный режим"
else:
    lmodetext = "Светлый режим"
buttonLightMode = Button(controls_frame, text=lmodetext, command=lightModeClick, background=lmode12, fg=textcol,
                         font='Times 8')
back_button.grid(row=0, column=0)
forward_button.grid(row=0, column=1)
play_button.grid(row=0, column=2)
pause_button.grid(row=0, column=3)
stop_button.grid(row=0, column=4)
buttonLightMode.grid(row=0, column=5)

file_frame = Frame(master_frame, background=lmode25)
file_frame.grid(row=0, column=5)

openfile_button = Button(file_frame, text="Открыть трек", width=12, command=openfile, background=lmode12,
                         font='Times 8', fg=textcol)
openfolder_button = Button(file_frame, text="Oткрыть несколько треков", width=22, command=openfiles, background=lmode12,
                           font='Times 8', fg=textcol)

openfile_button.grid()
openfolder_button.grid()

root.mainloop()
