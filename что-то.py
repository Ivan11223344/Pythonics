from  tkinter import *
root = Tk()

def change_labal():
    ent = pole1.get()
    labl = l1.config(text=ent),l2.config(text=ent),l3.config(text=ent)

def change_labal_two():
    ent =pole2.get()
    labl = l2.config(text=ent),l2.config(text=ent),l3.config(text=ent)             

pole1 = Entry(width=25)
pole2 = Entry(width=25)
pole3 = Entry(width=25)

bt1 = Button(text="загрузить",command = change_labal)

l1 = Label("фамилия")
l2 = Label("имя")
l3 = Label("номер телефона")

pole1.grid(row=0,column=0)
pole2.grid(row=0,column=1)
pole3.grid(row=0,column=2)

bt1.grid(row=0,column=3)

l1.grid(row=1,column=0)
l2.grid(row=1,column=0)
l3.grid(row=1,column=0)

root.mainloop()