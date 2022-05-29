class Equipo:
    __nombre=''
    __ciudad=''
    __contratos=[]
    def __init__(self,nombre,ciudad):
        self.__nombre=nombre
        self.__ciudad=ciudad
        self.__contratos=[]
    def agregarContrato(self,contrato):
        self.__contratos.append(contrato)