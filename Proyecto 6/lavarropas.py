from aparato import Aparato


class Lavarropas(Aparato):
    __capacidadLitros=0
    __frezzer=False
    __ciclica=False
    def __init__(self,marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga,capacidadLitros,frezzer,ciclica):
        super().__init__(marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga,capacidadLitros,frezzer,ciclica)
        self.__capacidadLitros=capacidadLitros
        self.__frezzer=frezzer
        self.__ciclica=ciclica