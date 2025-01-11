import getpass
from FonctionLogin import *
from FonctionDashboard import *


def main():

    ###############################################################################################################
    ############################################### AUTHENTIFICATION ##############################################
    ###############################################################################################################

    Chemin_Fichier = "./DataBase.csv"
    df = Ouverture_Fichier(Chemin_Fichier)

    Existe = False
    UserName = None  # Pour stocker le nom d'utilisateur authentifié

    while not Existe:  # Boucle tant qu'aucun utilisateur valide n'est connecté
        print("-------- Menu Principal --------\n")
        print("1. Connexion")
        print("2. Inscription")
        print("3. Quitter")
        print("\n--------------------------------\n")

        try:
            ChoixLogin = int(input("Faites votre choix : "))
            print("--------------------------------\n")

            # Connexion de l'utilisateur
            if ChoixLogin == 1:
                UserName = input("Veuillez saisir votre nom d'utilisateur : ")
                Password = getpass.getpass("Veuillez saisir votre mot de passe : ")
                Existe = Connexion(df, UserName, Password)
                if Existe:
                    print("\n-------- Bienvenue sur votre espace --------")
                else:  # Affichage pour les deux cas pour des raisons de sécurité
                    print("Utilisateur n'existe pas")

            # Inscription d'un nouvel utilisateur
            elif ChoixLogin == 2:
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
                        print("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")

                if Existe:
                    print("Utilisateur créé avec succès.")
                    print("\n-------- Bienvenue sur votre espace --------\n")

            # Quitter le programme
            elif ChoixLogin == 3:
                print("-------- Au revoir --------")
                exit()

            else:
                print("Vous n'avez pas choisi une option valide.")

        except ValueError:
            print("Erreur : Vous devez entrer un nombre pour faire un choix.")


    ###############################################################################################################
    ############################################### DASHBOARD #####################################################
    ###############################################################################################################

    while True:
        print("\n-------- Menu Principal --------\n")
        print("1. Jouer QCM")
        print("2. Consultation Des Scores")
        print("3. Deconnexion")
        print("\n--------------------------------")

        try:
            ChoixDashboard = int(input("Faites votre choix : "))
            print("\n--------------------------------\n")

            if ChoixDashboard == 1:
                print("\n--------------------------------\n")
                print("Types de QCM disponibles :")
                print("1. Algorithmique")
                print("2. Python")
                print("3. Réseau")
                print("4. Sécurité")
                print("--------------------------------")
                try:
                    type_qcm = int(input("Choisissez le type de QCM (1-4) : "))
                    JouerQCM(type_qcm, UserName)
                except ValueError:
                    print("Erreur : Vous devez entrer un nombre valide pour choisir le type de QCM.")

            elif ChoixDashboard == 2:
                print("\n--------------------------------\n")
                Chemin_Fichier = "./DataBase.csv"
                df = Ouverture_Fichier(Chemin_Fichier)
                AfficherScores(df, UserName)

            elif ChoixDashboard == 3:
                print("-------- Au revoir --------")
                break

            else:
                print("Choix invalide, veuillez entrer un nombre entre 1 et 3.")

        except ValueError:
            print("Erreur : Vous devez entrer un nombre pour faire un choix.")


###############################################################################################################
################################################# MAIN ########################################################
###############################################################################################################


if __name__ == "__main__":
    main()
