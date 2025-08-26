# IMPORT TKINTER
from tkinter import *
cal = Tk()
data = ""
def get_data(value):
    global data
    data = data+str(value)
    vars.set(data)
def equal_data():
    global data
    try:
        total = str(eval(data))
        vars.set(total)
        data = ""
    except:
        vars.set("ERROR")
def clear():
    global data
    data = ""
    vars.set("")
# TITLE
cal.title("CALCULATOR",)
# LOGO
cal.iconbitmap(r"C:\Users\AMUDMC\Desktop\PYTHON AQUIB/Calculator_30001.ico")
# BACKGROUND COLOR
cal.config(bg="#FFFFFF")
# cal.minsize(500,500)
cal.geometry("520x580")
cal.resizable(False,False)
# LABEL
lab1 = Label(cal,text="CALCULATOR",font=("ARIAL ROUNDED MT BOLD",30,"bold"),bg="#D1EEEE",
             relief="groove",justify=CENTER)
lab1.pack()
# CALCULATOR ENTRY BUTTON
vars = StringVar()
cal_entry_but = Entry(cal,font=("Montserrat Black",20,"bold"),bd=5,textvariable=vars)
cal_entry_but.place(x=20,y=80,height=50,width=480)
# BUTTONS
but_1 = Button(cal,text="1",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(1))
but_1.place(x=20,y=150,height=80,width=120)

but_2 = Button(cal,text="2",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(2))
but_2.place(x=140,y=150,height=80,width=120)

but_3 = Button(cal,text="3",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(3))
but_3.place(x=260,y=150,height=80,width=120)

but_div = Button(cal,text="/",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data("/"))
but_div.place(x=380,y=150,height=80,width=120)

but_4 = Button(cal,text="4",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(4))
but_4.place(x=20,y=230,height=80,width=120)

but_5 = Button(cal,text="5",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(5))
but_5.place(x=140,y=230,height=80,width=120)

but_6 = Button(cal,text="6",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(6))
but_6.place(x=260,y=230,height=80,width=120)

but_mul = Button(cal,text="*",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data("*"))
but_mul.place(x=380,y=230,height=80,width=120)

but_7 = Button(cal,text="7",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(7))
but_7.place(x=20,y=310,height=80,width=120)

but_8 = Button(cal,text="8",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(8))
but_8.place(x=140,y=310,height=80,width=120)

but_9 = Button(cal,text="9",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(9))
but_9.place(x=260,y=310,height=80,width=120)

but_sub = Button(cal,text="-",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data("-"))
but_sub.place(x=380,y=310,height=80,width=120)

but_dot = Button(cal,text=".",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data("."))
but_dot.place(x=20,y=390,height=80,width=120)

but_zero = Button(cal,text="0",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data(0))
but_zero.place(x=140,y=390,height=80,width=120)

but_clear = Button(cal,text="C",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=clear)
but_clear.place(x=260,y=390,height=80,width=120)

but_add = Button(cal,text="+",font=("Montserrat Black",20,"bold"),bg="#E0E0E0",fg="#000000",command=lambda:get_data("+"))
but_add.place(x=380,y=390,height=80,width=120)

but_equ = Button(cal,text="=",font=("Montserrat Black",20,"bold"),bg="#2196F3",fg="#000000",command=equal_data)
but_equ.place(x=20,y=470,height=80,width=480)

cal.mainloop()