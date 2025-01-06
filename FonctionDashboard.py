import csv
from TraitementFichier import *


def AfficherQCM ( lecteur_csv,points_par_question,score):

    for question in lecteur_csv:
        # Afficher la question et les options
        print(question['question'])
        print("1)", question['option1'])
        print("2)", question['option2'])
        print("3)", question['option3'])
        print("4)", question['option4'])
                
        # Demander une réponse à l'utilisateur
        while True:
            try:
                reponse = int(input("Votre réponse (1-4) : "))
                if 1 <= reponse <= 4:
                    break
                else:
                    print("Veuillez entrer un nombre entre 1 et 4.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")

                # Vérifier si la réponse est correcte
        if reponse == int(question['correct_option']):
            print("✅ Bonne réponse !\n")
            score += points_par_question

        else:
            print(f"❌ Mauvaise réponse. La bonne réponse était la reponse {question['correct_option']}.\n")


        # Afficher le score final
    print(f"Votre score final : {score}")

    with open(fichier_csv, mode='r', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)



   




def JouerQCM(typeQCM):
    # Associer chaque type de QCM à son fichier CSV
    fichiers_qcm = {
        1: r"C:\Users\milen\OneDrive\Desktop\Projet-QCM\QCM\Algo.csv",
        2: r"C:\Users\milen\OneDrive\Desktop\Projet-QCM\QCM\Python.csv",
        3: r"C:\Users\milen\OneDrive\Desktop\Projet-QCM\QCM\Reseau.csv",
        4: r"C:\Users\milen\OneDrive\Desktop\Projet-QCM\QCM\Securite.csv"
    }


    fichier_csv = fichiers_qcm[typeQCM]  # Sélection du fichier correspondant
    score = 0
    points_par_question = 100

    # Lecture du fichier CSV
    with open(fichier_csv, mode='r', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        
        print(f"\n--- QCM Type {typeQCM} ---\n")
        AfficherQCM(lecteur_csv,points_par_question, score)
            
     

# Exemple d'utilisation :
print("Types de QCM disponibles :")
print("1. Algorithmique")
print("2. Python")
print("3. Réseau")
print("4. Sécurité")
type_qcm = int(input("Choisissez le type de QCM (1-4) : "))
JouerQCM(type_qcm)
