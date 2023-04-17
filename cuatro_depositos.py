from threading import Thread, Lock
from gasolinera import Gasolinera
import time

def cuatrodeps():
    inicio = time.time()
    gasolinera = Gasolinera()
    cola_repostar = []
    for i in range(1,51):
        cola_repostar.append(i)
    for coche in cola_repostar:
        if time.time() - inicio >= 1.5:
            break
        surtidores_libres = gasolinera.comprobar_surtidor()
        if surtidores_libres != -1:
            hilos = []
# NO ESTA ACABADO
cuatrodeps()