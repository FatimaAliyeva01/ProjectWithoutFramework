from tkinter import *

root=Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False,False)
def register():
    name_info=nameValue.get()
    surname_info=surnameValue.get()
    password_info=passwordValue.get()
    email_info=emailValue.get()

    file = open(name_info+ ".txt","w")
    file.write(name_info+"\n")
    file.write(surname_info+"\n")
    file.write(password_info+"\n")
    file.write(email_info+"\n")
    file.close()

    nameEntry.delete(0,END)
    surnameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    emailEntry.delete(0,END)


    Label(text="Registration sucess", fg="green", font=("calibri",11)).place(x=250,y=430)




Label(root,text="Student Registration From",font="arial 25").pack(pady=50)
Label(text="Name",font=23).place(x=100,y=150)
Label(text="Surname",font=23).place(x=100,y=200)
Label(text="Password",font=23).place(x=100,y=250)
Label(text="Email",font=23).place(x=100,y=300)

#entry
nameValue=StringVar()
surnameValue=StringVar()
passwordValue=StringVar()
emailValue=StringVar()
nameEntry=Entry(root,textvariable=nameValue,width=30,bd=2,font=20)
surnameEntry=Entry(root,textvariable=surnameValue,width=30,bd=2,font=20)
passwordEntry=Entry(root,textvariable=passwordValue, show="*",width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
surnameEntry.place(x=200,y=200)
passwordEntry.place(x=200,y=250)

emailEntry.place(x=200,y=300)
#check button
checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=200,y=340)
Button(text="Register",font=20,width=11,height=2,command=register).place(x=250,y=380)


root.mainloop()

