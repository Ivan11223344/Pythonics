from  tkinter import *
root = Tk()

def create():
    E1=pole1.get()
    E2=pole2.get()
    result=E1 + " - " + E2
    Lb.insert(END,result)
    pole1.delete(0,END)
    pole2.delete(0,END)

def poper():
    index = Lb.curselection()[0]
    Lb.delete(index)      

def deleted():
    index = Lb.curselection()[0]
    E1=pole1.get()
    E2=pole2.get()
    Lb.delete(index)
    result=E1 + " - " + E2
    Lb.insert(END,result)
    pole1.delete(0,END)
    pole2.delete(0,END)

pole1 = Entry(width=25)
pole2 = Entry(width=25)

but1 = Button(text="загрузить",command=create,bg="green")
but2 = Button(text="удалить",command=poper,bg="red")
but3 = Button(text="изменить",command=deleted,bg="blue")

l1 = Label(text="имя")
l2 = Label(text="телефон")

Lb = Listbox()

pole1.grid(row=0,column=0)
pole2.grid(row=1,column=0)

l1.grid(row=0,column=1)
l2.grid(row=1,column=1)

but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)

Lb.grid(row=4,column=0)

root.mainloop()