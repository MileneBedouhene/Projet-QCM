import pandas as pd
import hashlib



# Fonction d'ouverture d'un fichier csv
def Ouverture_Fichier(Chemin_Fichier):
    df = pd.read_csv(Chemin_Fichier)
    return(df)

# Fonction de sauvegarde de fichier csv
def sauvegarder_fichier(df, Chemin_Fichier):
    df.to_csv(Chemin_Fichier, index=False)  # index=False pour ne pas inclure l'index comme colonne dans le fichier CSV
    
# Fonction de hachage
def Hachage_Password(PassWord):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(PassWord.encode('utf-8'))
    return sha256_hash.hexdigest()


# Fonction de verification de l'existance d'un utilisateur
def VerificationUtilisateur(df, UserName):
    if UserName in df['username'].values:
        return True  
    else:
        return False


# Fonction de connexion
def Connexion(df, UserName, Password):
    if VerificationUtilisateur(df, UserName):
        utilisateur = df[df['username'] == UserName].iloc[0]
        password_hache = Hachage_Password(Password)
        
        if password_hache == utilisateur['password']:
            return True  # Mot de passe correct
        else:
            return False  # Mot de passe incorrect
    else:
        return False  # Utilisateur n'existe pas
    

# Fonction de creation
def CreationUtilisateur(df, UserName, Password, Chemin_Fichier):
    if VerificationUtilisateur(df, UserName):
        return False  # Utilisateur existe
    else:
        password_hache = Hachage_Password(Password)
        nouvel_utilisateur = {
            'username': UserName,
            'password': password_hache,
            'score_total': 0,  
            'historique_qcm_histoire': 0,
            'historique_qcm_geo': 0,
            'historique_qcm_python': 0,
            'historique_qcm_algorithmique': 0,
            'historique_qcm_reseau': 0
        }
        
        # Convertir le dictionnaire en DataFrame
        nouvel_utilisateur_df = pd.DataFrame([nouvel_utilisateur])
    
        # Ajouter le nouvel utilisateur au DataFrame existant
        df = pd.concat([df, nouvel_utilisateur_df], ignore_index=True)
    
        # Sauvegarder les changements dans le fichier CSV
        sauvegarder_fichier(df, Chemin_Fichier)
    
        return True


### Test :
print("==== Menu Principal ====")
print("1. Connexion")
print("2. Inscription")
print("3. Quitter")
print("=========================")


Chemin_Fichier = "./DataBase.csv"
df = Ouverture_Fichier(Chemin_Fichier)
Existe = False

Choix = int(input("Faites votre choix : "))
if Choix == 1 :
    UserName = input("Veuillez saisir votre nom d'utilisateur : ")
    Password = input("Veuillez saisir votre mot de passe : ")
    Existe = Connexion(df, UserName, Password)
    if Existe :
        print("Bienvenue sur votre espace")
    else :  # Afficher ca pour les deux cas (utilisateur non exisatant ou mot de passe incorrecte) pour des raisons de securite
        print("Utilisateur n'existe pas")

elif Choix == 2:
    while Existe == False:
        UserName = input("Veuillez saisir votre nom d'utilisateur : ")
        Password = input("Veuillez saisir votre mot de passe : ")
        Existe = CreationUtilisateur(df, UserName, Password,Chemin_Fichier)
        if Existe :
            print("Utilisateur creer avec succes")
            print("Bienvenue sur votre espace")
        else:
            print("Veuillez saisir un autre nom d'utilisateur")

elif Choix == 3:
    exit()

else :
    print("Vous n'avez pas choisit les bonnes options")
    exit()





