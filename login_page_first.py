from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import os
from home import run_home

t=tk.Tk()
t.title('OS')
t.configure(background = 'grey')
w, h = t.winfo_screenwidth(), t.winfo_screenheight()
t.geometry("600x400+400+200")
t.minsize(600,400)
t.maxsize(1250, 700) 

def enter():
	if uid.get()=='root' and pswd.get()=='root':
		tkinter.messagebox.showinfo('Success','Logged_In')
		t.destroy()
		run_home('root')
		
	elif uid.get()=='user' and pswd.get()=='user':
		tkinter.messagebox.showinfo('Success','Logged_In')
		t.destroy()
		run_home('user')

	else:
		tkinter.messagebox.showinfo('Alert','Incorrect User ID or Password')

	return

msg = Label(t, text='LOGIN', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
user = Label(t, text='User ID', font=tkFont.Font(family="Times New Roman", size=30),borderwidth=2, relief="solid")
password = Label(t, text='Password', font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
uid = Entry(t,font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
pswd = Entry(t,show='*',font=tkFont.Font(family="Times New Roman", size=30), borderwidth=2, relief="solid")
submit = Button(t, text='Submit', font=tkFont.Font(family="Times New Roman", size=30), command=enter, borderwidth=2, relief="solid")

msg.place(x = 100, y = 20 , width=400, height=60)
user.place(x = 100, y = 120 , width=180, height=60)
password.place(x = 100, y = 220 , width=180, height=60)
uid.place(x = 320, y = 120 , width=180, height=60)
pswd.place(x = 320, y = 220 , width=180, height=60)
submit.place(x = 100, y = 320 , width=400, height=60)

def shut():
	sys.exit()

t.load = Image.open('power.png')
t.load = t.load.resize((70,70), Image.ANTIALIAS)
t.photo = ImageTk.PhotoImage(t.load,master=t)
t.img = Button(t, image=t.photo, command=shut)
t.img.image = t.photo
t.img.place(x=530, y=320, width=60, height=60)	

mainloop()
