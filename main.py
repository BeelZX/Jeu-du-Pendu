# Brun Dylan
# groupe 4-1

#######################
# importations
#######################

from mots import MOTS
from figures_pendu import FIGURES_PENDU
import random

#######################
# fonctions
#######################

def maj_to_min(lettre):
    """
    str -> str
    :param (lettre): Une lettre.
    Retourne une lettre majuscule en minuscule.
    """
    if 65 <= ord(lettre) <= 90:
        lettre = chr(ord(lettre)+32)
    return lettre

def choisit_mot(liste_mot):
    """
    list(str) -> str
    :param (liste_mot): Liste constituée de chaînes de caractères
    Retourne une chaîne aléatoirement choisie parmis les chaines de caractères dans la liste liste_mot.
    """
    return liste_mot[random.randint(0, len(liste_mot) - 1)]

def est_dans(lettre, mot):
    """
    str, str -> bool
    :param (lettre, mot): une lettre ; un mot
    Teste si le caractère lettre est dans la chaine de caractères de mot.
    """
    for i in mot:
        if i == lettre:
            return True
    return False

def input_lettre(props):
    """
    str -> str
    :param (props): Chaîne de caractères constitutée des lettres déjà proposées auparavant.
    Demande une lettre à l'utilisateur, s'il n'en donne pas une, retourne un message d'erreur adapté.
    """
    reponse_exigee = 0
    lettre = input("Proposez une lettre : ")
    while reponse_exigee < 3:
        reponse_exigee = 0
        if len(lettre) > 1:
            print("Proposez qu'une seule lettre , s'il vous plaît.")
            lettre = input("Proposez une lettre : ")
        else:
            reponse_exigee += 1
        
        if len(lettre) == 1:
            if not(97 <= ord(maj_to_min(lettre)) <= 122):
                print(f"{lettre} n'est pas une lettre.")
                lettre = input("Proposez une lettre : ")
            else:
                reponse_exigee += 1
            
        if est_dans(lettre, props):
            print("Vous avez déjà proposé cette lettre.")
            lettre = input("Proposez une lettre : ")
        else:
            reponse_exigee += 1
    return maj_to_min(lettre)

def dessine_pendu(n):
    """
    int -> NoneType
    :param (n): Un nombre entier.
    Affiche la n-ième figure de la liste de chaînes de caractères FIGURES_PENDU.
    """
    print(FIGURES_PENDU[n-1])

def affiche_erreurs(erreurs):
    """
    str -> NoneType
    :param (erreurs): Chaîne de caractères
    Affiche les éléments de la chaîne erreurs comme erreurs du joueur.
    """
    print("Erreurs :")
    print(" ".join(erreurs))
    
def affiche_correctes(lettres, mot_secret):
    """
    str, str -> NoneType
    :param (lettres, mot_secret): Lettres qui sont dans la chaîne de caractères mot_secret ; chaîne de caractères
    Affiche les lettres correctes entrées par le joueur.
    """
    reponse:list[str] = []
    while len(reponse) != len(mot_secret):
        for i in mot_secret:
            if est_dans(i, lettres):
                reponse.append(i)
            else:
                reponse.append("_")
    print(" ".join(reponse))
    
def gagne(propositions, mot_secret):
    """
    str, str -> bool
    :param (propositions, mot_secret): chaîne de caractères qui contient les propositions de lettres ; Chaîne de caractères qui est le mot à trouver
    Retourne test qui vérifie si le joueur a trouvé le mot secret.
    """
    for i in mot_secret:
        if not est_dans(i, propositions):
            return False
    return True

def main():
    """
    NoneType -> NoneType
    Utilise les fonctions décrites auparavant pour créer le jeu du pendu.
    """
    mot_secret = choisit_mot(MOTS)
    erreurs:list[str] = []
    propositions = ''
    while len(erreurs) < 6 and not gagne(propositions, mot_secret):
        dessine_pendu(len(erreurs) + 1)
        affiche_erreurs(erreurs)
        affiche_correctes(propositions, mot_secret)
        lettre = input_lettre(propositions)
        propositions += lettre
        if not est_dans(lettre, mot_secret):
            erreurs.append(lettre)
    if gagne(propositions, mot_secret):
        print(f"Vous avez gagné ! Le mot secret était: {mot_secret}")
    else:
        dessine_pendu(len(erreurs) + 1)
        print(f"Vous avez perdu. Le mot secret était: {mot_secret}")
        
if __name__ == '__main__':
    main()