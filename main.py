
import random

CONSEILS = {
    "PASSES": [
        "Observe tes coéquipiers avant de faire une passe.",
        "Évite les passes risquées au milieu du terrain.",
        "Utilise les passes courtes pour garder le ballon.",
        "Cherche un joueur démarqué.",
        "Change le côté du jeu si l'adversaire bloque ton attaque."
    ],
    "TIRS": [
        "Approche-toi de la surface avant de tirer.",
        "Vise le côté opposé au gardien.",
        "Ne tire pas si un défenseur bloque ton chemin.",
        "Dans la surface, privilégie une frappe bien placée.",
        "Regarde la position du gardien avant de tirer."
    ],
    "DEFENSE": [
        "Ne fais pas sortir tous tes défenseurs.",
        "Protège le chemin vers ton but.",
        "Anticipe les passes de l'adversaire.",
        "Évite de tacler trop tôt.",
        "Garde tes défenseurs bien organisés."
    ],
    "DRIBBLES": [
        "Dribble seulement si tu as de l'espace.",
        "Change de direction pour surprendre ton adversaire.",
        "Évite les dribbles près de ta propre surface.",
        "Utilise les gestes techniques avec modération.",
        "Protège le ballon quand un défenseur approche."
    ],
    "TACTIQUES": [
        "Écarte le jeu pour créer des espaces.",
        "Ne précipite pas tes attaques.",
        "Fais circuler le ballon.",
        "Observe les espaces derrière la défense.",
        "Alterne entre attaques rapides et possession."
    ]
}

def donner_conseil(categorie=None):
    if categorie not in CONSEILS:
        categorie = random.choice(list(CONSEILS.keys()))

    conseil = random.choice(CONSEILS[categorie])

    print("\nFC ASSISTANT AI")
    print("Catégorie :", categorie)
    print("Conseil :", conseil)

def demarrer():
    print("================================")
    print("       FC ASSISTANT AI")
    print("================================")

    while True:
        print("\n1. Passes")
        print("2. Tirs")
        print("3. Défense")
        print("4. Dribbles")
        print("5. Tactiques")
        print("6. Conseil aléatoire")
        print("0. Quitter")

        choix = input("\nChoisis une option : ")

        categories = {
            "1": "PASSES",
            "2": "TIRS",
            "3": "DEFENSE",
            "4": "DRIBBLES",
            "5": "TACTIQUES"
        }

        if choix == "0":
            print("À bientôt !")
            break
        elif choix == "6":
            donner_conseil()
        elif choix in categories:
            donner_conseil(categories[choix])
        else:
            print("Choix incorrect. Réessaie.")

if __name__ == "__main__":
    demarrer()
