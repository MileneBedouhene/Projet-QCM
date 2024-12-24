import pandas as pd
import csv


# Fonction d'ouverture d'un fichier csv
def Ouverture_Fichier(Chemin_Fichier):
    df = pd.read_csv(Chemin_Fichier)
    return(df)

# Fonction de sauvegarde de fichier csv
def Sauvegarde_Fichier(df, Chemin_Fichier):
   df.to_csv(Chemin_Fichier, index=False, quoting=csv.QUOTE_NONNUMERIC) # index=False pour ne pas inclure l'index comme colonne dans le fichier CSV
    