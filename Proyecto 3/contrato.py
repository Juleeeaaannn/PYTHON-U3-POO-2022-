class Contrato:
    __fdeinicio=''
    __fdefinalizacion=''
    __pagomensual=0.0
    __jugador=None
    __equipo=None
    def __init__(self,fdeinicio,fdefinalizacion,pagomensual,jugador,equipo):
        self.__fdeinicio=fdeinicio
        self.__fdefinalizacion=fdefinalizacion
        self.__pagomensual=pagomensual
        self.__equipo=equipo
        self.__jugador=jugador
        