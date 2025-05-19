# -*- coding: utf-8 -*-
'''
    Jeu du Taquin principal
'''

from Taquin import Taquin

def jouer_taquin(niveau):
    '''
    Lance une partie de taquin selon le niveau choisi
    :param niveau: int entre 0 et 4
    '''
    jeu = Taquin()
    jeu.melanger(niveau)
    coups = 0

    while not jeu.est_gagne():
        print(jeu)
        try:
            valeur = int(input("Quelle case voulez-vous déplacer ? (1 à 15) "))
            if 1 <= valeur <= 15:
                if jeu.est_possible(valeur):
                    jeu.deplacer(valeur)
                    coups += 1
                else:
                    print("Déplacement impossible pour cette case.")
            else:
                print("Valeur invalide, veuillez entrer un nombre entre 1 et 15.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    print(jeu)
    print(f"Bravo ! Vous avez gagné en {coups} coups.")

if __name__ == "__main__":
    print("Bienvenue dans le jeu du Taquin !")
    niveau = -1
    while niveau not in [0, 1, 2, 3, 4]:
        try:
            niveau = int(input("Choisissez un niveau de difficulté (0 facile à 4 difficile) : "))
        except ValueError:
            print("Veuillez entrer un nombre entre 0 et 4.")

    jouer_taquin(niveau)
