from ramo import Ramo
class ManejaRamo:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def Venta(self):
        band=True
        i=0
        lista=[]
        while(band):
            venta=input('ingrese flores a comprar, (para terminar ingrese 0): ')
            if(venta=='0'):
                band=False
            lista.append(venta)
            i+=1
        ramo=Ramo(i,lista)
        print('ramo vendido')
