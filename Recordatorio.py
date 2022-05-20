from ast import Continue
from msilib.schema import RemoveRegistry
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tokenize import String
from numpy import var 
from tkcalendar import Calendar, DateEntry 
from datetime import datetime
import time
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib




def Recordatorio():
    
    def createDB():
        try:
            conn = sqlite3.connect('recordatorios.db')
            c = conn.cursor()
                        
            c.execute("""
                    CREATE TABLE "recordatorio" (
                        "id"	INTEGER,
                        "titulo"	VARCHAR(30),
                        "fecha"	VARCHAR(15),
                        "categoria"	VARCHAR(15),
                        "descripcion"	VARCHAR(100),
                        PRIMARY KEY("id" AUTOINCREMENT)
                    )
                    """)
            messagebox.showinfo(Recordatorio, "Base de datos creada con éxito")
            conn.close()
        except:
        #if the count is 1, then table exists
            messagebox.showinfo(Recordatorio,'Ya existe una BBDD') 
        
    
    def clearTextInput():
        texto.delete("1.0","end")
        titulo.delete(0,"end")
        cal.delete(1)
        lista_desplegable.set('')

    def guardardatos():
        res = messagebox.askyesno('Pregunta', '¿Estás segura de guardar estos datos?')
        if res == True:
            a = titulo.get()
            b = fecha.get()
            c =(lista_desplegable.get())
            #VAR descripción
            descripcion=texto.get(1.0, END+"-1c")
            print(a, b, c, descripcion)
            conexion=sqlite3.connect("recordatorios.db")
            cursor=conexion.cursor()
            cursor.execute("INSERT INTO recordatorio VALUES(NULL,'" + a +
                            "','"+ b + "', '" + c +"', '"+ descripcion +"')")
            conexion.commit()
            conexion.close()
            clearTextInput()
        elif res == False:
            None
        
    def infoAdicional():
        messagebox.showinfo("Julian Decoppet", "Este programa fue hecho con todo\nmi amor y cariño.")
    def enviar_mail():
        # create message object instance
        msg = MIMEMultipart()
        
        a = str(titulos.get())
        b = fecha.get()
        c = (lista_desplegable.get())
        d = str(mail.get())
        
        #VAR descripción
        descripcion=texto.get(1.0, END+"-1c")
        message = f'Título: {a}\nCategoría: {c}\nMensaje: {descripcion}\nFecha: {b}'
        
        # setup the parameters of the message
        password = "anju1234"
        msg['From'] = 'testmail.app.notas@gmail.com'
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
      


    #Inicio
    Recor = Toplevel()
    Recor.title('Crear - Recordatorio')
    barraMenu=Menu(Recor)
    Recor.config(menu=barraMenu, background="#141414")
    
    #MENU
    archivoMenu=Menu(barraMenu, tearoff=0)
    archivoMenu.add_command(label="Crear BBDD", command=createDB)
    archivoMenu.add_command(label="Abrir")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Guardar")
    archivoMenu.add_command(label="Guardar como")

    archivo_edicionMenu=Menu(barraMenu, tearoff=0)

    archivo_herramientasMenu=Menu(barraMenu, tearoff=0)

    archivo_ayudaMenu=Menu(barraMenu, tearoff=0)
    
    
    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

    barraMenu.add_cascade(label="Edicion", menu=archivo_edicionMenu)

    barraMenu.add_cascade(label="Herramientas", menu=archivo_herramientasMenu)

    barraMenu.add_cascade(label="Ayuda", menu=archivo_ayudaMenu)
    
    archivo_ayudaMenu.add_command(label="Ayuda", command=infoAdicional)
    #FIN MENU
    
    #Variables
    categorias = ('Estudio', 'Trámites', 'Examen', 'Otros')
    titulos=StringVar()
    fecha=StringVar()
    mail=StringVar()
    """
    highlightbackground="black", Cuando desclickeas
    highlightcolor="#ffcc66" Cuando clickeas
    """
    #Label y entry
    Label(Recor, text="Título: ", background="#141414",fg="#ffcc66",font=('Microsoft YaHei UI Light',11, )).grid(row=1, column=0, sticky=W,padx = 20, pady = 20)
    titulo = Entry(Recor, textvariable=titulos,border=0,highlightthickness=2)
    titulo.config(font=('Microsoft YaHei UI Light',11, ), highlightbackground="black",highlightcolor="#ffcc66")
    titulo.grid(row=1,column=1, sticky=W+E,padx = 20, pady = 20)
    
    
    

    #Fecha
    Label(Recor, text="Fecha: ", background="#141414",fg="#ffcc66",font=('Microsoft YaHei UI Light',11, )).grid(row=2, column=0, sticky=W,padx = 20, pady = 20)

    cal = DateEntry(Recor, width=18, state='readonly', textvariable=fecha, background="#141414", font=('Microsoft YaHei UI Light',11, ),border=0,highlightthickness=2)
    cal.grid(row=2, column=1, sticky=W+E,padx = 20, pady = 20)
    cal.config(headersbackground='#364c55',headersforeground='#fff',foreground='#009',background='#fff')

    Label(Recor, text="Categoria: ", background="#141414",fg="#ffcc66",font=('Microsoft YaHei UI Light',11, )).grid(row=3, column=0, sticky=W,padx = 20, pady = 20)
    
    #COMBOBOX
    lista_desplegable=ttk.Combobox(Recor, state="readonly", font=('Microsoft YaHei UI Light',11, ))
    lista_desplegable.grid(row=3, column=1, sticky=W+E,padx = 20, pady = 20)
    lista_desplegable["values"] = categorias

    Label(Recor, text="Descripción: ", background="#141414",fg="#ffcc66",font=('Microsoft YaHei UI Light',11, )).grid(row=4, column=0, sticky=W,padx = 20, pady = 20)
    texto = Text(Recor, height=10)
    texto.config(font=('Microsoft YaHei UI Light',11, ),border=0,highlightthickness=2, highlightbackground="black",highlightcolor="#ffcc66")
    texto.grid(row=4,column=1, sticky=W+E,padx = 20, pady = 20)

    #MAIL
    Label(Recor, text="Mail - opcional: ", background="#141414",fg="#ffcc66",font=('Microsoft YaHei UI Light',11, )).grid(row=5, column=0, sticky=W,padx = 20, pady = 20)
    correo = Entry(Recor, textvariable=mail,border=0,highlightthickness=2)
    correo.config(font=('Microsoft YaHei UI Light',11, ), highlightbackground="black",highlightcolor="#ffcc66")
    correo.grid(row=5,column=1, sticky=W+E,padx = 20, pady = 20)

    # botón
    button1=Button(Recor, text="Guardar", command=guardardatos, background="#141414", fg="#ffcc66").grid(row=7, sticky=W+E, column=1, pady=10, padx=20)
    button2=Button(Recor, text="Enviar mail", command=enviar_mail, background="#141414", fg="#ffcc66").grid(row=7, sticky=W+E, column=0, pady=10, padx=20)

    #BIND BOTONES

    Recor.mainloop()