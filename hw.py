from tkinter import *
root=Tk()
root.title("Multiplication")
root.geometry('400x300')
l1=Label(text="Multiplication", fg="white", bg="blue", height=1, width=300)
n1l=Label(text="ENTER FIRST NUMBER", bg="red")
n1e=Entry()
n2l=Label(text="ENTER SECOND NUMBER", bg="red")
n2e=Entry()

def mul():
    n1= int(n1e.get())
    n2= int(n2e.get())
    mult=n1*n2
    textbox.insert(1.0,"MULTIPLICATION=")
    textbox.insert(1.17, mult)

textbox=Text(height=3)
btm=Button(text="CALCULATE", command=mul)
l1.pack()
n1l.pack()
n1e.pack()
n2l.pack()
n2e.pack()
btm.pack()
textbox.pack()
root.mainloop()
