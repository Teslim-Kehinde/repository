from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
layout = Tk()
layout.title("Start Up")
layout.resizable(True,True)
#Menu Frame
fra1 = tkinter.Frame(layout, bg="purple")
fra1.pack(side="top",fill=X)
def continuebutton():
    print("Continue.....")
def newbutton():
    print("Starting New Game....")
def savebutton():
    print("Saving New Game....")

#Introducing menu
main_menu = Menu(layout)
layout.config(menu=main_menu)

main_menufam1 = Menu(main_menu)
main_menu.add_cascade(label="Play", menu=main_menufam1)

main_menufam1.add_command(label="Continue", command=continuebutton)
main_menufam1.add_separator()
main_menufam1.add_command(label="Start New Game", command=newbutton)

main_menufam2 = Menu(main_menu)
main_menu.add_cascade(label="Exit", menu=main_menufam2)
main_menufam2.add_command(label="Save ", command=savebutton)
main_menufam2.add_command(label="Don't save", command=layout.quit)
#Status bar
labe = tkinter.Label(layout, text="Permissions: RW   |End-of-lines: CRLF  |Encoding: ASCII   |Line:34  Column:108|Memory: 61%", anchor=E)
labe.pack(side="bottom", fill=X)


#Style
style=ttk.Style(layout)
style.theme_use("vista")
#First Frame
fra2 = ttk.Frame(layout, height= 200, width=200,relief=RIDGE, padding=(10,10))
fra2.pack(side="left",anchor=N)

ent1 = tkinter.Entry(fra2, width=20,font=("callibri",12), foreground="black")
ent1.grid(row=0, column=1,sticky='snew',padx=2,pady=2)

lab1 = tkinter.Label(fra2, text="Username", bg="black",fg="white",relief=RAISED).grid(row=0, column=0, sticky='snew',padx=2,pady=2)

ent2 =  ttk.Entry(fra2, width=20, font=("callibri",12), foreground="black",show="*")
ent2.grid(row=1, column=1,sticky='snew',padx=2,pady=2)


lab2 = tkinter.Label(fra2, text="Password", bg="black",fg="white",relief=GROOVE).grid(row=1, column=0, sticky='snew',padx=2,pady=2)
def clickon():
    print(ent1.get())
    print(ent2.get())
    if ent1.get() == " " and ent2.get() == " ":
        print("Please input your details")
    else:
        ttk.LabelFrame(fra2, text="Welcome to our\n website",height=100,width=100,padding=(5,5)).grid(row=3, column=0, columnspan=2)
        if ent1.get()== "Teslim Kehinde" and ent2.get()=="Takbaba2272":
            messagebox.showinfo(title="Login info", message="We from Tcrux-Tech welcome {} to our app".format(ent1.get()))
        else:
            messagebox.showinfo(title="Login info", message="Please input correct information")
    ent1.delete(0, END)
    ent2.delete(0, END)  
but1 = tkinter.Button(fra2, text="Login",command=clickon,relief=GROOVE, fg="#6bcadf", background="#10090d", font=("TimesNewRoman", 12,"bold"))
but1.grid(row=2, column=1,padx=2,pady=2)
layout.rowconfigure(0, weight=1)
layout.rowconfigure(1, weight=1)
layout.rowconfigure(2, weight=1)
layout.columnconfigure(0, weight=1)
layout.columnconfigure(1, weight=1)


layout.mainloop()
