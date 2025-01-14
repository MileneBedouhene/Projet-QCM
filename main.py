import getpass
from Fonctions.FonctionLogin import *
from Fonctions.FonctionDashboard import *


def main():

    ###############################################################################################################
    ############################################### AUTHENTIFICATION ##############################################
    ###############################################################################################################

    Chemin_Fichier = "./DataBase/DataBase.csv"
    df = Ouverture_Fichier(Chemin_Fichier)

    Existe = False

    while not Existe:  # Boucle tant qu'aucun utilisateur valide n'est connecté
        print("\n---------------------------------------------------- Menu Principal ----------------------------------------------------\n")
        print("1. Connexion")
        print("2. Inscription")
        print("3. Quitter")
        

        try:
            print("\n"+"-" *120)
            ChoixLogin = int(input("Faites votre choix entre (1-3): "))
            print("-" *120 + "\n")

            # Connexion de l'utilisateur
            if ChoixLogin == 1:
                UserName = input("Veuillez saisir votre nom d'utilisateur : ")
                Password = getpass.getpass("Veuillez saisir votre mot de passe : ")
                Existe = Connexion(df, UserName, Password)
                if Existe:
                    print("\n---------------------------------------------- Bienvenue sur votre espace ----------------------------------------------")
                else:  # Affichage pour les deux cas pour des raisons de sécurité
                    print("\n"+"-" *120)
                    print("Erreur : Utilisateur n'existe pas")
                    print("-" *120 + "\n")

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
                            print("\n"+"-" *120)
                            print("Erreur : Les mots de passe ne correspondent pas. Veuillez réessayer.")
                            print("-" *120 + "\n")

                    # Création de l'utilisateur après vérification que les mots de passe soient corrects
                    Existe = CreationUtilisateur(df, UserName, Password, Chemin_Fichier)
                    if not Existe:
                        print("\n"+"-" *120)
                        print("Ce nom d'utilisateur est déjà pris. Veuillez en choisir un autre.")
                        print("-" *120 + "\n")

                if Existe:
                    print("\n"+"-" *120)
                    print("Utilisateur créé avec succès.")
                    print("-" *120 + "\n")
                    print("\n---------------------------------------------- Bienvenue sur votre espace ----------------------------------------------")

            # Quitter le programme
            elif ChoixLogin == 3:
                print("\n"+"-" *120)
                print("-------- Au revoir --------")
                print("-" *120 + "\n")
                exit()

            else:
                print("\n"+"-" *120)
                print("Erreur : Vous n'avez pas choisi une option valide.")
                print("-" *120 + "\n")

        except ValueError:
            print("\n"+"-" *120)
            print("Erreur : Vous devez entrer un nombre pour faire un choix.")
            print("-" *120 + "\n")


    ###############################################################################################################
    ############################################### DASHBOARD #####################################################
    ###############################################################################################################

    while True:
        
        print("\n---------------------------------------------------- Menu Principal ----------------------------------------------------\n")
        print("1. Jouer QCM")
        print("2. Consultation Des Scores")
        print("3. Deconnexion")
        print("\n"+"-" *120)

        try:
            ChoixDashboard = int(input("Faites votre choix entre (1-3) : "))
            print("-" *120 + "\n")

            if ChoixDashboard == 1:
                print("Types de QCM disponibles :")
                print("1. Algorithmique")
                print("2. Python")
                print("3. Réseau")
                print("4. Sécurité")
                print("\n"+"-" *120)
                try:
                    type_qcm = int(input("Choisissez le type de QCM (1-4) : "))
                    print("-" *120 + "\n")
                    JouerQCM(type_qcm, UserName)
                except ValueError:
                    print("Erreur : Vous devez entrer un nombre valide pour choisir le type de QCM.")

            elif ChoixDashboard == 2:
                Chemin_Fichier = "./DataBase/DataBase.csv"
                df = Ouverture_Fichier(Chemin_Fichier)
                print("------------------------------------------------ Consultation des Scores ------------------------------------------------")
                AfficherScores(df, UserName)
                print("-" *120 + "\n")

            elif ChoixDashboard == 3:
                print("------------------------------------------------------ Au revoir -------------------------------------------------------")
                break

            else:
                print("\n"+"-" *120)
                print("Choix invalide, veuillez entrer un nombre entre 1 et 3.")
                print("-" *120 + "\n")

        except ValueError:
            print("\n"+"-" *120)
            print("Erreur : Vous devez entrer un nombre pour faire un choix.")
            print("-" *120 + "\n")


###############################################################################################################
################################################# MAIN ########################################################
###############################################################################################################


if __name__ == "__main__":
    main()
