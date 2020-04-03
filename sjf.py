from tkinter import *
class shortestjob:
    def __init__(self,root):
        root=Tk()
        self.root=root
        self.n=0
        self.i=1
        self.arr=[]
        self.b=[]
        self.pos=[]
        self.root.title('Shortest Job First')
        self.l1=Label(self.root,text='Number of processes:')
        self.l1.grid(row=0,column=0,columnspan=2)
        self.e1=Entry(self.root)
        self.e1.grid(row=0,column=2)
        self.b1=Button(self.root,text='Okay',command=self.stop)
        self.b1.grid(row=0,column=3)
        self.text=StringVar()
        self.text.set('Process 1')
        self.l2=Label(self.root,textvariable=self.text)
        self.l2.grid(row=1,column=0)
        self.l3=Label(self.root,text='Arrival Time')
        self.l3.grid(row=2,column=0)
        self.e2=Entry(self.root)
        self.e2.grid(row=2,column=1)
        self.l4=Label(self.root,text='Burst Time')
        self.l4.grid(row=2,column=2)
        self.e3=Entry(self.root)
        self.e3.grid(row=2,column=3)
        self.b2=Button(self.root,text='Enter',command=self.update,width=10)
        self.b2.grid(row=3,column=0,columnspan=5)
        self.te=Text(self.root)
        self.te.grid(row=4,column=0,columnspan=5)
    def stop(self):
        self.e1.config(state='disabled')
        self.n=int(self.e1.get())
    def update(self):
        self.arr.append(int(self.e2.get()))
        self.b.append(int(self.e3.get()))
        self.pos.append(self.i)
        self.e2.delete(0,END)
        self.e3.delete(0,END)
        self.i+=1
        if self.i<=self.n:
            self.text.set('Process '+str(self.i))
        else:
            self.e2.config(state='disabled')
            self.e3.config(state='disabled')
            self.sjf()
    def sjf(self):
        a=[]
        j=0
        wt=0
        twt=0
        tat=0
        tta=0
        while j<self.n:
            a.append([self.pos[j],self.arr[j],self.b[j]])
            j+=1
        a.sort(key=lambda x: x[2])
        tat=a[0][2]
        self.te.insert(INSERT,'Processes will be executed in the order:\n')
        j=0
        while j<self.n:
            self.te.insert(INSERT,str(a[j][0])+' ')
            j+=1
        j=0
        self.te.insert(INSERT,'\nProcess no.\tWait Time\tTurn-around Time\n')
        self.te.insert(INSERT,str(a[j][0])+'\t\t'+str(wt)+'\t\t'+str(tat))
        j=1
        while j<self.n:
            wt=tat
            twt+=wt
            tat=wt+a[j][2]
            tta+=tat
            self.te.insert(INSERT,'\n'+str(a[j][0])+'\t\t'+str(wt)+'\t\t'+str(tat))
            j+=1
        self.te.insert(INSERT,'\nAverage Waiting Time: '+str(twt/self.n))
        self.te.insert(INSERT,'\nAverage Turn Around Time: '+str(tta/self.n))
#ob=shortestjob(t)
#t.mainloop()
