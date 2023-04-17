import random

class Gasolinera:
    def __init__(self):
        # Los surtidores y la caja son booleanos que indican si se pueden usar o no
        self.surtidor1 = True
        self.surtidor2 = False
        self.surtidor3 = False
        self.surtidor4 = False
        self.caja = True

    def comprobar_surtidor(self):
        surtidores = [self.surtidor1, self.surtidor2, self.surtidor3, self.surtidor4]
        libre = False
        for i in range(len(surtidores)):
            if surtidores[i] == True:
                libre = True
                return i
        if libre == True:
            return i
        else:
            return -1

    def llenar_deposito(self, surtidor):
        if surtidor == 0:
            self.surtidor1 = False
        elif surtidor == 1:
            self.surtidor2 = False
        elif surtidor == 2:
            self.surtidor3 = False
        elif surtidor == 3:
            self.surtidor4 = False
        duracion = random.randrange(5,10)
        print('Depósito lleno')
        if surtidor == 0:
            self.surtidor1 = True
        elif surtidor == 1:
            self.surtidor2 = True
        elif surtidor == 2:
            self.surtidor3 = True
        elif surtidor == 3:
            self.surtidor4 = True
        return duracion

    def pagar(self):
        if self.caja == True:
            self.caja = False
            print('Pago realizado')
            self.caja = True
            return 3

