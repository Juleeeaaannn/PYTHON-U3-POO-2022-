import numpy as np
from flores import Flores
class ManejaFlores:
    __dimension=10
    __cantidad=0
    __incremento=0
    def __init__(self):
        self.__flores=np.empty(self.__dimesion,dtype=Flores)
    def agregarFlor(self,flor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
            self.__flores[self.__cantidad]=flor #AGREGO UNA FLOR AL ARREGLO
            self.__cantidad += 1 #ACUMULO CANTIDAD DE FLORES