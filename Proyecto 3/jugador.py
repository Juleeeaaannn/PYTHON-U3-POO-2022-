class Jugador:
    __nombre=''
    __dni=''
    __ciudad=''
    __pais=''
    __fdenacimiento=''
    #Variales de clase
    __fdeinicio=''
    __fdefinalizacion=''
    def __init__(self,nombre,dni,ciudad,pais,fdenacimiento):
        self.__nombre=nombre
        self.__dni=dni
        self.__ciudad=ciudad
        self.__pais=pais
        self.__fdenacimiento=fdenacimiento