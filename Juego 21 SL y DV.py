import random
"Johan Sebastian Lopez 20142020013"
"Juan David Villalobo 20142020224"
def valorCarta(carta, acumutotal):
    if(carta[0]=="J" or carta[0]=="Q" or carta[0]=="K"):
        return 10
    if carta[0]=="A" and acumutotal+11>21:
        return 1
    elif carta[0]=="A" and acumutotal+11<=21:
        return 11
    else:
        return int(carta[0])


def contarMano(listaDeCartas, acumutotal):
    if len(listaDeCartas)==1:
        return valorCarta(listaDeCartas[0], acumutotal)
    else:
        return valorCarta(listaDeCartas[0], acumutotal)+contarMano(listaDeCartas[1:],acumutotal+valorCarta(listaDeCartas[0],acumutotal))


def retornarCartas():
    return random.sample([(x,y) for x in [2,3,4,5,6,7,8,9,10,"J","Q","K","A"] for y in ["Diamantes","Corazones","Picas","Treboles"]],52)


def juego(cartasJugador, cartasCasa, contador):
    if(contador==1):
        print "______BIENVENIDO AL 21_______"
        print "\nCartas de la Casa: [Carta Oculta], "+str(cartasCasa[1])
        print "\nSus cartas son: "+str(cartasJugador)
        print "\nSu puntaje es: "+str(contarMano(cartasJugador,0))
        if(contarMano(cartasJugador,0)<21):
            if(input("¿Desea pedir otra carta? 1.Si 2.Plantar ")==1):
                juego(cartasJugador+retornarCartas()[:1],cartasCasa,contador)
            else:
                juego(cartasJugador,cartasCasa,2)
        elif(contarMano(cartasJugador,0)==21):
            juego(cartasJugador,cartasCasa,2)
        else:
            print "LA CASA ES LA GANADORA"
    elif(contador==2):
        print "________JUEGA CASA________"
        print "\nSus cartas son: "+str(cartasJugador)
        print "\nPuntaje: "+str(contarMano(cartasJugador,0))
        print "\nCartas Casa: "+str(cartasCasa)
        print "\nPuntaje: "+str(contarMano(cartasCasa,0))
        if(contarMano(cartasCasa,0)<21):
            if(contarMano(cartasCasa,0)<contarMano(cartasJugador,0)):
                juego(cartasJugador,cartasCasa+retornarCartas()[:1],contador)
            else:
                juego(cartasJugador,cartasCasa,3)
        elif(contarMano(cartasCasa,0)==21):
            print "LA CASA ES LA GANADORA"
        else:
            print "¡FELICITACIONES, EL JUGADOR HA GANADO!"
    else:
        if(contarMano(cartasCasa,0)<contarMano(cartasJugador,0)):
            print "¡FELICITACIONES, EL JUGADOR HA GANADO!"
        elif(contarMano(cartasCasa,0)>=contarMano(cartasJugador,0)):
            print "LA CASA ES LA GANADORA"
juego(retornarCartas()[:2], retornarCartas()[:2],1)
