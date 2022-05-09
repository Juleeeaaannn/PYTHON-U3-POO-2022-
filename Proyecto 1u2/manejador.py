import csv
from facultad import Facultad
from carrera import Carrera
class ManejaFacultades:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def LeerArchivo(self):
        contador=0
        list=[]
        archivo=open("Facultades.csv")
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            if(not band)
                if(contador<fila[0]):
                    contador=fila[0]
                    b=fila[1]
                    c=fila[2]
                    d=fila[3]
                    e=fila[4]
                else:
                    carrera=Carrera(fila[1],fila[2],fila[3],fila[4],fila[5])
                    list.append(carrera)
                    band=True
            elif(band):
