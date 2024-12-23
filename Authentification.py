import getpass
from Login import *

def authentification():
   
    Chemin_Fichier = "./DataBase.csv"
    df = Ouverture_Fichier(Chemin_Fichier)

    print("-------- Menu Principal --------\n")
    print("1. Connexion")
    print("2. Inscription")
    print("3. Quitter")
    print("\n--------------------------------")

    Existe = False
    try:
        Choix = int(input("Faites votre choix : "))
        print("--------------------------------\n")

        # Connexion de l'utilisateur
        if Choix == 1:
            UserName = input("Veuillez saisir votre nom d'utilisateur : ")
            Password = getpass.getpass("Veuillez saisir votre mot de passe : ")
            Existe = Connexion(df, UserName, Password)
            if Existe:
                print("\n-------- Bienvenue sur votre espace --------")
            else:  # Affichage pour les deux cas pour des raisons de sécurité
                print("Utilisateur n'existe pas")

        # Inscription d'un nouvel utilisateur
        elif Choix == 2:
            Existe = False 
            while not Existe:
                UserName = input("Veuillez saisir votre nom d'utilisateur : ")

                while True:
                    Password = getpass.getpass("Veuillez saisir votre mot de passe : ")
                    ConfirmPassword = getpass.getpass("Veuillez confirmer votre mot de passe : ")
                    if Password == ConfirmPassword:
                        break 
                    else:
                        print("Les mots de passe ne correspondent pas. Veuillez réessayer.")
                
                # Création de l'utilisateur après vérification que les mots de passe soient corrects
                Existe = CreationUtilisateur(df, UserName, Password, Chemin_Fichier)
                if not Existe:
                    print("Veuillez saisir un autre nom d'utilisateur")

            if Existe:
                print("Utilisateur créé avec succès.")
                print("-------- Bienvenue sur votre espace --------")

        # Quitter le programme
        elif Choix == 3:
            print("-------- Au revoir --------")
            exit()

        else:
            print("Vous n'avez pas choisi une option valide.")
            exit()

    except ValueError:
        print("--------------------------------")
        print("Erreur : Vous devez entrer un nombre pour faire un choix.")
        print("--------------------------------")



