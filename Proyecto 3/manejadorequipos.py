import numpy as np
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