import numpy as np
from datetime import timedelta, datetime
import csv
from equipo import Equipo
class ManejaEquipo:
    __dimension=10
    __cantidad=0
    __incremento=2
    def __init__(self):
        self.__equipos=np.empty(self.__dimension,dtype=Equipo)
    def agregar(self,equipo):
        if(self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__equipos.resize(self.__dimension)
            self.__equipos[self.__cantidad]=equipo
            self.__cantidad+=1
        else:
            self.__equipos[self.__cantidad]=equipo
            self.__cantidad+=1
    def LeerArchivo(self):
        archivo=open("equipos.csv")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            equipo1=Equipo(fila[0],fila[1])
            self.agregar(equipo1)
    def mostrarEquipos(self):
        print('----------------Equipos----------------')
        for i in self.__equipos:
            print(i.getNombre())
    def Buscar(self,equipo):
        i=0
        retorna=None
        while(i<len(self.__equipos) and equipo!=self.__equipos[i].getNombre()):
            i+=1
        if(i<len(self.__equipos)):
            retorna=self.__equipos[i]
        else:print('Equipo no econtrado!')
        return retorna
    def ConsultarContratos(self):
        id=input('Ingrese Nombre del equipo:')
        equipo=self.Buscar(id)
        lista=equipo.getContratos()
        if(len(lista)==0):
            print('El equipo no tiene contratos con ningun jugador')
        else:    
            for i in equipo.getContratos():    
                print(i.getJugador())