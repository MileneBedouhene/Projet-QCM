import csv
from TraitementFichier import *


def MettreAJourScore(username, nouveau_score, typeQCM):
    # Chemin du fichier des utilisateurs
    fichier_utilisateurs = r"C:\\Users\\milen\\OneDrive\\Desktop\\Projet-QCM\\DataBase.csv"
    utilisateurs = []
    type_qcm = {
        1:"historique_qcm_Algorithmique",
        2: "historique_qcm_Python",
        3: "historique_qcm_Réseau",
        4: "historique_qcm_Sécurité" 
    }
    # Lecture du fichier des utilisateurs
    with open(fichier_utilisateurs, mode='r', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            utilisateurs.append(ligne)
    
    # Recherche de l'utilisateur
    utilisateur_trouve = False
    for utilisateur in utilisateurs:
        if utilisateur['username'] == username:
            utilisateur_trouve = True

            # Récupérer les scores précédents
            score_qcm = int(utilisateur[type_qcm[typeQCM]])
            score_total = int(utilisateur['score_total'])

            # Mise à jour du score du QCM si le nouveau score est supérieur
            if nouveau_score > score_qcm:
                utilisateur[type_qcm[typeQCM]] = str(nouveau_score)

            score_total_nouveau = sum([
                int(utilisateur['historique_qcm_Sécurité']),
                int(utilisateur['historique_qcm_Python']),
                int(utilisateur['historique_qcm_Réseau']),
                int(utilisateur['historique_qcm_Algorithmique'])
            ])

            # Si la somme des scores est supérieure au score total précédent, on met à jour
            if score_total_nouveau > score_total:
                utilisateur['score_total'] = str(score_total_nouveau)

            break
    # Si l'utilisateur a été trouvé, on réécrit le fichier avec les nouvelles informations
    if utilisateur_trouve:
        with open(fichier_utilisateurs, mode='w', encoding='utf-8', newline='') as fichier:
            champs = ['username', 'password', 'score_total', 'historique_qcm_Sécurité', 
                      'historique_qcm_Python', 'historique_qcm_Réseau', 'historique_qcm_Algorithmique']
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writeheader()
            writer.writerows(utilisateurs)
            print("Les scores ont été mis à jour avec succès !")
    else:
        print("Utilisateur non trouvé.")


def AfficherQCM(lecteur_csv, points_par_question, score, username, typeQCM):
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
            print(f"❌ Mauvaise réponse. La bonne réponse était la réponse {question['correct_option']}.\n")

    # Afficher le score final
    print(f"Votre score final : {score}")

    # Mettre à jour le score dans le fichier utilisateur
    MettreAJourScore(username, score, typeQCM)





def JouerQCM(typeQCM, username):
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
        AfficherQCM(lecteur_csv, points_par_question, score, username, typeQCM)



        

def AfficherScores(df, username):

    try:
        # Filtrer les données pour trouver l'utilisateur
        utilisateur = df[df['username'] == username]
        
        if utilisateur.empty:
            print("Utilisateur introuvable dans la base de données.")
            return
        
        # Extraire les scores
        score_total = int(utilisateur['score_total'].values[0])
        score_securite = int(utilisateur['historique_qcm_Sécurité'].values[0])
        score_python = int(utilisateur['historique_qcm_Python'].values[0])
        score_reseau = int(utilisateur['historique_qcm_Réseau'].values[0])
        score_algo = int(utilisateur['historique_qcm_Algorithmique'].values[0])
        
        # Affichage des scores
        print("\n--- Consultation des Scores ---")
        print(f"Score total : {score_total}")
        print(f"Meilleur Score QCM Sécurité : {score_securite}")
        print(f"Meilleur Score QCM Python : {score_python}")
        print(f"Meilleur Score QCM Réseau : {score_reseau}")
        print(f"Meilleur Score QCM Algorithmique : {score_algo}")
        print("--------------------------------")
    
    except KeyError as e:
        print(f"Erreur : La colonne {e} est manquante dans le fichier CSV.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")
    
