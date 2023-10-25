
#1) Création de la grille vide de morpion
grille = [[' ' for _ in range(3)] for _ in range(3)]

def afficher_grille():
    for ligne in grille:
        print('|'.join(ligne))
        print('-' * 5)

#2)Écrire la fonction permettant de jouer un O ou un X.

def jouer_tour(joueur):
    print(f"C'est le tour du joueur {joueur}.")
    ligne, colonne = -1, -1 

    while True:
        try:
            ligne = int(input("Entre le numéro de la ligne ou tu veux mettre ton symbole avec 0, 1, ou 2 : "))
            colonne = int(input("Entre le numéro de la colonne ou tu veux mettre ton symbole avec 0, 1, ou 2 : "))

            if 0 <= ligne < 3 and 0 <= colonne < 3 and grille[ligne][colonne] == ' ':
                grille[ligne][colonne] = joueur
                break
            else:
                print("Nombres invalides ou case déjà occupée.Réessaye.")
        except ValueError:
            print("Veuillez entrer les nombres indiqué uniquement !.")

joueur_actuel = 'X'
for _ in range(9): 
    afficher_grille()
    jouer_tour(joueur_actuel)
    joueur_actuel = 'O' if joueur_actuel == 'X' else 'X'

afficher_grille()

#3)Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3 symboles sur une ligne verticale, horizontale, diagonale.


def verifier_ligne_gagnante(grille, joueur):
    for ligne in grille:
        if all(symbole == joueur for symbole in ligne):
            return True
    return False

def verifier_colonne_gagnante(grille, joueur):
    for colonne in range(3):
        if all(grille[i][colonne] == joueur for i in range(3)):
            return True
    return False


def verifier_diagonale_gagnante(grille, joueur):
    if all(grille[i][i] == joueur for i in range(3)) or all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    return False


def verifier_victoire(grille, joueur):
    return (verifier_ligne_gagnante(grille, joueur) or
            verifier_colonne_gagnante(grille, joueur) or
            verifier_diagonale_gagnante(grille, joueur))


if verifier_victoire(grille, 'X'):
    print("Le joueur X a gagné !")
elif verifier_victoire(grille, 'O'):
    print("Le joueur O a gagné !")

    #4)Écrire la fonction vérifiant si la grille est complète.