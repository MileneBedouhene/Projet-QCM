import csv
from datetime import datetime
import json
from TraitementFichier import *

def MettreAJourScore(username, nouveau_score, typeQCM):
    fichier_utilisateurs = "./DataBase.csv"
    utilisateurs = []
    type_qcm = {
        1: "historique_qcm_Algorithmique",
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
            
            # Créer un nouvel enregistrement avec date et score
            nouvelle_tentative = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'score': nouveau_score
            }
            
            # Convertir la chaîne JSON existante en liste Python ou créer une nouvelle liste
            historique_actuel = json.loads(utilisateur[type_qcm[typeQCM]]) if utilisateur[type_qcm[typeQCM]] else []
            
            # Ajouter la nouvelle tentative
            historique_actuel.append(nouvelle_tentative)
            
            # Convertir la liste mise à jour en chaîne JSON
            utilisateur[type_qcm[typeQCM]] = json.dumps(historique_actuel)
            
            # Calculer le score total 
            meilleurs_scores = []
            for type_key in type_qcm.values():
                historique = json.loads(utilisateur[type_key]) if utilisateur[type_key] else []
                meilleur_score = max([tentative['score'] for tentative in historique]) if historique else 0
                meilleurs_scores.append(meilleur_score)
            
            utilisateur['score_total'] = str(sum(meilleurs_scores))
            break
            
    if utilisateur_trouve:
        with open(fichier_utilisateurs, mode='w', encoding='utf-8', newline='') as fichier:
            champs = ['username', 'password', 'score_total', 'historique_qcm_Sécurité',
                     'historique_qcm_Python', 'historique_qcm_Réseau', 'historique_qcm_Algorithmique']
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writeheader()
            writer.writerows(utilisateurs)
            print("\n--------------------------------")
            print("Les scores ont été mis à jour avec succès !")
            print("--------------------------------\n")
    else:
        print("\n--------------------------------")
        print("Erreur : Utilisateur non trouvé.")
        print("--------------------------------\n")


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
                print("\n-----------------------------------")
                reponse = int(input("Votre réponse (1-4) : "))
                print("-----------------------------------\n")
                if 1 <= reponse <= 4:
                    break
                else:
                    print("\n-------------------------------------")
                    print("Veuillez entrer un nombre entre 1 et 4.")
                    print("-------------------------------------\n")
            except ValueError:
                print("\n--------------------------------")
                print("Veuillez entrer un nombre valide.")
                print("--------------------------------\n")

        # Vérifier si la réponse est correcte
        if reponse == int(question['correct_option']):
            print("\n-----------------")
            print("✅ Bonne réponse !")
            print("-----------------\n")
            score += points_par_question
        else:
            print("\n---------------------------------------------------------------------------------------")
            print(f"❌ Mauvaise réponse. La bonne réponse était la réponse {question['correct_option']}.")
            print("---------------------------------------------------------------------------------------\n")

    # Afficher le score final
    print("\n----------------------------")
    print(f"Votre score final : {score}")
    print("----------------------------\n")

    # Mettre à jour le score dans le fichier utilisateur
    MettreAJourScore(username, score, typeQCM)


def JouerQCM(typeQCM, username):
    # Associer chaque type de QCM à son fichier CSV
    fichiers_qcm = {
        1: './QCM/Algo.csv',
        2: './QCM/Python.csv',
        3: './QCM/Reseau.csv',
        4: './QCM/Securite.csv'
    }

    fichier_csv = fichiers_qcm[typeQCM]  # Sélection du fichier correspondant
    score = 0
    points_par_question = 100

    # Lecture du fichier CSV
    with open(fichier_csv, mode='r', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        AfficherQCM(lecteur_csv, points_par_question, score, username, typeQCM)



def AfficherScores(df, username):
    try:
        # Filtrer les données pour trouver l'utilisateur
        utilisateur = df[df['username'] == username]
        
        if utilisateur.empty:
            print("\n----------------------------------------------")
            print("Utilisateur introuvable dans la base de données.")
            print("----------------------------------------------\n")
            return
        
        print("\n=== Historique des scores ===\n")
        
        types_qcm = {
            'historique_qcm_Sécurité': 'Sécurité',
            'historique_qcm_Python': 'Python',
            'historique_qcm_Réseau': 'Réseau',
            'historique_qcm_Algorithmique': 'Algorithmique'
        }
        
        score_total = int(utilisateur['score_total'].values[0])
        print(f"Score total (meilleurs scores) : {score_total}\n")
        
        for col, nom in types_qcm.items():
            historique = json.loads(utilisateur[col].values[0]) if utilisateur[col].values[0] else []
            print(f"\nQCM {nom}:")
            if historique:
                print("Date                    Score")
                print("-" * 35)
                for tentative in sorted(historique, key=lambda x: x['date'], reverse=True):
                    print(f"{tentative['date']}  {tentative['score']}")
                meilleur_score = max(tentative['score'] for tentative in historique)
                print(f"\nMeilleur score: {meilleur_score}")
            else:
                print("Aucune tentative enregistrée")
            print()
            
    except KeyError as e:
        print(f"\nErreur : La colonne {e} est manquante dans le fichier CSV.")
    except Exception as e:
        print(f"\nErreur inattendue : {e}")