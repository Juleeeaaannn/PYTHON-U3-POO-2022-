class Flores:
    __numero=0
    __nombre=''
    __color=''
    __descipcion=''
    def __init__(self,numero,nombre,color,descripcion):
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descipcion=descripcion
    def __str__(self):
        return('{}  {} {} {}').format(self.__numero,self.__color,self.__nombre,self.__descipcion)