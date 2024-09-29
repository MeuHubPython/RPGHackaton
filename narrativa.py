import random


inimigos = ["Orc", "Zumbi", "Goblin", "Esqueleto", "Dragão", "Lobisomen"]

exploracao = ["Você entrou em uma caverna", "Você caiu em uma armadilha!!", "Você foi atingido criticamente por uma flecha!! Você morreu!!"]

def narrativa(escolha):
    match escolha:
        case 3:
            return print(f"Apareceu um {random.choice(inimigos)}!! O que você vai fazer?")
        case 1:
            a = random.choice(exploracao)
            if a == exploracao[0]:
                return print(a)
            elif a == exploracao[1]:
                print(a)
                return Person.life -= 15
            elif a == exploracao[2]:
                print(a)
                break



