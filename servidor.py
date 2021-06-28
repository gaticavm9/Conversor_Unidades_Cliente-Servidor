#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Programa Servidor

import socket
import sys
import pint
import os

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('0.0.0.1', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if len(sys.argv) != 2:
    print ("Agregar el puerto donde se va a ofrecer el servicio desarrollado.")
    sys.exit(0)

IP = get_ip()  
PUERTO = int(sys.argv[1])

print ("\nServicio se va a configurar en el puerto: ", PUERTO, "en el servidor ", IP, "\n")

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlace del socket con la IP y el puerto
socket_servidor.bind((IP, PUERTO))

# Escuchar conexiones entrantes con el metodo listen,
# El parametro indica el numero de conexiones entrantes que vamos a aceptar
socket_servidor.listen(2)

print ("Servicio configurado en puerto ", PUERTO, "en el servidor ", IP)

try:
    while True:
        print ("Esperando conexión de un cliente ...")
        # Instanciar objeto socket_cliente para recibir datos,
        # direccion_cliente recibe la tupla de conexion: IP y puerto
        socket_cliente, direccion_cliente = socket_servidor.accept()
        print ("Cliente conectado desde: ", direccion_cliente)
        

        while True:
            try:
                tipo = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >>1 ", tipo)

                cant = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >>2 ", cant)
                cantidad=float(cant)

                desde = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >>3 ", desde)


                if tipo == "1": 
                             if   desde == "1": medida=cantidad*ureg.cm
                             elif desde == "2": medida=cantidad*ureg.meter
                             elif desde == "3": medida=cantidad*ureg.km
                             elif desde == "4": medida=cantidad*ureg.inch
                             elif desde == "5": medida=cantidad*ureg.foot
                             elif desde == "6": medida=cantidad*ureg.yard
                             elif desde == "7": medida=cantidad*ureg.mile
                             else             : print('error')
                elif tipo == "2":
                             if   desde == "1": medida=cantidad*ureg.cm**2
                             elif desde == "2": medida=cantidad*ureg.meter**2
                             elif desde == "3": medida=cantidad*ureg.hectare
                             elif desde == "4": medida=cantidad*ureg.km**2
                             elif desde == "5": medida=cantidad*ureg.inch**2
                             elif desde == "6": medida=cantidad*ureg.foot**2
                             elif desde == "7": medida=cantidad*ureg.acre
                             elif desde == "8": medida=cantidad*ureg.mile**2
                             else             : print('error') 
                elif tipo == "3":
                             if   desde == "1": medida=cantidad*ureg.liter
                             elif desde == "2": medida=cantidad*ureg.cc
                             elif desde == "3": medida=cantidad*ureg.gallon
                             else             : print('error') 
                elif tipo == "4": 
                             if   desde == "1": medida=cantidad*ureg.gram
                             elif desde == "2": medida=cantidad*ureg.kg
                             elif desde == "3": medida=cantidad*ureg.ounce
                             elif desde == "4": medida=cantidad*ureg.pound
                             else             : print('error') 
                elif tipo == "5": 
                             if   desde == "1": medida=Q_(cantidad, ureg.degC)
                             elif desde == "2": medida=Q_(cantidad, ureg.degF)
                             elif desde == "3": medida=Q_(cantidad, ureg.kelvin)
                             else             : print('error') 
                else:
                            print('error')
                print(medida)

                ##Conversion
                hacia = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >>4 ", hacia)

                if tipo == "1": 
                             if   hacia == "1": medidaC=medida.to(ureg.cm)
                             elif hacia == "2": medidaC=medida.to(ureg.meter)
                             elif hacia == "3": medidaC=medida.to(ureg.km)
                             elif hacia == "4": medidaC=medida.to(ureg.inch)
                             elif hacia == "5": medidaC=medida.to(ureg.foot)
                             elif hacia == "6": medidaC=medida.to(ureg.yard)
                             elif hacia == "7": medidaC=medida.to(ureg.mile)
                             else             : print('error')
                elif tipo == "2":
                             if   hacia == "1": medidaC=medida.to(ureg.cm**2)
                             elif hacia == "2": medidaC=medida.to(ureg.meter**2)
                             elif hacia == "3": medidaC=medida.to(ureg.hectare)
                             elif hacia == "4": medidaC=medida.to(ureg.km**2)
                             elif hacia == "5": medidaC=medida.to(ureg.inch**2)
                             elif hacia == "6": medidaC=medida.to(ureg.foot**2)
                             elif hacia == "7": medidaC=medida.to(ureg.acre)
                             elif hacia == "8": medidaC=medida.to(ureg.mile**2)
                             else             : print('error') 
                elif tipo == "3":
                             if   hacia == "1": medidaC=medida.to(ureg.liter)
                             elif hacia == "2": medidaC=medida.to(ureg.cc)
                             elif hacia == "3": medidaC=medida.to(ureg.gallon)
                             else             : print('error') 
                elif tipo == "4": 
                             if   hacia == "1": medidaC=medida.to(ureg.gram)
                             elif hacia == "2": medidaC=medida.to(ureg.kg)
                             elif hacia == "3": medidaC=medida.to(ureg.ounce)
                             elif hacia == "4": medidaC=medida.to(ureg.pound)
                             else             : print('error') 
                elif tipo == "5": 
                             if   hacia == "1": medidaC=medida.to('degC')
                             elif hacia == "2": medidaC=medida.to('degF')
                             elif hacia == "3": medidaC=medida.to('kelvin')
                             else             : print('error') 
                else:
                            print('error')
                print(medidaC)


                #Envio
                respuesta_servidor = str(medidaC)
                socket_cliente.send(respuesta_servidor.encode("utf-8"))


                continuar = socket_cliente.recv(1024).decode('utf-8')
                print (direccion_cliente[0] + " >>C ", continuar)

                if continuar == "2":
                    print ("Cliente finalizo la conexion.")
                    print ("Cerrando la conexion con el cliente ...")
                    socket_cliente.close()
                    print ("Conexion con el cliente cerrado.")
                    break
                
            except socket.error:
                print ("Conexion terminada abruptamente por el cliente.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break
            except KeyboardInterrupt:
                print ("\n∫Se interrunpio el cliente con un Control_C.")
                print ("Cerrando conexion con el cliente ...")
                socket_cliente.close()
                print ("Conexion con el cliente cerrado.")
                break

except KeyboardInterrupt:
    print ("\nSe interrumpio el servidor con un Control_C.")
    #socket_cliente.close()
    print ("Cerrando el servicio ...")
    socket_servidor.close()
    print ("Servicio cerrado, Adios!")
