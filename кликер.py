from tkinter import*

click = 0 

def click_button():
  
    r = ["Linux", "Python", "Tk", "Tkiner"]
    lis = Listbox(root,selectmode=SINGLE,hight=4)
    for i in r:
        lis.insert(END,i)
   
    global click
    click += 1
    btn.config(text="clicks {}".format(click))

root = Tk()
root.title("GUI на Pithon")
root.geometry("400x400")

btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)

but = Button(background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)

bat = Button(background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)

btn.grid(row=0,column=0)
but.grid(row=1,column=1)
bat.grid(row=2,column=2)



root.mainloop()
