import numpy as np
from contrato import Contrato
class ManejaContrato:
    __dimension=10
    __cantidad=0
    __incremento=2
    def __init__(self):
        self.__contratos=np.empty(self.__dimension,dtype=Contrato)
    def agregar(self,contrato):
        if(self.__cantidad == self.__dimension):
            self.__dimension+=self.__incremento
            self.__contratos.resize(self.__dimension)
            self.__contratos[self.__cantidad]=contrato
            self.__cantidad+=1
        else:
            self.__contratos[self.__cantidad]=contrato
            self.__cantidad+=1