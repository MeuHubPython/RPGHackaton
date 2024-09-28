import random
#import  

def fight():
    while True:
        choice = input("Escolha um número para continuar: /n1-Explorar /n2-fugir /n3-Atacar")
        if choice == 1:
            #código da narrativa
            print("")
        elif choice == 2:
            print("Você fugiu, o jogo acabou /n(porque você é um covarde...)")
            break
        elif choice == 3:
            #código do ataque
            print("")
        else:
            try:
                print("Escolha um comando válido")
            except TypeError:
                print("Só são permitido números")
