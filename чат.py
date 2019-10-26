from tkinter import*

def clics_button():
    r = ["Linux", "Python", "Tk", "Tkiner"]
    lis = Listbox(root,selectmode=SINGLE,hight=4)
    for i in r:
        lis.insert(END,i)

root = Tk()
root.title("GUI на Pithon")
root.geometry("400x400")
root.mainloop()