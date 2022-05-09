from ast import Return
from carrera import Carrera
class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=0
    __carrera=[]
    def __init__(self,codigo,nombre,direccion,localidad,telefono,carrera=[]):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__carrera.append(carrera)
    def __str__(self):
        return('{} {} {} {} {}').format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono)