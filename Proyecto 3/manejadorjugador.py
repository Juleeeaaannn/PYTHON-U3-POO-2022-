from jugador import Jugador
class ManejaJugador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregar(self,jugador):
        self.__lista.append(jugador)
    def crearJugador(self):
        print('----------------Crear Jugador----------------')
        print('1.Crear Jugador')
        print('2.Generar Jugadores')
        op=input('->')
        if(op=='1'):
            nom=input('Ingrese Nombre:')
            dni=input('Ingrese DNI:')
            ciu=input('Ingrese Ciudad:')
            pais=input('Ingrese Pais:')
            fdenacimiento=input('Ingrese fecha de nacimiento:')
            jugador1=Jugador(nom,dni,ciu,pais,fdenacimiento)
            self.__lista.append(jugador1)
            print('.............Jugador Creado.............')
        elif(op=='2'):
            jugador2=Jugador('Julian','123','San Juan','Argentina','06/12/2000')
            jugador3=Jugador('Alan','124','Buenos Aires','Argentina','7/7/77')
            jugador4=Jugador('Riquelme','125','Buenos Aires','Argentina','8/8/88')
            jugador5=Jugador('Agustin','126','Buenos Aires','Argentina','9/9/99')
            jugador6=Jugador('Pipa','127','Buenos Aires','Argentina','6/6/66')
            jugador7=Jugador('Kun','128','Buenos Aires','Argentina','5/5/55')
            self.__lista.append(jugador2)
            self.__lista.append(jugador3)
            self.__lista.append(jugador4)
            self.__lista.append(jugador5)
            self.__lista.append(jugador6)
            self.__lista.append(jugador7)
            print('.............Jugadores Creados.............')
    def mostrarJugadores(self):
        print('----------------Jugadores----------------')
        for i in self.__lista:
            print(i.getNombre())
    def Buscar(self,jugador):
        i=0
        retorna=None
        while(i<len(self.__lista) and jugador!=self.__lista[i].getNombre()):
            i+=1
        if(i<len(self.__lista)):
            retorna=self.__lista[i]
        else:print('Jugador no econtrado!')
        return retorna
