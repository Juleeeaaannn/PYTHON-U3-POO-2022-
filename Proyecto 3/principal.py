from menu import Menu
from manejadorjugador import ManejaJugador
from manejadorcontrato import ManejaContrato
from manejadorequipos import ManejaEquipo
if __name__=='__main__':
    menu=Menu()
    manejadorJ=ManejaJugador()
    manejadorC=ManejaContrato()
    manejadorE=ManejaEquipo()
    manejadorE.LeerArchivo()
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.')
        print('2.')
        print('3.')
        print('4.Salir')
        op=input('->')
        print('------------------------------------------')
        if(op=='1' or op=='2' or op=='3'):
            menu.opcion(op,manejadorJ,manejadorC,manejadorE)
        salir = op =='4'


