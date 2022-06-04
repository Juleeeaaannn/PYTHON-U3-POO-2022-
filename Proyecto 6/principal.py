from coleccion import Manejador
from objectencoder import ObjectEncoder
if __name__=='__main__':
    jsonF=ObjectEncoder()
    aparatos = Manejador()
    diccionario=jsonF.leerJSONArchivo('aparatoselectronicos.json')
    aparatos=jsonF.decodificarDiccionario(diccionario)
    print('archivo leido!')
