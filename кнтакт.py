from tkinter import *
root = Tk()
from tkinter import filedialog as fd
img = PhotoImage(file="avatar.png")

import pandas as  pd 
import os

file = pd.read_csv('telephone.docx')
df = pd.DataFrame(file)
# print(str(df['номер'][3]))

data = {
    'Имя': [],
    'Фамилия': [],
    'номер': [],
    'emayl': [],
    'аватарка':[]
}
contacts = pd.DataFrame(data)
contacts.to_csv("phonebook.csv")

# for x in massiv:
#     print(enumerate(massiv))

# def reg():
#     for x in massiv:
#         x = x.lower()
#     return massiv

# massive = ['Петров','Иванов','Иванов']
# print(massiv[1].lover())
# print(sorted(reg(massiv)))

# x = x.lower()

def deleted():
    index = Lb.curselection()[0]
    
    
def create():
    index = Lb.curselection()[0]
    E1=pole1.get()
    E2=pole2.get()
    E3=pole3.get()
    E4=pole4.get()
    Lb.delete(index)
    result=E1 + " " + E2 + " *" + E3 + "*" + " - " + E4
    contacts.loc[0]= {'Имя':'tghjk', 'Фамилия':'tghjk', 'номер':'12345678900', 'imail':'qwe@gmail.com'}
    constant = contacts.sort_values(by='Имя')
    constant = constant.reset_index(drop=True)
    constant.to_csv("phones.csv")
    pole1.delete(0,END)
    pole2.delete(0,END)

def poper():
    pass

# def insert():
#     telephone = fd.askopenfilename()
#     f = open(telephone)
#     s = f.read()
#     text.insert(1.0 s)
#     f.close()

# def extract():
#     telephone = fd.asksaveasfilename(filetypes=)
#     f = open(telephone, "w")

def infa():
    pass

sortlist = []
dictsort = []

# with open ('example.csv','r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         sortlist.append(row['Name']+'-'+row['last_name']+'-'+row['Nomber'])
#     sortist = sorted(sortlist)
#     for x in sortlist:
#         x = x.split('-')
#         x = {'Name':x[0], 'last_name': x[1], 'Namber':x[2]}
#         dictsort.append(x)

pole1 = Entry(width=23)
pole2 = Entry(width=23)
pole3 = Entry(width=23)
pole4 = Entry(width=23)

pole01 = Entry(width=23)
pole02 = Entry(width=23)
pole03 = Entry(width=23)
pole04 = Entry(width=23)

avatarka = Button(image=img)

but1 = Button(text="загрузить",command=create,bg="green")
but2 = Button(text="удалить",command=poper,bg="red")
but3 = Button(text="изменить",command=deleted,bg="blue")
but4 = Button(text="информация",command=infa)

l1 = Label(text="имя")
l2 = Label(text="фамилия")
l3 = Label(text="ник")
l4 = Label(text="телефон") 
l5 = Label(text="здесь аватарка")

Lb = Listbox(width=45)



pole1.grid(row=0,column=0)
pole2.grid(row=1,column=0)
pole3.grid(row=2,column=0)
pole4.grid(row=3,column=0)

pole01.grid(row=5,column=1)
pole02.grid(row=5,column=2)
pole03.grid(row=5,column=3)
pole04.grid(row=5,column=4)

l1.grid(row=0,column=1)
l2.grid(row=1,column=1)
l3.grid(row=2,column=1)
l4.grid(row=3,column=1)
l5.grid(row=5,column=2)

but1.grid(row=0,column=2)
but2.grid(row=1,column=2)
but3.grid(row=2,column=2)
but4.grid(row=6,column=0)

Lb.grid(row=5,column=0)

root.mainloop()