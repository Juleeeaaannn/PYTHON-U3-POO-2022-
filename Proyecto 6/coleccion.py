from nodo import Nodo
class Lista:
    __comienzo=None
    def __init__(self):
        self.__comienzo=None
    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)