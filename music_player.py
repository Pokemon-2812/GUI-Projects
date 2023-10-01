from tkinter import *
from tkinter.filedialog import askopenfile
from pygame import mixer
import json
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter.messagebox import showerror
root=tb.Window(themename="darkly")
root.geometry("550x400")
root.title("Music Player")
style=tb.Style()
file=None
mixer.init()
lbxVar=StringVar()
values=[]
def add():
    global file
    file = askopenfile(defaultextension='.wav', filetypes =[('Wav Files', '*.wav'),("Mp3 Files",'*.mp3'),("Mp4 Files",'*.mp4'),("All Files","*.*")])
    if file=="":
        file=None
    if file!=None:
        if not(file.name in songs):
            song_name=file.name.split("/")[len(file.name.split("/"))-1]
            values.append(song_name)
            lbx['values']=values
            songs.append(file.name)
            short_songs[song_name]=file.name
            lbxVar.set(song_name)
def play():
    global file
    if lbxVar.get()!=None:
        try:
            file=short_songs[lbxVar.get()]
        except Exception as e:
            showerror("Error","No such file!")
            file=None
    if file!=None:
        try:
            mixer.music.load(file)
            root.title("Music Player - "+ file)
            mixer.music.play()
        except Exception as e:
            pass
def delete():
    try:
        songs.remove(short_songs[lbxVar.get()])
        lbx['values']=values
    except Exception as e:
        print(e)
    else:
        save()
def save():
    with open('songs.json','w') as f:
        json.dump(songs,f)
try:
    with open('songs.json','r') as f:
        songs=json.load(f)
except Exception as e:
    songs=[]
tb.Label(root,text="Music Playlist",font="arial 18",bootstyle="light").pack(pady=10,padx=5)
# scrollbar=Scrollbar(root)
# scrollbar.pack(fill=Y,side=RIGHT)
lbx=tb.Combobox(root,textvariable=lbxVar)
lbx.pack(fill=X)
# scrollbar.config(command=lbx.yview)
short_songs={}
for song in songs:
    if "/" in song:
        song_name=song.split("/")[len(song.split("/"))-1]
    else:
        song_name=song
    short_songs[song_name]=song
    values.append(song_name)
    lbx['values']=values
if(len(values)>0):
    lbxVar.set(values[0])
btn1=tb.Button(root,text="Add",bootstyle="primary",command=add)
btn1.pack(side=LEFT,padx=5,pady=5)
btn2=tb.Button(root,text="Delete",bootstyle="danger",command=delete)
btn2.pack(side=LEFT,padx=5,pady=5)
btn3=tb.Button(root,text="Save",bootstyle="success",command=save)
btn3.pack(side=LEFT,padx=5,pady=5)
btn4=tb.Button(root,text="Play",bootstyle="info",command=play)
btn4.pack(side=LEFT,padx=5,pady=5)
style.configure('TButton',font="arial 12",width=9)
root.mainloop()