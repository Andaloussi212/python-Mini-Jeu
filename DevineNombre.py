import random
nombreOrdi = random.randint(1,100)
estDevine = False
compteurTentative = 0

while estDevine : 
    nombreJoueur = int(input("Quel est votre tentative : "))
    if nombreJoueur < nombreOrdi :
        print("Trop petit ! Essaye encore ! ")
        compteurTentative += 1
    elif nombreJoueur > nombreOrdi :
        print("Trop grand ! Essaye encore ! ")
        compteurTentative += 1
    else :
        print("Bien joué ! C'étais le nombre à devinier !")
        estDevine = True
print(compteurTentative)