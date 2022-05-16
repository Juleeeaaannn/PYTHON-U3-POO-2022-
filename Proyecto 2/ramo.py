class Ramo:
    __tamaño=0
    __flores=[]

    def __init__(self,tamaño,flores=None):
        self.__tamaño=tamaño
        if(flores!=None):
            self.setFlores(flores)
    def setFlores(self,flor):
        for i in flor:
            self.__flores.append(i)