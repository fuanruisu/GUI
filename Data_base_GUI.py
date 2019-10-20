""""
Nombre:dashboard.py
Objetivo: Construye el menu principal de la aplicación
de la base de datos.
Autor: M. A. Ascencio Y.
Fecha: 10/10/19
"""
from tkinter import *
from tkinter import ttk
import pymysql

agr=[]
bus=[]
cam=[]
borr=[]
azar=['Alex',2,3]

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
    txtbuscar.pack()
    txtbuscar.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')
    txtbuscar.delete(0, 'end')

    txtnuevo.pack()
    txtnuevo.pack_forget()
    txtnuevo.delete(0,'end')
    nuevo.pack()
    nuevo.pack_forget()

    btnEnviar.pack()
    btnEnviar.pack_forget()
    btnEnviar1.pack()
    btnEnviar1.pack_forget()
    btnEnviar2.pack()
    btnEnviar2.pack_forget()
    btnEnviar3.pack()
    btnEnviar3.pack_forget()


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
    txtbuscar.delete(0, 'end')
    txtbuscar.pack()
    txtbuscar.pack_forget()

    txtnuevo.pack()
    txtnuevo.pack_forget()
    txtnuevo.delete(0,'end')
    nuevo.pack()
    nuevo.pack_forget()


    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()
    mssss.pack()
    mssss.pack_forget()
    
    btnEnviar1.pack()
    btnEnviar1.pack_forget()
    btnEnviar2.pack()
    btnEnviar2.pack_forget()
    btnEnviar3.pack()
    btnEnviar3.pack_forget()


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

    txtClave.pack()
    txtClave.pack_forget()
    txtDesc.pack()
    txtDesc.pack_forget()
    txtPrecio.pack()
    txtPrecio.pack_forget()

    txtnuevo.pack()
    txtnuevo.pack_forget()
    txtnuevo.delete(0,'end')
    nuevo.pack()
    nuevo.pack_forget()

    btnEnviar.pack()
    btnEnviar.pack_forget()
    btnEnviar2.pack()
    btnEnviar2.pack_forget()
    btnEnviar3.pack()
    btnEnviar3.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')
    txtbuscar.delete(0, 'end')

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
    txtnuevo.delete(0,'end')
    txtbuscar.delete(0, 'end')

    txtbuscar.pack()
    txtbuscar.pack_forget()

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    mssss.pack()
    mssss.pack_forget()
    
    btnEnviar1.pack()
    btnEnviar1.pack_forget()
    btnEnviar.pack()
    btnEnviar.pack_forget()
    btnEnviar3.pack()
    btnEnviar3.pack_forget()
    
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

    txtClave.pack()
    txtClave.pack_forget()
    txtPrecio.pack()
    txtPrecio.pack_forget()
    txtbuscar.pack()
    txtbuscar.pack_forget()

    txtClave.delete(0, 'end')
    txtDesc.delete(0, 'end')
    txtPrecio.delete(0, 'end')
    txtbuscar.delete(0, 'end')

    txtnuevo.pack()
    txtnuevo.pack_forget()
    txtnuevo.delete(0,'end')
    nuevo.pack()
    nuevo.pack_forget()

    ms.pack()
    ms.pack_forget()
    mss.pack()
    mss.pack_forget()
    msss.pack()
    msss.pack_forget()

    btnEnviar.pack()
    btnEnviar.pack_forget()
    btnEnviar1.pack()
    btnEnviar1.pack_forget()
    btnEnviar2.pack()
    btnEnviar2.pack_forget()

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

    txtbuscar.place(x=180,y=50,width=100,height=30)

    btnEnviar1.place(x=180,y=200,width=100,height=30)

    clear_buscar()
 
def cambiar():
    msss.place(x=130,y=0, width=200, height=30)

    clabel.place(x=40,y=50,width=100,height=30)
    dlabel.place(x=40,y=100,width=110,height=30)
    plabel.place(x=40,y=150,width=100,height=30)
    nuevo.place(x=40,y=200,width=100,height=30)

    txtClave.place(x=180,y=50,width=100,height=30)
    txtDesc.place(x=180,y=100,width=100,height=30)
    txtPrecio.place(x=180,y=150,width=100,height=30)
    txtnuevo.place(x=180,y=200,width=100,height=30)
    btnEnviar2.place(x=180,y=250,width=100,height=30)

    clear_cambiar()

def borrar():
    mssss.place(x=130,y=0, width=200, height=30)

    dlabel.place(x=40,y=50,width=100,height=30)

    txtDesc.place(x=180,y=50,width=100,height=30)

    btnEnviar3.place(x=180,y=200,width=100,height=30)

    clear_borrar()

def creditos():
    anii.place(x=40,y=50,width=300,height=30)
    alex.place(x=40,y=100,width=300,height=30)
    juan.place(x=40,y=150,width=300,height=30)
    clear_creditos()

def datosagregar():
    agr.append(txtClave.get())
    agr.append(txtDesc.get())
    agr.append(txtPrecio.get())
    #Limpiar pantalla
    
    #Obtención de clave, nombre, y sueldo
    clave=agr[1]
    nombre=agr[0]
    sueldo=agr[2]
    #inicialización para guardar en base de datos mysql
    db= pymysql.connect("localhost","root","","crudpython")
    #prepare a cursor object using cursor() method
    cursor = db.cursor()
    #sqlcad="INSERT INTO empleados(clave,nombre,sueldo) VALUES "+"("+clave+","+"'"+nombre+"'"+","+sueldo+");"
    sql = "INSERT INTO empleados (clave, nombre,sueldo) VALUES (%s, %s,%s)"
    val = (clave,nombre,sueldo)
    #Ejecuta el SQL query usando el metodo execute().
    cursor.execute(sql,val)
    #commit your changes in the database
    db.commit()

    print("Operación realizada...")

    #desconecta del servidor
    db.close()  
    n=len(agr)
    for i in range(n):
        agr.pop(0)


      

def datoscambiar():
    cam.append(txtClave.get())
    cam.append(txtDesc.get())
    cam.append(txtPrecio.get())
    cam.append(txtnuevo.get())
    nclave=cam[1]
    nnombre=cam[0]
    nsueldo=cam[2]
    clave=cam[3]
    db= pymysql.connect("localhost","root","","crudpython")
    cursor = db.cursor()


    sql="UPDATE `empleados` SET `clave`=%s,`nombre`=%s,`sueldo`=%s WHERE clave=%s;"
    val=(nclave,nnombre,nsueldo,clave)
    cursor.execute(sql,val)
    
    #commit your changes in the database
    db.commit()
    db.close()
    print("Operacion realizada!")
    n=len(cam)
    for i in range(n):
        cam.pop(0)



def datosbucar():
    a=int(entrada.get())
    db= pymysql.connect("localhost","root","","crudpython")

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    sqlcad="SELECT * FROM empleados WHERE clave=%s;"
    
    #Ejecuta el SQL query usando el metodo execute().
    cursor.execute(sqlcad,a)
    #commit your changes in the database
    db.commit()
    resultado = cursor.fetchall()
    for row in resultado:
        clave = row[0]
        nombre = row[1]
        sueldo = row[2]
        

    #desconecta del servidor
    db.close()


    print(a)
    ventana2=Tk()
    ventana2.geometry("300x300")

    datblabel= Label(ventana2,text="Datos del trabajador buscado")
    nmlabel = Label(ventana2, text = "Nombre:")
    nclabel = Label(ventana2, text = "Clave:")
    nslabel = Label(ventana2, text = "Sueldo:")

    datblabel.place(x=90,y=0, width=200, height=30)
    nmlabel.place(x=40,y=50,width=100,height=30)
    nclabel.place(x=40,y=100,width=110,height=30)
    nslabel.place(x=40,y=150,width=100,height=30)

    txtNom=ttk.Entry(ventana2)
    txtClav=ttk.Entry(ventana2)
    txtSuel=ttk.Entry(ventana2)


    txtNom.insert(0,nombre)
    txtClav.insert(0,clave)
    txtSuel.insert(0,sueldo)

    txtNom.place(x=140,y=50,width=100,height=30)
    txtClav.place(x=140,y=100,width=100,height=30)
    txtSuel.place(x=140,y=150,width=100,height=30)
    
def datosborrar():
    borr.append(txtDesc.get())
    
    db= pymysql.connect("localhost","root","","crudpython")
    cursor = db.cursor()

    clave=borr[0]
    
    sql="DELETE FROM `empleados` WHERE clave=%s;"
    val=(clave)
    cursor.execute(sql,val)
    
    #commit your changes in the database
    db.commit()
    db.close()
    borr.pop(0)



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
nuevo  = Label(ventana, text = "Clave anterior:")
# Campos de texto
txtClave = ttk.Entry(ventana)
txtDesc =  ttk.Entry(ventana)
txtPrecio = ttk.Entry(ventana)
txtnuevo= ttk.Entry(ventana)

entrada= StringVar()
txtbuscar= ttk.Entry(ventana,textvariable=entrada)

# Botones
btnEnviar = ttk.Button(text ="Enviar",command=datosagregar)
btnEnviar1= ttk.Button(text ="Enviar",command=datosbucar)
btnEnviar2= ttk.Button(text ="Enviar",command=datoscambiar)
btnEnviar3= ttk.Button(text ="Enviar",command=datosborrar)

ventana.mainloop()

def main():
    print(agr)
    print(bus)
    print(cam)
    print(borr)
    print(datosbucar())

if __name__ == "__main__":
    main()

