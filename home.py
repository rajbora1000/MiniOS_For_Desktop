from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
from PIL import Image,ImageTk
import sys
import time
from datetime import date
from PIL import Image,ImageTk
import os
import math
import datetime

print('Used/Total : 0 B / 100 B')
time1 = ''
semaphore=0
logged=''

def run_home(user):

	print('Main Memory Available')
	print(semaphore)

	t=tk.Tk()
	t.title('HOME')
	t.configure(background = 'grey')
	w, h = t.winfo_screenwidth(), t.winfo_screenheight()
	t.geometry("1200x550+150+150")
	t.minsize(1000,550)
	t.resizable(0, 0)

	z=user+'.txt'

	try:
		file = open(z,"r") 
		tkinter.messagebox.showinfo('Log',file.read())
		file.close()
	except:
		tkinter.messagebox.showinfo('Log','No Log Data Found')
	try:
		os.remove(z)
	except:
		pass


	global logged
	logged=logged+str(datetime.datetime.now())+' Logged in : '+user+'\n'
	print(logged)

	mem=Label(t, text='Used/Total : 0 B / 100 B',bg='grey',font=('times', 10, 'bold'))
	mem.place(x=0,y=0,width=200,height=30)

	if 1==1:
		t.maxsize(1000, 600)
		def tick():
		    global time1
		    time2 = time.strftime('%H:%M:%S')
		    if time2 != time1:
		        time1 = time2
		        clock.config(text=time2)
		    clock.after(200, tick)
		
		clock = Label(t, font=('times', 20, 'bold'), bg='grey')
		clock.place(x=750, y=0, width=150, height=50)
		date1=Label(t,text=date.today(), font=('times', 20, 'bold'), bg='grey')
		date1.place(x=600, y=0, width=150, height=50)
		tick()

		def image_update():
			return

		def run_notepad():
			global semaphore
			if semaphore==1:
				print('Wait : Not Enough Space Available')
			if semaphore==0:
				global logged
				logged=logged+str(datetime.datetime.now())+' Notepad\n'
				print(logged)
				semaphore=1
				print('Accessing Main Memory')
				print(semaphore)
				used=70
				print('Used/Total : 70 B / 100 B')
				mem.config(text='Used/Total : 70 B /100 B')
				print()
				def run():
					root=Tk()
					ta=Text(root)
					mb=Menu(root)
					nfile=Menu(mb)
					edit=Menu(mb)
					sb=Scrollbar(ta)
					mfile=None
					root.title('Untitled - Notepad')
					left=(root.winfo_screenwidth()/2)-(300/2)
					top=(root.winfo_screenheight()/2)-(300/2) 
					root.geometry('%dx%d+%d+%d'%(300,300,left,top)) 
					def quitApplication(): 
						global semaphore
						semaphore=0
						print('Exiting Main Memory')
						print(semaphore)
						print('Used/Total : 0 B / 100 B')
						mem.config(text='Used/Total : 0 B /100 B')
						root.destroy()
						return
					def openFile(): 
						global mfile
						mfile = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")]) 
						if mfile == "": 
							mfile = None
						else: 
							# Try to open the file 
							# set the window title 
							root.title(os.path.basename(mfile) + " - Notepad") 
							ta.delete(1.0,END)
							file=open(mfile,"r")
							ta.insert(1.0,file.read())
							file.close()
					def newFile(): 
						global mfile
						root.title("Untitled - Notepad") 
						mfile = None
						ta.delete(1.0,END) 
					def saveFile(): 
						global mfile
						if mfile == None: 
							# Save as new file 
							mfile = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")]) 
							if mfile == "": 
								mfile = None
							else: 
								file = open(mfile,"w") 
								file.write(ta.get(1.0,END)) 
								file.close()
								root.title(os.path.basename(mfile) + " - Notepad") 
						else: 
							file = open(mfile,"w") 
							file.write(ta.get(1.0,END)) 
							file.close() 
					def cut(): 
						ta.event_generate("<<Cut>>") 
					def copy(): 
						ta.event_generate("<<Copy>>") 
					def paste(): 
						ta.event_generate("<<Paste>>") 

					root.grid_rowconfigure(0, weight=1)
					root.grid_columnconfigure(0, weight=1)
					ta.grid(sticky = N + E + S + W) 
					nfile.add_command(label="New",command=newFile)
					nfile.add_command(label="Open",command=openFile)
					nfile.add_command(label="Save",command=saveFile)
					nfile.add_separator()										 
					nfile.add_command(label="Exit",command=quitApplication) 
					mb.add_cascade(label="File",menu=nfile)	 
					edit.add_command(label="Cut",command=cut)
					edit.add_command(label="Copy",command=copy)
					edit.add_command(label="Paste",command=paste)
					mb.add_cascade(label="Edit",menu=edit)	 
					root.config(menu=mb) 
					sb.pack(side=RIGHT,fill=Y)				 
					sb.config(command=ta.yview)	 
					ta.config(yscrollcommand=sb.set) 

					mainloop()
				run()
				print(semaphore)


		t.load = Image.open('Notepadicon.png')
		t.load = t.load.resize((70,70), Image.ANTIALIAS)
		t.photo = ImageTk.PhotoImage(t.load,master=t)
		t.img = Button(t, image=t.photo,command=run_notepad)
		t.img.image = t.photo
		t.img.place(x=10, y=60, width=70, height=70)

		def run_calc():
			global semaphore
			if semaphore==1:
				print('Wait : Not Enough Space Available')
			else:
				print('Accessing Main Memory')
				semaphore=1
				print(semaphore)
				print('Used/Total : 60 B / 100 B')
				mem.config(text='Used/Total : 60 B /100 B')
				global logged
				logged=logged+str(datetime.datetime.now())+' Calculator\n'
				print(logged)
				def run():
					root = Tk()
					root.title('Calulator') 
					left=(root.winfo_screenwidth()/2)-(300/2)
					top=(root.winfo_screenheight()/2)-(300/2) 
					root.geometry('%dx%d+%d+%d'%(290,300,left,top))
					e = Entry( root) 
					e.grid(row=0,column=0,columnspan=6,pady=3) 
					e.focus_set() 

					def getandreplace(): 
						expression = e.get() 
						newtext=expression.replace('/','/') 
						newtext=newtext.replace('x','*') 

					def equals(): 
						"""when equal is pressed"""
						getandreplace() 
						try: 
							# evaluate the expression using the eval function 
							value= eval(newtext) 
						except SyntaxError or NameError: 
							e.delete(0,END) 
							e.insert(0,'Invalid Input!') 
						else: 
							e.delete(0,END) 
							e.insert(0,value) 

					def squareroot(): 
						"""squareroot method"""
						getandreplace() 
						try: 
							# evaluate the expression using the eval function 
							value= eval(newtext) 
						except SyntaxError or NameError: 
							e.delete(0,END) 
							e.insert(0,'Invalid Input!') 
						else: 
							sqrtval=math.sqrt(value) 
							e.delete(0,END) 
							e.insert(0,sqrtval) 

					def square(): 
						"""square method"""
						getandreplace() 
						try: 
							#evaluate the expression using the eval function 
							value= eval(newtext) 
						except SyntaxError or NameError: 
							e.delete(0,END) 
							e.insert(0,'Invalid Input!') 
						else: 
							sqval=math.pow(value,2) 
							e.delete(0,END) 
							e.insert(0,sqval) 

					def clearall(): 
							"""when clear button is pressed,clears the text input area"""
							e.delete(0,END) 

					def clear1(): 
							txt=e.get()[:-1] 
							e.delete(0,END) 
							e.insert(0,txt) 

					def action(argi): 
							"""pressed button's value is inserted into the end of the text area"""
							e.insert(END,argi)
					def quitcalc():
						global semaphore
						semaphore=0
						print('Exiting Main Memory')
						print(semaphore)
						print('Used/Total : 0 B / 100 B')
						mem.config(text='Used/Total : 0 B /100 B')
						root.destroy()

					Button( root,text="=",width=11,height=3, command=lambda:equals()).grid(row=4, column=4,columnspan=2) 
					Button( root,text='AC',width=5,height=3, command=lambda:clearall()).grid(row=1, column=4) 
					Button( root,text='C',width=5,height=3, command=lambda:clear1()).grid(row=1, column=5) 
					Button( root,text="+",width=5,height=3, command=lambda:action('+')).grid(row=4, column=3) 
					Button( root,text="x",width=5,height=3, command=lambda:action('x')).grid(row=2, column=3) 
					Button( root,text="-",width=5,height=3, command=lambda:action('-')).grid(row=3, column=3) 
					Button( root,text="÷",width=5,height=3, command=lambda:action('/')).grid(row=1, column=3) 
					Button( root,text="%",width=5,height=3, command=lambda:action('%')).grid(row=4, column=2) 
					Button( root,text="7",width=5,height=3, command=lambda:action('7')).grid(row=1, column=0) 
					Button( root,text="8",width=5,height=3, command=lambda:action(8)).grid(row=1, column=1) 
					Button( root,text="9",width=5,height=3, command=lambda:action(9)).grid(row=1, column=2) 
					Button( root,text="4",width=5,height=3, command=lambda:action(4)).grid(row=2, column=0) 
					Button( root,text="5",width=5,height=3, command=lambda:action(5)).grid(row=2, column=1) 
					Button( root,text="6",width=5,height=3, command=lambda:action(6)).grid(row=2, column=2) 
					Button( root,text="1",width=5,height=3, command=lambda:action(1)).grid(row=3, column=0) 
					Button( root,text="2",width=5,height=3, command=lambda:action(2)).grid(row=3, column=1) 
					Button( root,text="3",width=5,height=3, command=lambda:action(3)).grid(row=3, column=2) 
					Button( root,text="0",width=5,height=3, command=lambda:action(0)).grid(row=4, column=0) 
					Button( root,text=".",width=5,height=3, command=lambda:action('.')).grid(row=4, column=1) 
					Button( root,text="(",width=5,height=3,	command=lambda:action('(')).grid(row=2, column=4) 
					Button( root,text=")",width=5,height=3,	command=lambda:action(')')).grid(row=2, column=5) 
					Button( root,text="?",width=5,height=3,	command=lambda:squareroot()).grid(row=3, column=4) 
					Button( root,text="x²",width=5,height=3, command=lambda:square()).grid(row=3, column=5)
					Button( root,text='EXIT',width=40,height=3, command=quitcalc).grid(row=5, column=0,columnspan=6)
					mainloop()
				run()


		t.load1 = Image.open('Calculator.png')
		t.load1 = t.load1.resize((70,70), Image.ANTIALIAS)
		t.photo1 = ImageTk.PhotoImage(t.load1,master=t)
		t.img1 = Button(t, image=t.photo1,command=run_calc)
		t.img1.image = t.photo1
		t.img1.place(x=10, y=150, width=70, height=70)

		def run_file():
			global logged
			logged=logged+str(datetime.datetime.now())+' File Explorer\n'
			import subprocess
			subprocess.Popen('explorer "C:\"')

		t.load2 = Image.open('file.png')
		t.load2 = t.load2.resize((70,70), Image.ANTIALIAS)
		t.photo2 = ImageTk.PhotoImage(t.load2,master=t)
		t.img2 = Button(t, image=t.photo2,command=run_file)
		t.img2.image = t.photo2
		t.img2.place(x=10, y=250, width=70, height=70)


		def run_terminal():
			
			def run():
				global logged
				logged=logged+str(datetime.datetime.now())+' Terminal\n'
				t=Tk()
				t.title('Terminal')
				t.configure(background = 'grey')
				w, h = t.winfo_screenwidth(), t.winfo_screenheight()
				t.geometry("1000x150+245+245")
				path=os.getcwd()
				data='MiniOS/DRS:> '

				def quitterminal():
					t.destroy()
					return

				def check():
					if e.get()!='':
						if e.get()=='cwd':
							temp=data+''+os.getcwd()
							line1.configure(text=temp)
							e.delete(0,'end')
							#res(len(temp)*5)
						elif e.get()=='hostname':
							temp=data+''+os.environ['COMPUTERNAME']
							line1.configure(text=temp)
							e.delete(0,'end')
							#res(len(temp)*5)
						elif e.get()=='who':
							temp=data+''+user
							line1.configure(text=temp)
							e.delete(0,'end')
							#res(len(temp)*5)
						elif e.get()=='ls':
							temp=data+''+(' , '.join(map(str, (os.listdir(os.getcwd())))))
							line1.configure(text=temp)
							e.delete(0,'end')
							#res(len(temp)*5)
						elif e.get()=='shutdown':
							sys.exit()
							e.delete(0,'end')
						elif e.get()=='exit':
							quitterminal()
						else:
							temp=data+"'"+e.get()+"'"+" is not recognized as an internal or external command, operable program or batch file."
							line1.configure(text=temp)
							e.delete(0,'end')
						

				line1=Label(t, text=data, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10), anchor='w')
				line2=Label(t, text= data, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10), anchor='w')
				e=Entry(t, bg='black', fg='white', font=tkFont.Font(family="Times New Roman", size=10))
				submit=Button(t, text='RUN', command=check)
				quitt=Button(t, text='QUIT TERMINAL', command=quitterminal)
				line1.place(x=0, y=0, width=1000, height=50)
				line2.place(x=0, y=50, width=130, height=50)
				e.place(x=130, y=50, width=870, height=50)
				submit.place(x=0, y=100, width=800, height=50)
				quitt.place(x=800, y=100, width=200, height=50)
				t.mainloop()
			global semaphore
			if semaphore==0:
				run()
			else:
				run()
				#suspend others and then run terminal
				pass


		t.load3 = Image.open('terminal.png')
		t.load3 = t.load3.resize((70,70), Image.ANTIALIAS)
		t.photo3 = ImageTk.PhotoImage(t.load3,master=t)
		t.img3 = Button(t, image=t.photo3,command=run_terminal)
		t.img3.image = t.photo3
		t.img3.place(x=10, y=350, width=70, height=70)


		def run_music():
			global logged
			logged=logged+str(datetime.datetime.now())+' Music Playery\n'
			import music as tty
			ob=tty.MusicPlayer()

		t.load4 = Image.open('music.png')
		t.load4 = t.load4.resize((70,70), Image.ANTIALIAS)
		t.photo4 = ImageTk.PhotoImage(t.load4,master=t)
		t.img4 = Button(t, image=t.photo4,command=run_music)
		t.img4.image = t.photo4
		t.img4.place(x=10, y=450, width=70, height=70)


	if user=='root':
		t.maxsize(1200,700)
		def run_sjf():
			global logged
			logged=logged+str(datetime.datetime.now())+' Accessed Process Scheduler \n'
			import sjf as tty
			ob=tty.shortestjob(t)
		t.load5 = Image.open('process.jpg')
		t.load5 = t.load5.resize((70,70), Image.ANTIALIAS)
		t.photo5 = ImageTk.PhotoImage(t.load5,master=t)
		t.img5 = Button(t, image=t.photo5,command=run_sjf)
		t.img5.image = t.photo5
		t.img5.place(x=1120, y=150, width=70, height=70)

		def run_best():
			global logged
			logged=logged+str(datetime.datetime.now())+' Accessed Memory Manager\n'
			import bestfit as tty
			ob=tty.memory()

		t.load6 = Image.open('memory.png')
		t.load6 = t.load6.resize((70,70), Image.ANTIALIAS)
		t.photo6 = ImageTk.PhotoImage(t.load6,master=t)
		t.img6 = Button(t, image=t.photo6,command=run_best)
		t.img6.image = t.photo6
		t.img6.place(x=1120, y=250, width=70, height=70)

		def run_filemgmt():
			global logged
			logged=logged+str(datetime.datetime.now())+' Accessed Partitions\n'
			import filemgmt as tty
			ob=tty.run_file()

		t.load8 = Image.open('filemgmt.png')
		t.load8 = t.load8.resize((70,70), Image.ANTIALIAS)
		t.photo8 = ImageTk.PhotoImage(t.load8,master=t)
		t.img8 = Button(t, image=t.photo8,command=run_filemgmt)
		t.img8.image = t.photo8
		t.img8.place(x=1120, y=350, width=70, height=70)


	def shut():
		global logged
		logged=logged+str(datetime.datetime.now())+' Logged out'
		x=user+'.txt'
		file = open(x,'a') 
		file.write(logged) 
		file.close()
		sys.exit()

	t.load9 = Image.open('power.png')
	t.load9 = t.load9.resize((70,70), Image.ANTIALIAS)
	t.photo9 = ImageTk.PhotoImage(t.load9,master=t)
	t.img9 = Button(t, image=t.photo9, command=shut)
	t.img9.image = t.photo9
	t.img9.place(x=940, y=0, width=50, height=50)
	t.mainloop()

#run_home('root')