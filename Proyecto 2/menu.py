from manejadorflores import ManejaFlores
from manejadorramo import ManejaRamo
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher= {'1':self.opcion1,
                          '2':self.opcion2,
                          '3':self.salir}
    def opcion(self,op,manejador):
        func=self.__switcher.get(op,lambda: print('Opcion no valida'))
        if(op=='1' or op=='2'):
            func(manejador)
        else:
            func()
    def opcion1(self,manejador):
        if(type(manejador)==ManejaRamo):
            manejador.Venta()
    def opcion2(self,manejador):
        if(type(manejador)==ManejaFlores):
            pass
    def salir(self):
        print('finalizado...')