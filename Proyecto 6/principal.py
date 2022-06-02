from coleccion import Lista
from objectencoder import ObjectEncoder
if __name__=='__main__':
    jsonF=ObjectEncoder()
    aparatos = Lista()
    diccionario=jsonF.leerJSONArchivo('aparatoselectronicos.json')
    aparatos=jsonF.decodificarDiccionario(diccionario)
