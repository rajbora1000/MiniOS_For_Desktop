from tkinter import *
class memory:
    def __init__(self):
        root=Tk()
        self.root=root
        self.root.title('Memory Management')
        #self.root.geometry('300x200')
        self.mem=[]
        self.p=[]
        self.l1=Label(self.root,text='Enter the size of Memory Block:')
        self.l1.grid(row=0,column=0)
        self.e1=Entry(self.root)
        self.e1.grid(row=0,column=1)
        self.b1=Button(self.root,text='Add Block',command=self.addm)
        self.b1.grid(row=1,column=0)
        self.b2=Button(self.root,text='Done',command=self.stopm)
        self.b2.grid(row=1,column=1)
        self.l2=Label(self.root,text='Enter the size of Process: ')
        self.l2.grid(row=2,column=0)
        self.e2=Entry(self.root)
        self.e2.grid(row=2,column=1)
        self.b3=Button(self.root,text='Add Process',command=self.addp)
        self.b3.grid(row=3,column=0)
        self.b4=Button(self.root,text='Done',command=self.pstop)
        self.b4.grid(row=3,column=1)
        self.te=Text(self.root)
        self.te.grid(row=4,column=0,columnspan=2)
    def addm(self):
        self.mem.append(int(self.e1.get()))
        self.e1.delete(0,END)
    def addp(self):
        self.p.append(int(self.e2.get()))
        self.e2.delete(0,END)
    def stopm(self):
        self.e1.config(state='disabled')
    def pstop(self):
        self.e2.config(state='disabled')
        self.te.insert(INSERT,'Memory Block\tSize')
        i=0
        while i<len(self.mem):
            self.te.insert(INSERT,'\nBlock'+str(i+1)+'\t\t'+str(self.mem[i]))
            i+=1
        self.bestfit()
    def bestfit(self):
        i=0
        while i<len(self.p):
            dif=max(self.p)
            k=-1
            j=0
            while j<len(self.mem):
                if self.mem[j]-self.p[i]<dif and self.mem[j]-self.p[i]>=0:
                    dif=self.mem[j]-self.p[i]
                    k=j
                j+=1
            if k!=-1:
                self.te.insert(INSERT,'\nProcess '+str(i+1)+' allocated to Block '+str(k+1))
                self.mem[k]-=self.p[i]
            else:
                self.te.insert(INSERT,'\nProcess '+str(i+1)+' not allocated to any Block')
            i+=1

#ob=memory(t)
#t.mainloop()