class Ramo:
    __tamaño=str
    __flores=[]
    def __init__(self,tamaño,flores=None):
        self.__tamaño=tamaño
        if(flores!=None):
            self.setFlores(flores,1)
    def setFlores(self,flor):
        for p in flor:
            self.__flores.append(p)