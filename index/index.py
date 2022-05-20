from ast import Continue, Pass
from errno import ENOTSUP
from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
from tokenize import String
from turtle import width
from click import style
from numpy import var 
from tkcalendar import Calendar, DateEntry 
from datetime import datetime
import time
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from PIL import Image, ImageTk


def conn_bbdd(parametros):
    con = sqlite3.connect("recordatorios.db")
    cur = con.cursor()
    cur.execute(parametros)
    data = cur.fetchall()
    con.commit()
    con.close()
    return data

"""
PANTALLA1
""" 
def w_crear():
    #FUNCIONES
    def createDB():
        try:
            conn_bbdd("""
                    CREATE TABLE "recordatorio" (
                        "id"	INTEGER,
                        "titulo"	VARCHAR(30),
                        "fecha"	VARCHAR(15),
                        "categoria"	VARCHAR(15),
                        "descripcion"	VARCHAR(100),
                        PRIMARY KEY("id" AUTOINCREMENT)
                    )
                    """)
            messagebox.showinfo(w_crear, "Base de datos creada con éxito")
            
        except:
            a = titulos.get()
            b = fecha.get()
            c =lista.get()
            d=textos.get()
            print(a, b, c, d)
            conn_bbdd("INSERT INTO recordatorio VALUES(NULL,'" + a +
                    "','"+ b + "', '" + c +"', '"+ d +"')")
    def enviar_mail():
        # create message object instance
        msg = MIMEMultipart()
        
        a = str(titulos.get())
        b = fecha.get()
        c = lista.get()
        d = str(mail.get())
        
        #VAR descripción
        descripcion=textos.get()
        message = f'Título: {a}\nCategoría: {c}\nMensaje: {descripcion}\nFecha: {b}'
        
        # setup the parameters of the message
        password = "123"
        msg['From'] = '123'
        msg['To'] = d
        msg['Subject'] = a
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #create server
        server = smtplib.SMTP('smtp.gmail.com: 587')
        
        server.starttls()
        
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
        
        
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        
        server.quit()
        
        print ("successfully sent email to %s:" % (msg['To'])) 
    #FIN FUNCIONES
    w_crear=Frame(root,width=400,height=600,bg='#ffcc66')
    w_crear.place(x=0,y=28)
    def on_enter(e):
        e1.delete(0,'end')    
    def on_leave(e):
        if e1.get()=='':   
            e1.insert(0,'Asunto')
    
    
    e1 =Entry(w_crear,width=25,fg='black',border=0,bg='#ffcc66', textvariable=titulos)
    e1.delete(0,"end")
    e1.config(font=('Microsoft YaHei UI Light',11, ))
    e1.bind("<FocusIn>", on_enter)
    e1.bind("<FocusOut>", on_leave)
    e1.insert(0,'Asunto')
    e1.place(x=50,y=28)

    Frame(w_crear,width=295,height=2,bg='black').place(x=50,y=50)
    
    s=ttk.Style()
    s.theme_use('clam')
    s.configure('my.DateEntry', background="#ffcc66",
                fieldbackground='#ffcc66',
                foreground='dark',
                arrowcolor='white')
    
    cal = DateEntry(w_crear,style='my.DateEntry', width=30, state='readonly', textvariable=fecha,fg="black", bg="#ffcc66", font=('Microsoft YaHei UI Light',11, ),border=0)
    cal.config(headersbackground='#FFB6C1',headersforeground='black',foreground='black',background='#20B2AA')
    cal.place(x=50,y=100)

    Frame(w_crear,width=295,height=2,bg='black').place(x=50,y=130)
    
    options = ['Estudio','Trámites','Trabajo','Otros']
    lista=ttk.Combobox(w_crear, value=options, width=30,font=('Microsoft YaHei UI Light',11, ), state='readonly', textvariable=categorias)
    lista.config(background="#ffcc66", foreground='black')
    lista.current(0)
    lista.place(x=50,y=172)

    Frame(w_crear,width=295,height=2,bg='black').place(x=50,y=200)
    
    def on_enter2(e):
        texto.delete(0,'end')    
    def on_leave2(e):
        if texto.get()=='':   
            texto.insert(0,'Descripción')
    
    texto = Entry(w_crear, width=25,fg='black',  textvariable=textos)
    texto.config(font=('Microsoft YaHei UI Light',11, ),border=0,bg="#ffcc66")
    texto.delete(0,"end")
    texto.bind("<FocusIn>", on_enter2)
    texto.bind("<FocusOut>", on_leave2)
    texto.insert(0,'Descripción')
    texto.place(x=50,y=254)
    
    Frame(w_crear,width=295,height=2,bg='black').place(x=50,y=280)
    
    correo = Entry(w_crear, width=25,fg='black',  textvariable=mail)
    correo.config(font=('Microsoft YaHei UI Light',11, ),border=0,bg="#ffcc66")
    correo.place(x=50,y=336)
    
    Frame(w_crear,width=295,height=2,bg='black').place(x=50,y=370)
    
    bttn(50,450,'E N V I A R','#EDEDDE','#141414', enviar_mail, w_crear)
    bttn(50,500,'G U A R D A R','#EDEDDE','#141414', createDB, w_crear)

"""
PANTALLA2
""" 
def w_ver():
    #FUNCIONES
    def mostrar_datos():
            guardar = Tabla.get_children() #obtener elementos de la tabla
            for element in guardar:
                Tabla.delete(element)
            i = conn_bbdd('SELECT id,fecha,titulo,categoria,descripcion FROM recordatorio')
            for row in i:
                Tabla.insert('',0,text='', values=row)
    def delete_data():
        select = Tabla.selection()
        c=messagebox.askquestion("Aviso","¿Desea borrar lo seleccionado?")
        if c=='yes':
            for records in select:
                    selected=(Tabla.set(records, '#1'))
                    i = conn_bbdd("DELETE FROM recordatorio WHERE id =('" + selected +"')")
                    print(i)
                    Tabla.delete(records)       
    def w_actualizar():
            def volver():
                up2.delete(0,'end')
                texto2.delete(0,'end')
                w_actualizar.destroy()
                
                
            #FUNCIONES
            def update():
                a = titulos2.get()
                b = fecha2.get()
                c =lista2.get()
                d=textos2.get()
                print(a, b, c, d)
                conn_bbdd("UPDATE recordatorio SET titulo =('" + a +"'), fecha=('"+ b + "'), descripcion=('"+ d +"'), categoria=('" + c +"') WHERE id =('"+ id_tabla +"')")    
            
            def combobox(value):
                options2 = value
                return value
    
    
            w_actualizar=Frame(root,width=400,height=600,bg='#FFB6C1')
            w_actualizar.place(x=0,y=28)
            w_actualizar.config(height=600)
            

              
            


            up2=Entry(w_actualizar,width=25,fg='black',border=0,bg='#FFB6C1', textvariable=titulos2)
            up2.config(font=('Microsoft YaHei UI Light',11, ))
            up2.place(x=50,y=28)
            
            
            Frame(w_actualizar,width=295,height=2,bg='black').place(x=50,y=50)
            
            s=ttk.Style()
            s.theme_use('clam')
            s.configure('my.DateEntry', background='#FFB6C1',
                        fieldbackground='#ffcc66',
                        foreground='dark',
                        arrowcolor='white')
            
            cal = DateEntry(w_actualizar,style='my.DateEntry', width=30, state='readonly', textvariable=fecha2,fg="black", bg="#ffcc66", font=('Microsoft YaHei UI Light',11, ),border=0)
            cal.config(headersbackground='#FFB6C1',headersforeground='black',foreground='black',background='#20B2AA')
            cal.place(x=50,y=100)

            Frame(w_actualizar,width=295,height=2,bg='black').place(x=50,y=130)
            
            

            
            texto2 = Entry(w_actualizar, width=25,fg='black',  textvariable=textos2)
            texto2.config(font=('Microsoft YaHei UI Light',11, ),border=0,bg='#FFB6C1')
            texto2.place(x=50,y=254)
            
            Frame(w_actualizar,width=295,height=2,bg='black').place(x=50,y=276)
            fin_op = None
            options = ('Estudio', 'Trámites', 'Examen', 'Otros')
            select = Tabla.selection()
            if not select:
                lista2=ttk.Combobox(w_actualizar, value=options, width=30,font=('Microsoft YaHei UI Light',11, ), state='readonly', textvariable=categorias2)
                pass
            else:
                print(select)
                for records in select:
                        selected=[]
                        id_tabla=Tabla.set(records, '#1')
                        selected.append(Tabla.set(records, '#2'))
                        selected.append(Tabla.set(records, '#3'))   
                        selected.append(Tabla.set(records, '#4'))   
                        selected.append(Tabla.set(records, '#5'))       
                        print(selected)
                up2.insert(0,selected[1])
                options2 = selected[2]
                texto2.insert(0,selected[3])
                
                options = ('Estudio', 'Trámites', 'Examen', 'Otros')
                options3 = []
                cont = 0
                for o in options:
                    
                    if o in options2:
                        options3.insert(0,options2)
                    else:
                        options3.append(o)
                    cont += 1
                fin_op = tuple(options3)
            
                lista2=ttk.Combobox(w_actualizar, value=fin_op, width=30,font=('Microsoft YaHei UI Light',11, ), state='readonly', textvariable=categorias2)
            lista2.config(background='#FFB6C1', foreground='black')
            lista2.place(x=50,y=172)
            lista2.current(0)

            Frame(w_actualizar,width=295,height=2,bg='black').place(x=50,y=200)
            
            
            
            bttn(50,450,'E N V I A R','#EDEDDE','#141414', update, w_actualizar)
            bttn(50,500,'V O L V E R','#EDEDDE','#141414',volver,w_actualizar)
            
            
            
            ##TERMINAR
            #FIN FUNCIONES
    #FIN FUNCIONES
    w_ver=Frame(root,width=400,height=600,bg='#FFB6C1')
    w_ver.place(x=0,y=28)
    
    #BOTONES
    bttn(50,50, "R E F R E S C A R",'#EDEDDE','#141414',mostrar_datos,w_ver  )
    bttn(50,110, "A C T U A L I Z A R",'#EDEDDE','#141414',w_actualizar,w_ver  )
    bttn(50,170, "B O R R A R",'#EDEDDE','#141414',delete_data,w_ver  )
    #FIN BOTONES
    
    #TABLA
    Tabla=ttk.Treeview(w_ver,height=12, columns=('#1','#2','#3','#4','#5'))
    Tabla.place(x=0,y=300)
    Tabla.heading('#0' , text="-", anchor="w")
    Tabla.heading('#1' , text="Id", anchor="w")
    Tabla.heading('#2' , text="Fecha", anchor=CENTER)
    Tabla.heading('#3', text="Título", anchor=CENTER)
    Tabla.heading('#4', text="Categoría", anchor="w")
    Tabla.heading('#5' , text="Descripción", anchor="w")
    Tabla.column("#0",stretch=False, width=1)
    Tabla.column("#1",stretch=False, width=1)
    Tabla.column("#2", width=200)
    Tabla.column("#3", width=200)
    Tabla.column("#4",stretch=False, width=1)
    Tabla.column("#5",stretch=False, width=1)
    #FIN TABLA
    mostrar_datos() 
    
    
"""
PANTALLA3
"""     

def w_enviar():
    w_enviar=Frame(root,width=400,height=600,bg='#20B2AA')
    w_enviar.place(x=0,y=28)



root=Tk()
root.geometry('400x600')
root.resizable(0,0)
root.title('Anotador')
root.iconbitmap('C:\\Users\\July\\Desktop\\Programación\\Python\\Apps\\App 2\\resources\\logo2.ico')



#Variables
categorias = ('Estudio', 'Trámites', 'Examen', 'Otros')
titulos=StringVar()
fecha=StringVar()
mail=StringVar()
textos=StringVar()

categorias2 = ('Estudio', 'Trámites', 'Examen', 'Otros')
titulos2=StringVar()
fecha2=StringVar()
textos2=StringVar()

def bttn(x,y,text,bcolor,fcolor,cmd, pantalla): 
     
    def on_entera(e):
        myButton1['background'] = bcolor 
        myButton1['foreground']= fcolor  

    def on_leavea(e):
        myButton1['background'] = fcolor
        myButton1['foreground']= bcolor

    myButton1 = Button(pantalla,text=text,
                   width=42,
                   height=2,
                   fg=bcolor,
                   border=0,
                   bg=fcolor,
                   activeforeground=fcolor,
                   activebackground=bcolor,            
                    command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)







Button(root,width=18,height=0,text='C R E A R',pady=4,command=w_crear,border=0,bg='#ffcc66',fg='white',activebackground='#EFAD29',activeforeground='white').place(x=0,y=0)
Button(root,width=19,height=0,text='V E R',pady=4,border=0,command=w_ver,bg='#FFB6C1',fg='white',activebackground='#DB7093',activeforeground='white').place(x=130,y=0)
Button(root,width=19,height=0,text='E N V I A R',pady=4,border=0,command=w_enviar,bg='#20B2AA',fg='white',activebackground='#008B8B',activeforeground='white').place(x=266,y=0)

w_crear()

root.mainloop()