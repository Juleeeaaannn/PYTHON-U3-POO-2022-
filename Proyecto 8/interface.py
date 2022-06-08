#DE ESTA MANERA ME FUNCIONO NO CON EL (ITERFACE)
import zope.interface
class ITesorero (zope.interface.Interface):

    def gastosSueldoPorEmpleado ( dni):

        pass

 

class IDirector (zope.interface.Interface):

    def modificarBasico(dni, nuevoBasico):

       pass

    def modificarPorcentajeporcargo(dni, nuevoPorcentaje):

     pass

    def modificarPorcentajeporcategoría(dni, nuevoPorcentaje):

       pass

    def modificarImporteExtra(dni, nuevoImporteExtra):

       pass

 