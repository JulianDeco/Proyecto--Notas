from tkinter import *
from tkinter import messagebox
"""
SIEMPRE X E Y EMPIEZAN ARRIBA A LA IZQUIERDA
"""
root=Tk()
root.geometry('400x240')
root.resizable(0,0)
root.title('Login')

def login():
    w=Frame(root,width=400,height=240,bg='#EFAD29')
    w.place(x=0,y=28)

    #entrybox for username
    def on_enter(e):
        e1.delete(0,'end')

    def on_leave(e):
        if e1.get()=='':
            e1.insert(0,'username')

    
    e1 =Entry(w,width=28,fg='grey')
    e1.config(font=('consolas',13,'bold'))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'username')
    e1.place(x=70,y=42)



    def on_enter(e):
        e2.delete(0,'end')
    def on_leave(e):
        if e2.get()=='':
            e2.insert(0,'password')

    #entrybox for password
    e2 =Entry(w,width=28,fg='grey')
    e2.config(font=('consolas',13,'bold'))
    e2.bind("<FocusIn>", on_enter)
    e2.bind("<FocusOut>", on_leave)
    e2.insert(0,'password')
    e2.place(x=70,y=120-28)



    #command when login button pressed
    def log_command():
        
        file=open('username.txt','r')
        r=file.read()
        s=r.split()
        for j in s:
            dname=j


        myfile=open('password.txt', 'r')
        read=myfile.read()
        split1=read.split()
        for i in split1:
            dpass=i

        if e1.get()==dname and e2.get()==dpass:
            messagebox.showinfo('','     Successfully Logged in     ')
            root.destroy()
        else:
            messagebox.showwarning('try again', 'retry')
    
    Button(w,width=18,height=0,text='Login',command=log_command,border=0,bg='dark red',fg='white').place(x=130,y=146)

#signup

def signup():
    q=Frame(root,width=400,height=240,bg='purple')
    q.place(x=0,y=28)

    def on_enter(e):
        e3.delete(0,'end')
    def on_leave(e):
        if e3.get()=='':

            e3.insert(0,'enter username')
    #entrybox for username
    e3 =Entry(q,width=28,fg='grey')
    e3.config(font=('consolas',13,'bold'))
    e3.bind("<FocusIn>", on_enter)
    e3.bind("<FocusOut>", on_leave)
    e3.insert(0,'enter username')
    e3.place(x=70,y=70-28)



    def on_enter(e):
        e4.delete(0,'end')
    def on_leave(e):
        if e4.get()=='':
            e4.insert(0,'enter password')

    #entrybox for password
    e4 =Entry(q,width=28,fg='grey')
    e4.config(font=('consolas',13,'bold'))
    e4.bind("<FocusIn>", on_enter)
    e4.bind("<FocusOut>", on_leave)
    e4.insert(0,'enter password')
    e4.place(x=70,y=120-28)




    def entry_done():
        f1=open('username.txt','a')
        f1.truncate(0)
        f1.write(e3.get())
        f1.write(' ')

        f2=open('password.txt','a')
        f2.truncate(0)
        f2.write(e4.get())
        f2.write(' ')
    
        messagebox.showinfo("", "    successfully registered    ")
    

    Button(q,width=18,height=0,text='Signup',command=entry_done,border=0,fg='purple',bg='white').place(x=130,y=174-28)



def reset():
    f=Frame(root,width=400,height=240,bg='dark red')
    f.place(x=0,y=28)

    def on_enter(e):
        e5.delete(0,'end')
    def on_leave(e):
        if e5.get()=='':

            e5.insert(0,'username')
    #entrybox for username
    e5 =Entry(f,width=28,fg='grey')
    e5.config(font=('consolas',13,'bold'))
    e5.bind("<FocusIn>", on_enter)
    e5.bind("<FocusOut>", on_leave)
    e5.insert(0,'username')
    e5.place(x=70,y=70-28)



    def on_enter(e):
        e6.delete(0,'end')
    def on_leave(e):
        if e6.get()=='':
            e6.insert(0,'enter new password')

    #entrybox for password
    e6 =Entry(f,width=28,fg='grey')
    e6.config(font=('consolas',13,'bold'))
    e6.bind("<FocusIn>", on_enter)
    e6.bind("<FocusOut>", on_leave)
    e6.insert(0,'enter password')
    e6.place(x=70,y=120-28)

    def entry_done():
        f1=open('username.txt','a')
        f1.truncate(0)
        f1.write(e5.get())
        f1.write(' ')

        f2=open('password.txt','a')
        f2.truncate(0)
        f2.write(e6.get())
        f2.write(' ')
    
        messagebox.showinfo("", "   Password changed successfuly   ")
    

    Button(f,width=18,height=0,text='Reset',command=entry_done,border=0,fg='white',bg='#EFAD29').place(x=130,y=174-28)

login()

#Main_buttons
Button(root,width=18,height=0,text='C R E A R',pady=4,command=login,border=0,bg='#EFAD29',fg='white',activebackground='#EFAD29',activeforeground='white').place(x=0,y=0)
Button(root,width=19,height=0,text='V E R',pady=4,border=0,command=signup,bg='purple',fg='white',activebackground='purple',activeforeground='white').place(x=130,y=0)
Button(root,width=19,height=0,text='E N V I A R',pady=4,border=0,command=reset,bg='dark red',fg='white',activebackground='dark red',activeforeground='white').place(x=266,y=0)
root.mainloop()