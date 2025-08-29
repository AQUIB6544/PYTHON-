from tkinter import *
# CREAT WINDOW
todo = Tk()
todo.title("TO DO LIST")
todo.iconbitmap("D:\AKTU b.tech\internship\playlist_list_6297.ico")
todo.geometry("600x400")
todo.resizable(False,False)
todo.config(bg="gray")
# FUNCTION FOR ADD
def add():
    task = ent.get()
    lis.insert (END,task)
    ent.delete(0,END)
    # FUNCTION FOR MARK
def mark ():
    pos = lis.curselection()
    task = lis.get(pos)    
    lis.delete(pos)
    lis.insert (END,f"{task}  ✔")
# FUNCTION FOR DELETE
def delete():
    pos = lis.curselection()[0]
    lis.delete(pos)
# CREATE LABEL
lab01 = Label(todo,text="TO-DO-LIST",font=("Montserrat Black",20,"bold"))
lab01.place(x=220,y=10,height=30,width=170)
lab02 = Label(todo,text="ENTER TASK: ",font=("Montserrat Black",12,"bold"))
lab02.place(x=20,y=60,height=30,width=120)
# CREATE ENTRY BOX
ent = Entry(todo,font=("Montserrat Black",10,"bold"))
ent.place(x=150,y=60,height=30,width=430)
# CREATE LIST 
lis = Listbox(todo,font=("Montserrat Black",10,"bold"))
lis.place(x=20,y=100,height=185,width=560)
# CREATE BUTTON 
but_1 = Button(todo,text="ADD",font=("Montserrat Black",10,"bold"),command=add)
but_1.place(x=50,y=305,height=45,width=80)
but_2 = Button(todo,text="MARK",font=("Montserrat Black",10,"bold"),command=mark)
but_2.place(x=250,y=305,height=45,width=80)
but_3 = Button(todo,text="DELETE",font=("Montserrat Black",10,"bold"),command=delete)
but_3.place(x=460,y=305,height=45,width=80)
todo.mainloop()