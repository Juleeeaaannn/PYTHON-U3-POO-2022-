from flores import Flores
class Ramo:
    __tamano='' #chico mediano grande
    __flores=[] #de un ramo vendido se registra el tamaño del ramo y la o las flores pedidas

    def __init__(self,tamano,flores=None):
        if(tamano<15 and tamano>10):
            self.__tamano='Grande'
        elif(tamano<10 and tamano>5):
            self.__tamano='Mediano'
        elif(tamano<5):
            self.__tamano='Chico'

        if(flores!=None):
            self.setFlores(flores)
    def setFlores(self,flores):
        for i in flores:
            self.__flores.append(i)
    def getFlores(self):
        return self.__flores
    def __str__(self):
        print("---------------------------------------------------------------------")
        s='\n Tamaño:{}\n----------------'.format(self.__tamano)
        for i in self.__flores:
            s +='\n{}\n'.format(i.getNombre())
        return(s)