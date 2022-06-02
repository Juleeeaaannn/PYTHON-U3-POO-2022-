from zope.interface import implementer
from aparato import Aparato
#from ej5 import Interface
from nodo import Nodo
class Lista():
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def instertarElemento(self,posicion,elemento):
        pass
    def agregarElemento(self,elemento):
        #para agregar un elemento al final de una colección
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__actual=nodo
        self.__tope+=1
    def mostrarElemento(self):
        try:
            cont=0
            id=input('Ingrese posicion de el elemento que desea encontrar:')
            aux = self.__comienzo
            while aux!=None:
                if(self.__contador==id):
                    print(aux.getDato())
                    aux=None
                else:
                    aux=aux.getSiguiente()
        except SyntaxError:
            print('Ingrese una posicion correcta en el arreglo!')
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            aparatos=[aparato.toJSON() for aparato in self]
            )
        return d