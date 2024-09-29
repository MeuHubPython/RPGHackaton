import random

dice_life = random.randint(1, 50)
dice_forca = random.randint(1, 50)
dice_defesa = random.randint(1, 50)



class Person:
    def __init__(self, name, destreza:int, forca:int, defesa:int, life:int):
        self.name = name 
        self.destreza = destreza
        self.forca = forca
        self.defesa = defesa
        self.life = life

    
    def retorno(self):
        return f' Olá {self.name}, bem vindo ao {self}'


class Enemy:
    def __init__(self, life, forca, defesa):
        self.life = life
        self.forca = forca
        self.defesa = defesa