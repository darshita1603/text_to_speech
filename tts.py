from gtts import gTTS
from playsound import playsound
import tkinter as Tk
from tkinter import font
import os


m=Tk.Tk()
m.title("Text to Speech")
m.geometry("300x200")
language="en"

def start():
    text=enter.get()
    val=gTTS(text=text,lang=language,slow=False)
    val.save("myfiles.mp3")
    playsound("myfiles.mp3")
    os.remove("myfiles.mp3")

def reset():
    enter.set("")

def exit():
    m.destroy()


l1=Tk.Label(m,text="Enter Anything...!!!",font="Helvetica 15 bold")
l1.place(x=40,y=10)

enter=Tk.StringVar()
value_entry=Tk.Entry(m,width=40,highlightbackground="black",textvariable=enter)
value_entry.place(x=35,y=70)

b1=Tk.Button(m,text="Start",height=2,width=8,bd=2,bg="Green",fg="White",command=start)
b1.place(x=50,y=120)

b2=Tk.Button(m,text="Reset",height=2,width=8,bd=2,bg="blue",fg="White",command=reset)
b2.place(x=120,y=120)

b3=Tk.Button(m,text="Exit",height=2,width=8,bd=2,bg="Red",fg="White" ,command=exit)
b3.place(x=190,y=120)

m.mainloop()