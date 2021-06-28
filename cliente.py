#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa Cliente

import socket
import sys
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if len(sys.argv) != 3:
    print ("Agregar la IP del servidor y el puerto donde se ofrece el servicio.")
    sys.exit(0)

IP = sys.argv[1]
PUERTO = int(sys.argv[2])

print ("\nConectandose al servidor ", IP, " en el puerto ", PUERTO, " ...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((IP, PUERTO))
except:
    print ("No se puede conectar con el servidor.", IP, " en el puerto ", PUERTO)
    sys.exit(0)

print ("\nConectado, escriba finalizar() para terminar la conección.\n")

try:
    while True:
        fin="finalizar()"
        clear()
        print ("############### Bienvenido al conversor de unidades ###############")
        print ("Seleccione el tipo de conversor:")
        print ("1.Longitud 2.Area 3.Volumen 4.Peso 5.Temperatura") 
        tipo = str(input("\nIngrese el número de la opción >> "))
        socket_cliente.send(tipo.encode("utf-8"))
        #Cantidad
        clear()
        print ("Ingrese la cantidad a convertir")
        cantidad = str(input("Cantidad: "))
        socket_cliente.send(cantidad.encode("utf-8"))
        #Desde
        clear()
        print ("Seleccione la unidad de inicio")
        if tipo == "1": 
                     print ("1.centímetros 2.metros 3.kilómetros 4.pulgadas 5.pies 6.yardas 7.millas")
                     desde = str(input("Ingrese opción: "))
                     socket_cliente.send(desde.encode("utf-8"))
        elif tipo == "2": 
                     print ("1.centímetros² 2.metros² 3.hectáreas 4.kilómetros² 5.pulgadas² 6.pies² 7.acres 8.millas²")
                     desde = str(input("Ingrese opción: "))
                     socket_cliente.send(desde.encode("utf-8"))
        elif tipo == "3": 
                     print ("1.litros 2.cc 3.galones")
                     desde = str(input("Ingrese opción: "))
                     socket_cliente.send(desde.encode("utf-8"))
        elif tipo == "4": 
                     print ("1.gramos 2.kilogramos 3.onzas 4.libras")
                     desde = str(input("Ingrese opción: "))
                     socket_cliente.send(desde.encode("utf-8"))
        elif tipo == "5": 
                     print ("1.Centígrados 2.Fahrenheit")
                     desde = str(input("Ingrese opción: "))
                     socket_cliente.send(desde.encode("utf-8"))
        else:
                    print('error')

        #Hacia
        print ("  ")
        print ("Seleccione la unidad final")
        if tipo == "1": 
                     print ("1.centímetros 2.metros 3.kilómetros 4.pulgadas 5.pies 6.yardas 7.millas")
                     hacia = str(input("Ingrese opción: "))
                     socket_cliente.send(hacia.encode("utf-8"))
        elif tipo == "2": 
                     print ("1.centímetros² 2.metros² 3.hectáreas 4.kilómetros² 5.pulgadas² 6.pies² 7.acres 8.millas²")
                     hacia = str(input("Ingrese opción: "))
                     socket_cliente.send(hacia.encode("utf-8"))
        elif tipo == "3": 
                     print ("1.litros 2.cc 3.galones")
                     hacia = str(input("Ingrese opción: "))
                     socket_cliente.send(hacia.encode("utf-8"))
        elif tipo == "4": 
                     print ("1.gramos 2.kilogramos 3.onzas 4.libras")
                     hacia = str(input("Ingrese opción: "))
                     socket_cliente.send(hacia.encode("utf-8"))
        elif tipo == "5": 
                     print ("1.Centígrados 2.Fahrenheit")
                     hacia = str(input("Ingrese opción: "))
                     socket_cliente.send(hacia.encode("utf-8"))
        else:
                    print('error')

        #Devolucion de resultado
        clear()  
        recibido = socket_cliente.recv(1024).decode('utf-8')
        print ("Resultado de la conversión: " + recibido)

        #Opcion de continuar
        print('\n\nSeleccione una opcion para continuar')
        print('1.Volver a usar          2.Salir')
        continuar = str(input("\nIngrese opción: "))
        socket_cliente.send(continuar.encode("utf-8"))

        if continuar == "2": 
                         clear()  
                         print('Cerrando...')
                         #socket_cliente.send(fin.encode("utf-8"))
                         break
            

except socket.error:
    print ("Se perdio la conexion con el servidor.")
except KeyboardInterrupt:
    print ("\nSe interrunpio el cliente con un Control_C.")

finally:
    print ("Terminando conexion con el servidor ...")
    socket_cliente.close()
    print ("Conexion con el servidor terminado.")
