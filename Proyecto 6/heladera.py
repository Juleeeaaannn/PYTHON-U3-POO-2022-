from pyrsistent import freeze
from aparato import Aparato


class Heladera(Aparato):
    __capacidadLitros=0
    __frezzer=False
    __ciclica=False
    def __init__(self,marca,modelo,color,pais,precio,capacidadLitros,frezzer,ciclica):
        super().__init__(marca,modelo,color,pais,precio,capacidadLitros,frezzer,ciclica)
        self.__capacidadLitros=capacidadLitros
        self.__frezzer=frezzer
        self.__ciclica=ciclica
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                capacidadLitros=self.__capacidadLitros,
                freezer=self.__frezzer,
                ciclica=self.__ciclica
                )
                )
        return d