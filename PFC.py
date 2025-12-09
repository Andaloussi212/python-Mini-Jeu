import random

choix = ['pierre', 'feuille', 'ciseaux']
compteurJoueur = 0
compteurOrdi = 0
compteurManche = 0


print("BIENVENU SUR LE 🪨 PIERRE  - 📝 FEUILLE - ✂️ CISEAU !")
print("0 : Lire les regles")
print("1 : Différents choix")
print("2 : Commencez à jouer")
ChoixMenu = int(input("Votre choix : "))
if(ChoixMenu == 0) : 
    print("📜 Voici les regles : ")
    print("👨‍💻 Le joueur choisit 🪨 Pierre, 📝 Feuille ou ✂️ Ciseaux.")
    print("🤖 L’adversaire choisit aussi l’un des trois.")
    print("🪨 Pierre casse ✂️ Ciseaux → 🪨 Pierre gagne")
    print("✂️ Ciseaux coupent 📝 Feuille → ✂️ Ciseaux gagnent")
    print("📝 Feuille enveloppe 🪨 Pierre → 📝 Feuille gagne")
    print("Si les deux choisissent la même chose → égalité")
elif(ChoixMenu == 1) :
    print("Choix 1 : 🪨 Pierre")
    print("Choix 2 : 📝 Feuille")
    print("Choix 3 : ✂️ Ciseau")
elif(ChoixMenu == 2) : 
    print("Commençons à jouer !")
    compteurManche = int(input("Combien de manches voulez vous jouer ? : "))
    while(compteurJoueur < compteurManche and compteurOrdi < compteurManche) : 
        ChoixUtilisateur = str(input("Choisit : 🪨 Pierre - 📝 Feuille - ✂️ Ciseaux : "))
        ChoixOrdinateur = random.choice(choix)
        if (ChoixUtilisateur == ChoixOrdinateur) :
            print("👨‍💻 Vous avez choisit : ", ChoixUtilisateur)
            print("🤖 Il a choisit : ", ChoixOrdinateur)
            print("🟰 Egalité !")
        elif (ChoixUtilisateur == 'pierre' and ChoixOrdinateur == 'ciseaux' or ChoixUtilisateur == 'feuille' and ChoixOrdinateur == 'pierre' or ChoixUtilisateur == 'ciseaux' and ChoixOrdinateur == 'feuille') :
            print("👨‍💻 Vous avez choisit : ", ChoixUtilisateur)
            print("🤖 Il a choisit :", ChoixOrdinateur)
            print("✅ Vous avez gangné !")
            compteurJoueur = compteurJoueur + 1
        else :
            print("👨‍💻 Vous avez choisit : ", ChoixUtilisateur)
            print("🤖 Il a chosiit : ", ChoixOrdinateur)
            print("❌ Vous avez perdu !")
            compteurOrdi = compteurOrdi + 1

    if compteurJoueur == compteurManche : 
        print("🏆 Vous avez gangé la partie !")
    else :
        print("👎 L'ordi a gagné la partie...")   
else : 
    print("❓ Cette option n'existe pas...")

