import random
from person import Person, Enemy


dice = random.randint(1 , 20)

def menu():


def fight():
    if dice >= 15:

        damage = dice
        Enemy.life -= damage
        print(f'Você causou um dano de {damage}!')
        return


        

    elif dice < 15 and dice > 5:
        damage = dice - (Person.defesa/100)
        print(f'Você tomou um dano de {damage}!')
        Person.life -= damage
        return 
    
    else:
        print(f'Você tomou um dano de {dice}!')
        Person.life -= dice
        return
