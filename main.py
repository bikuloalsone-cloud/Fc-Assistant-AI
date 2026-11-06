
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

CONSEILS = {
    "PASSES": [
        "Observe tes coequipiers avant de passer.",
        "Cherche un joueur demarque.",
        "Evite les passes risquees.",
        "Change le cote du jeu si necessaire."
    ],
    "TIRS": [
        "Regarde la position du gardien.",
        "Approche-toi de la surface avant de tirer.",
        "Privilegie la precision.",
        "Evite les defenseurs."
    ],
    "DEFENSE": [
        "Protege le chemin vers ton but.",
        "Evite de tacler trop tot.",
        "Garde tes defenseurs organises."
    ],
    "DRIBBLES": [
        "Dribble seulement si tu as de l'espace.",
        "Change de direction pour surprendre.",
        "Protege le ballon."
    ],
    "TACTIQUES": [
        "Ecarte le jeu.",
        "Fais circuler le ballon.",
        "Ne precipite pas tes attaques."
    ]
}

class FCAssistant(App):

    def build(self):
        self.title = "FC Assistant AI"

        principal = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=12
        )

        titre = Label(
            text="[b]FC ASSISTANT AI[/b]",
            markup=True,
            font_size="26sp",
            size_hint_y=None,
            height=65
        )
        principal.add_widget(titre)

        self.resultat = Label(
            text="Bienvenue ! Choisis une categorie.",
            font_size="18sp"
        )
        principal.add_widget(self.resultat)

        for categorie in CONSEILS:
            bouton = Button(
                text=categorie,
                font_size="18sp",
                size_hint_y=None,
                height=55
            )
            bouton.bind(
                on_release=lambda instance, c=categorie:
                self.conseil(c)
            )
            principal.add_widget(bouton)

        bouton = Button(
            text="CONSEIL ALEATOIRE",
            size_hint_y=None,
            height=55
        )
        bouton.bind(
            on_release=lambda instance: self.conseil("ALEATOIRE")
        )
        principal.add_widget(bouton)

        return principal

    def conseil(self, categorie):
        if categorie == "ALEATOIRE":
            categorie = random.choice(list(CONSEILS.keys()))

        message = random.choice(CONSEILS[categorie])
        self.resultat.text = categorie + "\n\n" + message

if __name__ == "__main__":
    FCAssistant().run()
