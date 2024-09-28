class Person:
    def __init__(self, name, destreza:int, forca:int, defesa:int, life:int):
        self.name = name 
        self.destreza = destreza
        self.forca = forca
        self.defesa = defesa
        self.life = life

    
    def retorno(self):
        return f' Olá {self.name}, bem vindo ao {}'



input = Person("Luciano", 25, 45, 10, 100)

print(Person.retorno(input))