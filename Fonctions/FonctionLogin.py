import pandas as pd
import csv
import hashlib
import json
from Fonctions.TraitementFichier import * 

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
            'score_total': '0',  
            'historique_qcm_Sécurité': '[]',    
            'historique_qcm_Python': '[]',      
            'historique_qcm_Algorithmique': '[]',
            'historique_qcm_Réseau': '[]'       
        }
        

        nouvel_utilisateur_df = pd.DataFrame([nouvel_utilisateur])

        colonnes_attendues = [
            'username', 'password', 'score_total',
            'historique_qcm_Sécurité', 'historique_qcm_Python', 
            'historique_qcm_Algorithmique', 'historique_qcm_Réseau'
        ]

        # S'assurer que toutes les colonnes existent
        for colonne in colonnes_attendues:
            if colonne not in df.columns:
                if colonne in ['historique_qcm_Sécurité', 'historique_qcm_Python', 
                             'historique_qcm_Algorithmique', 'historique_qcm_Réseau']:
                    df[colonne] = '[]' 
                elif colonne == 'score_total':
                    df[colonne] = '0'   
                else:
                    df[colonne] = ""    

        # Ajouter le nouvel utilisateur au DataFrame existant
        df = pd.concat([df, nouvel_utilisateur_df], ignore_index=True)
    
        # Sauvegarder les changements dans le fichier CSV
        Sauvegarde_Fichier(df, Chemin_Fichier)
    
        return True