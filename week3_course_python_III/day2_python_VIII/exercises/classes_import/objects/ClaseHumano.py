class Humano:

    def __init__(self, nombre, armadura, nivel, ataque, ojos = 2, piernas = 2, dientes = 32, salud = 100):
        self.nombre = nombre 
        self.armadura = armadura 
        self.nivel = nivel 
        self.ataque = ataque 
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes
        self.salud = salud 

    def atacar(self, Orco):
        Orco.salud -= self.ataque - Orco.armadura
        print(f'La salud de {Orco.nombre} es {Orco.salud}')
    
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False

    def atributos(self):
        print(f'nombre : {self.nombre}\narmadura : {self.armadura}\nnivel : {self.nivel}')
        print(f'ataque : {self.ataque}\nojos : {self.ojos}\npiernas : {self.piernas}')
        print(f'dientes : {self.dientes}\nsalud : {self.salud}')
