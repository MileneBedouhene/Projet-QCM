from Login import *
import getpass


print("-------- Menu Principal --------\n")
print("1. Connexion")
print("2. Inscription")
print("3. Quitter")
print("\n--------------------------------")

Chemin_Fichier = "./DataBase.csv"
df = Ouverture_Fichier(Chemin_Fichier)

###############################################################################################################
########################################## System D'authentification ##########################################
###############################################################################################################

Existe = False
try:
    Choix = int(input("Faites votre choix : "))
    print("--------------------------------\n")
    if Choix == 1:
        UserName = input("Veuillez saisir votre nom d'utilisateur : ")
        Password = getpass.getpass("Veuillez saisir votre mot de passe : ")
        Existe = Connexion(df, UserName, Password)
        if Existe:
            print("\n-------- Bienvenue sur votre espace --------")
        else:  # Afficher ca pour les deux cas (utilisateur non exisatant ou mot de passe incorrecte) pour des raisons de securite
            print("Utilisateur n'existe pas")


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
    
            # Créer l'utilisateur après vérification que les mots de passes soient correctes
            Existe = CreationUtilisateur(df, UserName, Password, Chemin_Fichier)
            if not Existe:
                print("Veuillez saisir un autre nom d'utilisateur")

            
        if Existe:
            print("Utilisateur créé avec succès.")
            print("-------- Bienvenue sur votre espace --------")

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



###############################################################################################################
############################################### DASHBOARD #####################################################
###############################################################################################################


