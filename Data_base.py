""" Nombre: Data_base.py
Objetivo: codigo CRUD para operar base de datos
Autor: Juan Luis Magaña Paz & M. A. Ascencio Y.
Fecha: 27 de agosto de 2019
"""
import pymysql
import os
def main():
    os.system("cls")
    print("1)Crear\n2)Leer\n3)Actualizar\n4)Eliminar\n5)Exit")
    x=int(input("¿Que desea hacer?\n"))
    
    if(x==1):
        create()
    elif(x==2):
        read()
    elif(x==3):
        update()
    elif(x==4):
        delete()
    elif(x==5):
        exit
        os.system("cls")
    
        
def create():
  #captura de numero de empleados
    empleados=int(input("Número de empleados:\n"))    
    #for que se repite tantas veces como numeros de empleados hay
    for i in range(empleados):
        #Limpiar pantalla
        os.system("cls")
        #Obtención de clave, nombre, y sueldo
        clave=(input("Clave: \n"))
        nombre=(input("Nombre: \n"))
        sueldo=(input("Sueldo: \n"))
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
    
def read():
    os.system("cls")
    db= pymysql.connect("localhost","root","","crudpython")

    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    sqlcad="SELECT * FROM empleados;"
    #Ejecuta el SQL query usando el metodo execute().
    cursor.execute(sqlcad)
    #commit your changes in the database
    db.commit()
    resultado = cursor.fetchall()
    for row in resultado:
        clave = row[0]
        nombre = row[1]
        sueldo = row[2]
        #Now print fetched result
        print("id={0},nombre={1},sueldo={2}".format(clave,nombre,sueldo))

    #desconecta del servidor
    db.close()

def update():
    os.system("cls")
    db= pymysql.connect("localhost","root","","crudpython")
    cursor = db.cursor()

    clave=int(input("Ingrese el numero de clave del registro a actualizar\n"))
    os.system("cls")
    nclave=input("Ingrese la nueva clave\n")
    nnombre=input("Ingrese el nuevo nombre\n")
    nsueldo=input("Ingrese el nuevo sueldo\n")
    sql="UPDATE `empleados` SET `clave`=%s,`nombre`=%s,`sueldo`=%s WHERE clave=%s;"
    val=(nclave,nnombre,nsueldo,clave)
    cursor.execute(sql,val)
    os.system("cls")
    #commit your changes in the database
    db.commit()
    db.close()

def delete():
    os.system("cls")
    db= pymysql.connect("localhost","root","","crudpython")
    cursor = db.cursor()

    clave=int(input("Ingrese el numero de clave del registro a eliminar\n"))
    os.system("cls")
    sql="DELETE FROM `empleados` WHERE clave=%s;"
    val=(clave)
    cursor.execute(sql,val)
    os.system("cls")
    #commit your changes in the database
    db.commit()
    db.close()
if __name__=="__main__":
    main()
