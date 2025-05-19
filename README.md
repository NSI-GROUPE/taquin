
# 🧩 Projet NSI 2024-2025 – Jeu du Taquin (15-puzzle)

Projet réalisé dans le cadre de la spécialité **NSI (Numérique et Sciences Informatiques)** pendant l’année scolaire **2024-2025**.

## 👨‍💻 Auteur

- **Orélien** (*orelienads*)

---

## 🧠 Résumé

Ce projet consiste à programmer un **jeu du Taquin**, un puzzle classique où le joueur doit organiser des cases numérotées sur une grille 4x4 en déplaçant la case vide.  
Le programme propose plusieurs niveaux de difficulté qui influencent le mélange initial du plateau.  

Le jeu fonctionne en console et utilise une classe Python `Taquin` pour gérer la logique du puzzle.  
L’utilisateur peut interagir avec le jeu, déplacer les cases valides et tenter de résoudre le puzzle.

---

## 🗂️ Structure du projet

| Fichier           | Rôle                                                       |
|-------------------|------------------------------------------------------------|
| `taquin.py`       | Définit la classe `Taquin` avec toute la logique du jeu    |
| `jeu_taquin.py`   | Script principal pour lancer le jeu en mode console        |

---

## 🛠️ Technologies et bibliothèques utilisées

- Python 3 (aucune bibliothèque externe nécessaire)  
- Module standard `random` pour le mélange aléatoire du plateau

---

## 🚀 Instructions pour lancer le projet

### ▶️ Étapes :

1. Assurez-vous d’avoir **Python 3** installé.  
2. Placez-vous dans le dossier contenant les fichiers `.py`.  
3. Lancez le programme avec la commande :  
   ```bash
   python jeu_taquin.py
   ```  
4. Choisissez un niveau de difficulté entre 0 (facile) et 4 (difficile).  
5. Suivez les instructions à l’écran pour déplacer les cases et résoudre le puzzle.

---

## 📸 Capture d’écran

![image](https://github.com/user-attachments/assets/27fa9495-c789-4e07-9e76-c86d81f328ce)


---

## 🎯 Objectifs pédagogiques

- Programmation orientée objet et gestion des classes  
- Modélisation d’une grille en liste Python  
- Interaction utilisateur en mode console  
- Implémentation d’une logique de jeu simple et fonctionnelle  
- Utilisation d’algorithmes pour le mélange du puzzle garantissant sa résolution

---

## ✅ À savoir

- Le niveau 0 correspond à un puzzle non mélangé, donc déjà gagné.  
- Le mélange du plateau est effectué uniquement par des mouvements valides, assurant la solvabilité du jeu.  
- Les entrées utilisateur sont vérifiées pour éviter les erreurs et déplacements invalides.  
- Le nombre de coups effectués est affiché à la fin de la partie.

---

## 📬 Contact

Pour toute question, contactez l’auteur :

- Orélien : `@orelienads`

---

© Projet NSI 2024-2025 — Orélien (orelienads)
