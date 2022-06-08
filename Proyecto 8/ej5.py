import zope.interface
#DE ESTA MANERA ME FUNCIONO NO CON EL (ITERFACE)
class Iinterface(zope.interface.Interface):
    def insertarElemento(posicion,elemento):
        pass
        #para insertar un objeto en una posición determinada 
        #en una colección, teniendo en cuenta el manejo de excepciones 
        #cuando la posición donde se vaya a insertar no sea válida.
    def agregarElemento(elemento):
        pass
        #para agregar un elemento al final de una colección
    def mostrarElemento():
        pass
        # dada una posición de la colección, 
        # mostrar los datos del elemento almacenado en dicha posición
        # si esa posición es válida, en caso de que no sea válida lanzar
        # una excepción que controle el error.