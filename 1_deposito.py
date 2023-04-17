from gasolinera import Gasolinera

def undeposito():
    gasolinera = Gasolinera()
    cola_repostar = []
    tiempos = []
    for i in range(1,51):
        cola_repostar.append(i)
    for coche in cola_repostar:
        surtidor = gasolinera.comprobar_surtidor()
        if surtidor != -1:
            tiempo_llenar = gasolinera.llenar_deposito(surtidor)
            tiempo_pagar = gasolinera.pagar()
            tiempo_total = tiempo_llenar + tiempo_pagar
            tiempos.append(tiempo_total)
            if sum(tiempos)>=15:
                break
    print('Han repostado {} coches'.format(len(tiempos)))
    print('La media de tiempo de repostaje es de {} minutos'.format(sum(tiempos)/len(tiempos)))

undeposito()