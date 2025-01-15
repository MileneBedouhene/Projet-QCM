# Application QCM pour Étudiants en Informatique

Une application en ligne de commande permettant aux étudiants en informatique de tester leurs connaissances à travers des questionnaires à choix multiples.

## Prérequis

- Python 3.12.2 ou supérieur
- Bibliothèques Python requises :
  ```
  pandas
  hashlib
  getpass
  datetime
  ```

## Installation

1. Clonez le repository :
```bash
git clone https://github.com/MileneBedouhene/Projet-QCM.git
cd Projet-QCM
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Structure du Projet

```
Projet-QCM/
├── DataBase/
│   ├── DataBase.csv
├── Fonctions/
│   ├── FonctionDashboard.py
│   ├── FonctionLogin.py
│   ├── TraitemetFichier.py
├── QCM/
│   ├── Algo.csv
│   ├── Python.csv
│   ├── Reseau.csv
│   ├── Securite.csv
├── main.py
├── requirements.txt
└── README.md
```

## Utilisation

### 1. Lancer l'application :
```bash
python main.py
```

### 2. Affichage du menu principal du login :
   ![Menu Principal Du Login](https://drive.google.com/uc?export=view&id=1HzJHKAsJFx9JjjLxV-6KX8c1eNxWtpCl)

### 3. Choix :
  - Si vous faites le premier choix, vous devez inserer votre username et votre mot de passe.
    ![Connexion](https://drive.google.com/uc?export=view&id=1XcXXC-Dtswz8CVAc0aNqY3CFEIfBJqK3)

 - Si vous faites le deuxieme choix, vous devez inserer un username unique et votre mot de passe puis le confirmer.
   ![Inscription](https://drive.google.com/uc?export=view&id=1U0LW4DzYHlFuqaOMs5AxnUjcX1NZugtw)
 - Si vous faites le troisieme choix, vous allez quitter.
   ![Deconnexion](https://drive.google.com/uc?export=view&id=1o3OsNBYaYSPwbmGi5FTgZOqXHBKWAeQg)

### 4. Affichage du Dashboard : 
![Dashboard](https://drive.google.com/uc?export=view&id=1Bvyy0_d6CGgQSAsO-j-DH5baTVP-gI0g)

### 5. Choix :
- Si vous faites le premier choix, vous devez choisir le type de QCM :
  ![Jouer au QCM](https://drive.google.com/uc?export=view&id=16s1ZI5Jth6GY6phLFAsu0fl9NOk1wcob)

  - Par exemple ici j'ai choisis le QCM Python:
    ![Jouer au QCM](https://drive.google.com/uc?export=view&id=1jLBk6PdmAvmyFTeu3dSrcLPcq5GLFsZN)

  - Si vous avez la bonne reponse :
    ![Jouer au QCM](https://drive.google.com/uc?export=view&id=1-kzeKX9F1m3w-wmNp3frrpS6EJjOeGW2)

  - Si vous vaez la mauvaise reponse :
    ![Jouer au QCM](https://drive.google.com/uc?export=view&id=1XC6dA8y9LfRRhzEaiy_zaXn54YG0oh69)
    
  - A la fin le score obtenu vous sera affiché :
    ![Score QCM](https://drive.google.com/uc?export=view&id=1tdlP1Ap_ybo6nJFWDMl20DkuYEWBKhSc)

- Si vous faites le deuxieme choix les historiques de chaque QCM vous sera affiché, et aussi le meilleure score cumulé :
   ![Historique QCM](https://drive.google.com/uc?export=view&id=1HdgBVn-PBFSgYl8MjXA0tmYd4JrXXvJv)

- Si vous faires le troisieme choix, vous allez quitter :
  ![Historique QCM](https://drive.google.com/uc?export=view&id=138S6lqNFdJ-Q1dgoBF0kLc6jyIvE-VJt)


## Notes Importantes

- L'application sauvegarde automatiquement les progrès.

- Un minimum de 5 questions doit être complété pour valider un QCM

- Les scores sont calculés en pourcentage des réponses correctes.

## Support

En cas de problème ou pour toute question, contactez :

- Email : milenebedouhene@gmail.com

  
  
  
 

  





   


