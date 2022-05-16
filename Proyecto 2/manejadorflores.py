import numpy as np
from flores import Flores
import csv
class ManejaFlores:
    __dimension=10
    __cantidad=0
    __incremento=2
    def __init__(self):
        self.__flores=np.empty(self.__dimension,dtype=Flores)
    def agregarFlor(self,flor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
            self.__flores[self.__cantidad]=flor #AGREGO UNA FLOR AL ARREGLO
            self.__cantidad += 1 #ACUMULO CANTIDAD DE FLORES
        else:
            self.__flores[self.__cantidad]=flor #AGREGO UNA FLOR AL ARREGLO
            self.__cantidad += 1 #ACUMULO CANTIDAD DE FLORES
    def LeerArchivo(self):
        archivo=open('flores.csv')
        reader=csv.reader(archivo, delimiter=',')
        for fila in reader:
            flor=Flores(int(fila[0]),fila[1],fila[2],fila[3])
            self.agregarFlor(flor)
        print('archivo leido')