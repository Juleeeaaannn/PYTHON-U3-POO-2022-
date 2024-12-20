from zope.interface import implementer
from Manejador import Manejador as MJ
from objectencoder import ObjectEncoder as Encoder
from interface import IDirector,ITesorero

@implementer(IDirector)
@implementer(ITesorero)
def tesorero(manejaTesorero:ITesorero):
    print('-------TESORERO-------')
    manejaTesorero.gastosSueldoPorEmpleado()
def director(manejaTesorero:IDirector):
    print('-------DIRECTOR-------')
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher={'1':self.opcion1,
                         '2':self.opcion2,
                         '3':self.opcion3,
                         '4':self.opcion4,
                         '5':self.opcion5,
                         '6':self.opcion6,
                         '7':self.opcion7,
                         '8':self.opcion8,
                         '9':self.opcion9,
                         '10':self.salir}
    def opcion(self,op,Manejador,JSONF):
        func=self.__switcher.get(op,lambda:'opcion incorrecta!')
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7' or op=='8' or op=='9'):
            func(Manejador,JSONF)
        else:
            func()
    def opcion1(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            print('-----------Insertar personal-----------')
            Manejador.punto1()
    def opcion2(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            Manejador.punto2()
    def opcion3(self,Manejador,JSONF):
        if(type(Manejador)==MJ):
            Manejador.punto3()
    def opcion4(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto4()
    def opcion5(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto5()
    def opcion6(self,Manejador,JSONF):
        if(type(Manejador)==MJ,JSONF):
            Manejador.punto6()
    def opcion7(self,Manejador,JSONF):
        if(type(Manejador)==MJ and type(JSONF)==Encoder):
            Manejador.punto7()
    def opcion8(self,Manejador,JSONF):
        if(type(Manejador)==MJ and type(JSONF)==Encoder):
            d=Manejador.toJSON()
            JSONF.guardarJSONArchivo(d,'personal.json')
            print('ARCHIVO SUBIDO!')
    def opcion9(self,Manejador,JSONF):
        if(type(Manejador)==MJ and type(JSONF)==Encoder):
            u=input('Ingrese usuario:')
            c=input('Ingrese contraseña:')
            if(u=='uTesoreso' and c=='ag@74ck'):
                tesorero(ITesorero(Manejador))
            elif(u=='uDirector' and c=='ufC77#!1'):
                director(IDirector(Manejador))
            else:
                print('Error de usuario y contraseña')
    def salir(self):
        print('saliendo...')
