# IMPORT TKINTER
#TKINTER WINDOW
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip 
# COLOURS 
COLORS = {
      "main_bg": "#1a1d29",
      "secondry_bg": "#2d3748",
      "primary_text" : "#ffffff",
      "accent" : "#00d9ff",
      "button_bg": "#32d74b",
      "button_text": "#ffffff",
      "clear_copy_bg": "#1a1d29",
      "border": "#00d9ff",
      "active_back_ground _colour":"#28c440", 
      }

# CREAT WINDOW
pas_gen = Tk()
pas_gen.title("PASSWORD LENGTH")
pas_gen.config(bg=COLORS["main_bg"])
pas_gen.iconbitmap(r"D:\AKTU b.tech\internship/Strong Password Generator.ico")
pas_gen.geometry ("460x460")
pas_gen.resizable(False,False)
# FUNCTION FOR LENGTH OF PASSWORD 
# TAKE RAMDON CHARACTERS
def genrate_password():
      lenth = int(ent.get())
      characters = ""
      if var_upper.get():
            characters += string.ascii_uppercase

      if var_lower.get():
            characters += string.ascii_lowercase

      if var_digits.get():
            characters += string.digits

      if var_symbols.get():
            characters += string.punctuation

      if  characters == "":
            messagebox.showwarning("warning","PLEASE SELECT AT LEAST ONE CHARACTER TYPE!")
            return
      password = "".join(random.choice(characters) for _ in range(lenth))
      paswordEntry.delete(0,END)           
      paswordEntry.insert(0,password)
# FUNCTION FOR COPY CHARACTER
def copypassword():
      password = paswordEntry.get()
      if password:
            pyperclip.copy(password)
            messagebox.showinfo('copied',"password copied to clipboard")
      else:
            messagebox.showwarning('WARNING',"'NO' PASSWORD TO COPY")
#LABEL 
lab1 = Label(pas_gen,text="PASSWORD GENERATOR",
             font=("Montserrat Black",20,"bold"),justify="center",bg=COLORS["main_bg"],fg=COLORS["primary_text"])
lab1.place(x=30,y=20,height=50,width=400)
#ENTRY BOX
vars = StringVar()
ent = Entry(pas_gen,font=("Montserrat Black",20,"bold"),bd=8,textvariable=vars,
            relief=SOLID,bg=COLORS["secondry_bg"],fg=COLORS["primary_text"],
            insertbackground=COLORS["primary_text"],highlightbackground=COLORS["accent"],
            highlightcolor=COLORS["accent"],highlightthickness=2,justify="center")
ent.place(x=30,y=80,height=50,width=400)
# FUNCTION FOR CHEACK BOX
var_upper = BooleanVar(value = True)
var_lower = BooleanVar(value = True)
var_digits = BooleanVar(value = True)
var_symbols = BooleanVar(value = True)
#CHEACK BUTTONS
cb1 = Checkbutton(pas_gen,text="INCLUDE UPPERCASE LETTER",font=("Montserrat Black",10,"bold"),bg=COLORS["main_bg"],
                  fg=COLORS["primary_text"],activebackground=COLORS["main_bg"],activeforeground=COLORS["primary_text"],
                  selectcolor=COLORS["secondry_bg"],relief=FLAT,bd=0
                  ,variable=var_upper)
cb1.place(x=110,y=160)

cb2 = Checkbutton(pas_gen,text="INCLUDE LOWERCASE LATTER",font=("Montserrat Black",10,"bold"),bg=COLORS["main_bg"],
                  fg=COLORS["primary_text"],activebackground=COLORS["main_bg"],activeforeground=COLORS["primary_text"],
                  selectcolor=COLORS["secondry_bg"],relief=FLAT,bd=0,
                  variable=var_lower)
cb2.place(x=110,y=180)

cb3 = Checkbutton(pas_gen,text="INCLUDE DIGITS",font=("Montserrat Black",10,"bold"),bg=COLORS["main_bg"],
                  fg=COLORS["primary_text"],activebackground=COLORS["main_bg"],activeforeground=COLORS["primary_text"],
                  selectcolor=COLORS["secondry_bg"],relief=FLAT,bd=0,
                  variable=var_digits)
cb3.place(x=110,y=200)

cb4 = Checkbutton(pas_gen,text="INCLUDE SPECIAL CHARACTER",font=("Montserrat Black",10,"bold"),bg=COLORS["main_bg"],
                  fg=COLORS["primary_text"],activebackground=COLORS["main_bg"],activeforeground=COLORS["primary_text"],
                  selectcolor=COLORS["secondry_bg"],relief=FLAT,bd=0,
                  variable=var_symbols)
cb4.place(x=110,y=220)
#CREATE BUTTONS
but_1 = Button(pas_gen,text="GENRATE PASSWORD",font=("Montserrat Black",12,"bold"),
               bd=0,command = genrate_password,bg=COLORS["button_bg"],fg=COLORS["button_text"],
               activebackground=COLORS["active_back_ground _colour"],activeforeground=COLORS["button_text"],
               relief=FLAT,cursor="hand2")

paswordEntry = Entry(pas_gen,font=("Arial",16,"bold"),justify = "center")
paswordEntry.place(x=30,y=330,height=30,width=400)
but_1.place(x=140,y=260,height=50,width=200)
#CLEAR BUTTON
but_2 = Button(pas_gen,text="CLEAR",command=lambda:paswordEntry.delete(0,'end'),
               font=("Montserrat Black",10,"bold"),bg=COLORS["clear_copy_bg"],fg=COLORS["accent"],
               activebackground=COLORS["accent"],activeforeground=COLORS["main_bg"],relief=SOLID,cursor="hand2")
but_2.place(x=30,y=380,height=50,width=100)
#COPY BUTTON
but_3 = Button(pas_gen,text="COPY",command=copypassword,font=("Montserrat Black",10,"bold"),
               bd=2,bg=COLORS["clear_copy_bg"],fg=COLORS["accent"],activebackground=COLORS["accent"],
               activeforeground=COLORS["main_bg"],relief=SOLID,cursor="hand2",highlightcolor=COLORS["accent"])
but_3.place(x=320,y=380,height=50,width=100)

pas_gen.mainloop()
