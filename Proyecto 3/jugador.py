from contrato import Contrato
from equipo import Equipo
class Jugador:
    __nombre=''
    __dni=''
    __ciudad=''
    __pais=''
    __fdenacimiento=''
    __contratos=[]
    def __init__(self,nombre,dni,ciudad,pais,fdenacimiento):
        self.__nombre=nombre
        self.__dni=dni
        self.__ciudad=ciudad
        self.__pais=pais
        self.__fdenacimiento=fdenacimiento
        self.__contratos=[]
    def crearContrato(self,fechai,fechaf,pago,equipo):
        contrato1=Contrato(fechai,fechaf,pago,self,equipo)
        self.__contratos.append(contrato1)
        equipo.agregarContrato(contrato1)