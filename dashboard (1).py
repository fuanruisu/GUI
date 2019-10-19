""""
Nombre:dashboard.py
Objetivo: Construye el menu principal de la aplicación
de la base de datos.
Autor: M. A. Ascencio Y. & Juan Luis Magaña Paz
Fecha: 10/10/19
"""

from tkinter import *
from tkinter import ttk


def clear_pantalla():
    clabel.pack()
    clabel.pack_forget()
    dlabel.pack()
    dlabel.pack_forget()
    plabel.pack()
    plabel.pack_forget()

    txtClave.pack()
    txtClave.pack_forget()
    txtDesc.pack()
    txtDesc.pack_forget()
    txtPrecio.pack()
    txtPrecio.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    btnEnviar.pack()
    btnEnviar.pack_forget()

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()
    mssss.pack()
    mssss.pack_forget()

    anii.pack()
    anii.pack_forget()
    alex.pack()
    alex.pack_forget()
    juan.pack_forget()

def clear_creditos():
    clabel.pack()
    clabel.pack_forget()
    dlabel.pack()
    dlabel.pack_forget()
    plabel.pack()
    plabel.pack_forget()

    txtClave.pack()
    txtClave.pack_forget()
    txtDesc.pack()
    txtDesc.pack_forget()
    txtPrecio.pack()
    txtPrecio.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    btnEnviar.pack()
    btnEnviar.pack_forget()

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()
    mssss.pack()
    mssss.pack_forget()

    btnEnviar.pack()
    btnEnviar.pack_forget()


def clear_agregar():
    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()
    mssss.pack()
    mssss.pack_forget()
    
    anii.pack()
    anii.pack_forget()
    alex.pack()
    alex.pack_forget()
    juan.pack()
    juan.pack_forget()

def clear_buscar():
    clabel.pack()
    clabel.pack_forget()
    plabel.pack()
    plabel.pack_forget() 

    txtPrecio.pack()
    txtPrecio.pack_forget()


    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    ms.pack()

    ms.pack_forget()
    msss.pack()
    msss.pack_forget()
    mssss.pack()
    mssss.pack_forget()
    
    anii.pack()
    anii.pack_forget()
    alex.pack()
    alex.pack_forget()
    juan.pack()
    juan.pack_forget()
def clear_cambiar():
    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    mssss.pack()
    mssss.pack_forget()
    
    anii.pack()
    anii.pack_forget()
    alex.pack()
    alex.pack_forget()
    juan.pack()
    juan.pack_forget()
def clear_borrar():
    clabel.pack()
    clabel.pack_forget()
    plabel.pack()
    plabel.pack_forget()

    txtDesc.pack()
    txtDesc.pack_forget()
    txtPrecio.pack()
    txtPrecio.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()

    anii.pack()
    anii.pack_forget()
    alex.pack()
    alex.pack_forget()
    juan.pack()
    juan.pack_forget()
def agregar():
    ms.place(x=130,y=0, width=200, height=30)

    clabel.place(x=40,y=50,width=100,height=30)
    dlabel.place(x=40,y=100,width=110,height=30)
    plabel.place(x=40,y=150,width=100,height=30)

    txtClave.place(x=180,y=50,width=100,height=30)
    txtDesc.place(x=180,y=100,width=100,height=30)
    txtPrecio.place(x=180,y=150,width=100,height=30)

    btnEnviar.place(x=180,y=200,width=100,height=30)

    clear_agregar()

def buscar():
    mss.place(x=130,y=0, width=200, height=30)

    dlabel.place(x=40,y=50,width=100,height=30)

    txtClave.place(x=180,y=50,width=100,height=30)

    btnEnviar.place(x=180,y=200,width=100,height=30)

    clear_buscar()
 
def cambiar():
    msss.place(x=130,y=0, width=200, height=30)

    clabel.place(x=40,y=50,width=100,height=30)
    dlabel.place(x=40,y=100,width=110,height=30)
    plabel.place(x=40,y=150,width=100,height=30)

    txtClave.place(x=180,y=50,width=100,height=30)
    txtDesc.place(x=180,y=100,width=100,height=30)
    txtPrecio.place(x=180,y=150,width=100,height=30)

    btnEnviar.place(x=180,y=200,width=100,height=30)

    clear_cambiar()

def borrar():
    mssss.place(x=130,y=0, width=200, height=30)

    dlabel.place(x=40,y=50,width=100,height=30)

    txtClave.place(x=180,y=50,width=100,height=30)

    btnEnviar.place(x=180,y=200,width=100,height=30)

    clear_borrar()

def creditos():
    anii.place(x=40,y=50,width=300,height=30)
    alex.place(x=40,y=100,width=300,height=30)
    juan.place(x=40,y=150,width=300,height=30)
    clear_creditos()


ventana=Tk()
ventana.geometry("400x300")

menubar=Menu(ventana)

menutrab=Menu(menubar,tearoff=0)
menutrab.add_command(label="Agregar",command=agregar)
menutrab.add_command(label="Buscar",command=buscar)
menutrab.add_command(label="Cambiar",command=cambiar)
menutrab.add_command(label="Borrar",command=borrar)
menubar.add_cascade(label="Trabajadores",menu=menutrab)

menurep=Menu(menubar,tearoff=0)
menurep.add_command(label="Pantalla",command="mensaje")
menurep.add_command(label="PDF", command="mensaje")
menubar.add_cascade(label="Reportes", menu=menurep)

menusalir=Menu(menubar,tearoff=0)
menusalir.add_command(label="Créditos",command=creditos)
menusalir.add_command(label="Salir",command=quit)
menubar.add_cascade(label="¿Quiénes somos?",menu=menusalir)

ventana.config(menu=menubar)

ms = Label(ventana, text ="Agregar")
mss= Label(ventana,text="Buscar")
msss= Label(ventana,text="Cambiar")
mssss= Label(ventana,text="Borrar")

anii= Label(ventana,text="Creadores")
alex= Label(ventana,text="Manuel Alejandro Ascencio Ysordia")
juan= Label(ventana,text="Juan Luis Magaña Paz")

# Creamos elementos gráficos
clabel = Label(ventana, text = "Nombre:")
dlabel = Label(ventana, text = "Clave:")
plabel = Label(ventana, text = "Sueldo:")

# Campos de texto
txtClave = ttk.Entry()
txtDesc =  ttk.Entry()
txtPrecio = ttk.Entry()

# Botones
btnEnviar = ttk.Button(text ="Enviar")


ventana.mainloop()

