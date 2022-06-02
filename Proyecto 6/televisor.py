from aparato import Aparato


class Televisor(Aparato):
    __tipoPantalla=''
    __pulgadas=''
    __tipoDefinicion=''
    __conexion=False
    def __init__(self,marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga,capacidadLitros,frezzer,ciclica,tipoPantalla,pulgadas,tipoDefinicion,conexion):
        super().__init__(self,marca,modelo,color,pais,precio,capacidadLavado,velocidadCentrifugado,cantiProgramas,tipoCarga,capacidadLitros,frezzer,ciclica,tipoPantalla,pulgadas,tipoDefinicion,conexion)
        self.__tipoPantalla
        self.__pulgadas
        self.__tipoDefinicion
        self.__conexion