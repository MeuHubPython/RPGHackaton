class Person:


    def __init__(self, name, category, skill, life=int):
        self.name = name 
        self.category = []
        self.skill = []
        self.life = 100

    def __str__(self):
        return f'{name, skill}'
    
    def retorno(name, category, skill, life):
        print(__str__)

class Skill(Person):

    def fogo(self):
        return "Fire in the hole!!"
    

retorno = Person.retorno("Luciano", "Mago", "fogo", 100)

print(retorno)