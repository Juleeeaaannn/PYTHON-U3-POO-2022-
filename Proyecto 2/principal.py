from menu import Menu
from manejadorflores import ManejaFlores
from manejadorramo import ManejaRamo
if __name__=='__main__':
    menu=Menu()
    manejadorF=ManejaFlores()
    manejadorR=ManejaRamo()
    manejadorF.LeerArchivo()
    salir=False
    while not salir:
        print('------------------------------------------')
        print('1.')
        print('2.')
        print('3.Salir')
        op=input('->')
        print('------------------------------------------')
        if(op=='1'):
            menu.opcion(op,manejadorR)
        salir = op =='3'


