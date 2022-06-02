class Aparato:
    __marca=''
    __modelo=''
    __color=''
    __paisdefabricacion=''
    __preciobase=0.0
    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisdefabricacion=pais
        self.__preciobase=precio