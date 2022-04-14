"""
Module main
"""

import pickle
from plat import Plat, option


print("==================GESTION DE RESTAURANT==================\n")


def main():
    """Point d'entree du programme"""


    #Ouvrir le fichier et recuperer la liste
    with open("file_plat.txt", "rb") as file:
        list_plat = pickle.load(file)

    #Afficher le menu
    r = "0"
    while (r == "0" or r == "O" or r == "o"):
        print("==================Liste Des Options================")
        print("1_Ajouter un plat!")
        print("2_Lister les plats!")
        print("3_Modifier un plats!")
        print("4_Supprimer un plats!")
        ch = input("Faites un choix!")
        option(ch, list_plat)
        r = input("Appuyez sur O pour continuer ousur une autre touche pour quitter!")


if __name__ == "__main__":
	main()