from time import time
from gasolinera import Gasolinera

def lanzador():
    sec = time()
    gasolinera = Gasolinera()
    cola_repostar = []
    for i in range(1,51):
        cola_repostar.append(i)
    for i in cola_repostar:
        surtidor = Gasolinera.comprobar_surtidor()
        if surtidor != 0:
            Gasolinera.llenar_deposito(surtidor)
            Gasolinera.pagar()