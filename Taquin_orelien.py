# -*- coding: utf-8 -*-
'''
    la classe Taquin
    : Auteur: Projet Terminale NSI
'''

import random

class Taquin():
    '''
    classe pour le jeu du taquin
    '''
    
    def __init__(self):
        '''
        initialise l'objet avec une grille en position initiale
        '''
        self.grille = [i for i in range(1, 16)] + [0]

    def get_valeur(self, indice):
        '''
        renvoie le contenu de la case d'indice précisé avec 0 <= indice <= 15
        '''
        assert 0 <= indice <= 15, "Indice hors bornes"
        return self.grille[indice]

    def set_valeur(self, indice, valeur):
        '''
        modifie le contenu de la case d'indice précisé avec 0 <= indice <= 15 
        en y plaçant la valeur précisée avec 0 <= valeur <= 15
        '''
        assert 0 <= indice <= 15, "Indice hors bornes"
        assert 0 <= valeur <= 15, "Valeur hors bornes"
        self.grille[indice] = valeur

    def get_indice(self, valeur):
        '''
        renvoie l'indice de la case de la grille qui contient la valeur précisée
        '''
        assert 0 <= valeur <= 15, "Valeur hors bornes"
        return self.grille.index(valeur)

    def est_vide(self, indice):
        '''
        renvoie True si la case d'indice précisé est vide
        '''
        assert 0 <= indice <= 15, "Indice hors bornes"
        return self.get_valeur(indice) == 0

    def est_gagne(self):
        '''
        renvoie True si la grille est en position initiale
        '''
        return self.grille == [i for i in range(1, 16)] + [0]

    def __str__(self):
        '''
        renvoie une chaine de caractères pour représenter la grille.
        '''
        res = "+----+----+----+----+\n"
        for i in range(16):
            val = self.grille[i]
            if val == 0:
                res += "|    "
            else:
                res += f"| {val:2d} "
            if i % 4 == 3:
                res += "|\n+----+----+----+----+\n"
        return res

    def __repr__(self):
        '''
        renvoie une chaine qui décrit la classe grille.
        '''
        return "une grille de Taquin"

    def est_possible(self, valeur):
        '''
        renvoie True si la case contenant la valeur est déplaçable
        '''
        assert 1 <= valeur <= 15, "Valeur doit être entre 1 et 15"
        idx_valeur = self.get_indice(valeur)
        idx_vide = self.get_indice(0)
        x1, y1 = idx_valeur % 4, idx_valeur // 4
        x0, y0 = idx_vide % 4, idx_vide // 4
        return abs(x1 - x0) + abs(y1 - y0) == 1

    def deplacer(self, valeur):
        '''
        déplace, si possible, la case contenant la valeur précisée
        '''
        if self.est_possible(valeur):
            idx_valeur = self.get_indice(valeur)
            idx_vide = self.get_indice(0)
            self.grille[idx_vide], self.grille[idx_valeur] = self.grille[idx_valeur], self.grille[idx_vide]

    def valeurs_deplacables(self):
        '''
        renvoie une liste des valeurs des cases déplaçables
        '''
        deplacables = []
        idx_vide = self.get_indice(0)
        x0, y0 = idx_vide % 4, idx_vide // 4
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x, y = x0 + dx, y0 + dy
            if 0 <= x <= 3 and 0 <= y <= 3:
                idx = x + 4*y
                val = self.get_valeur(idx)
                if val != 0:
                    deplacables.append(val)
        return deplacables

    def melanger(self, niveau):
        '''
        mélange le puzzle selon le niveau passé en paramètre (0 à 4)
        '''
        assert 0 <= niveau <= 4, "Niveau doit être entre 0 et 4"
        coups = [5, 10, 30, 100, 200][niveau]
        for _ in range(coups):
            val = random.choice(self.valeurs_deplacables())
            self.deplacer(val)
