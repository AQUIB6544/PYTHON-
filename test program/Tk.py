from tkinter import *
# FOR TITTLT,ICON,TRANSPARENCE,BACKGROUND COLOUR,MINIMUN SIZE,LABLE,INPUT,PHOTOIMAGE,LABLEFRAM,BUTTON
win = Tk()
win.title("* AQUIB *")
win.iconbitmap(r'C:\Users\AMUDMC\Desktop\PYTHON AQUIB/bird_2.ico')
win.attributes("-alpha")
win.config(bg="seashell4")
win.minsize(500,500)
lab1 = Label(win,text="REGISTRATION FORM",fg="white",font=("TIME NEW ROMAN",30,"bold"),bg="black",)
lab1.pack()
lab2 = Label(win,text="YOUR NAME",fg="black",font=("TIME NEW ROMAN",15,"bold"))
lab2.place(x=200,y=60)
Entry = input("ENTER YOUR NAME :")
vars = StringVar()
lab3 = Label(win,font=("ARIAL ROUND MT bOLD",6,"bold"),textvariable=vars)
lab3.place(x=200,y=100)
vars.set(Entry)
ph = PhotoImage(file="D:\AMU/logo5.png")
lab3 = Label(win,image=ph,bg="red",text="see this image",compound="bottom",font=50)
lab3.place(x=150,y=200,height=300,width=300)
lf = LabelFrame(win,text="AQUIB",font=30,)
bt = Button(win,text="on",font=30,bg="green",image=ph,command="left")
bt.place(x=800,y=200,height=300,width=300)
def test():
    print(vars.get())
cb = Checkbutton(win,text="PYTHON",font=30,variable=vars)
cb.pack()
bt = Button(win,text="PYTHON",font=30,command=Text)
bt.pack()
print(vars.get())
# RADIOBUTTON
r1 = Radiobutton(win,text="python",value="py",variable=vars)
r1.pack(fill=X)
r2 = Radiobutton(win,text="java",value="ja",variable=vars,bg="green")
r2.pack(fill=X)



win.mainloop()