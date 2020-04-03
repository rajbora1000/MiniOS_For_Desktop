from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import sys
import os

def run_file():
	t=tk.Tk()
	t.title('Partitions Management')
	t.configure(background = 'grey')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("400x400")
	t.minsize(400,400)
	t.maxsize(500,500)

	def create_dir():
		try:
			if e1.get()!='':
				mode = 0o777
				os.mkdir(e1.get(),mode)
				tkinter.messagebox.showinfo('Success','Partition Created')
			else:
				tkinter.messagebox.showinfo('Alert','Enter Partition Name')
		except FileExistsError:
			tkinter.messagebox.showinfo('Alert','Cannot create a partition when a partition with that name already exists: '+e1.get())
		finally:
			e1.delete(0,'end')
		
	def rem_dir():
			try:
				if e2.get()!='':
					os.rmdir(e2.get())
					tkinter.messagebox.showinfo('Success','Partition Removed')
				else:
					tkinter.messagebox.showinfo('Alert','Enter Partition Name')
			except OSError:
				tkinter.messagebox.showinfo('Alert','No such Partition exists: '+e1.get())
			finally:
				e2.delete(0,'end')

	t.load1 = Image.open('create.png')
	t.load1 = t.load1.resize((80,80), Image.ANTIALIAS)
	t.photo1 = ImageTk.PhotoImage(t.load1,master=t)
	t.img1 = Button(t, image=t.photo1)
	t.img1.image = t.photo1
	t.img1.place(x=60, y=70, width=80, height=80)

	e1=Entry(t)
	e1.place(x=20, y=160, width=160, height=40)

	b1=Button(t, text='Create Partition', command=create_dir)
	b1.place(x=20, y=210, width=160, height=40)



	t.load2 = Image.open('delete.png')
	t.load2 = t.load2.resize((80,80), Image.ANTIALIAS)
	t.photo2 = ImageTk.PhotoImage(t.load2,master=t)
	t.img2 = Button(t, image=t.photo2)
	t.img2.image = t.photo2
	t.img2.place(x=260, y=70, width=80, height=80)

	e2=Entry(t)
	e2.place(x=220, y=160, width=160, height=40)

	b2=Button(t, text='Remove Partition',command=rem_dir)
	b2.place(x=220, y=210, width=160, height=40)

	t.mainloop()
