from aparato import Aparato


class Heladera(Aparato):
    __capacidadLavado=''
    __velocidadCentrifugado=''
    __cantiProgramas=''
    __tipoCarga=''
    def __init__(self,marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga):
        super().__init__(marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga)
        self.__capacidadLavado=capacidadLavado
        self.__velocidadCentrifugado=velocidadCentrifugado
        self.__cantiProgramas=cantiProgramas
        self.__tipoCarga=tipoCarga