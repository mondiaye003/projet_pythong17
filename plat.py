"""
Gestion de restaurant
__version__ = "1.0"
__author__ = "Mouhammad NDIAYE"
"""


from genericpath import exists
import pickle


class Plat:  
    def __init__(self, name, price):  
        self.name = name  
        self.price = price


    def ajouter(list_plat):
        #Ajout d'un plat
        name = input("Donner le nom du plat!")
        while True:
            try:
                price = int(input("Donner le prix du plat!"))
            except ValueError:
                print("Vous n'avez pas fourni un prix")
            else:
                break
        plat = Plat(name, price)
        if len(list_plat) ==  0:
            list_plat = []
            list_plat.append(plat)
        else:
            list_plat.append(plat)
        for k in list_plat:
            print(f"{k.name}---")
        #Ouvrir le fichier en y enregistrer la liste
        with open("file_plat.txt", "wb") as file:
            pickle.dump(list_plat, file)


    def lister(list_plat):
        #Affichage de la liste des plats
        i = 0
        for p in list_plat:
            print(f"Numero: {i}, Nom: {p.name}, Prix: {p.price}")
            i += 1


    def modifier(list_plat):
        #Modification d'un plat de la liste
        i = 0
        for p in list_plat:
            print(f"Numero: {i}, Nom: {p.name}, Prix: {p.price}")
            i += 1
        while True:
            try:
                s = int(input("Choisir le numero du plat a MODIFIER ou un nombre negatif pour quitter"))
            except ValueError:
                print("Vous n'avez pas fourni un bon numero")
            else:
                break
        if (s > -1) and (s < i+1):
            name = input("Donner le nom du plat!")
            while True:
                try:
                    price = int(input("Donner le prix du plat!"))
                except ValueError:
                    print("Vous n'avez pas fourni un prix")
                else:
                    break
            plat = Plat(name, price)
            list_plat[s] = Plat(name, price)
            print("Plat MODIFIER avec succes")
        else:
            print("Vous n'avez pas choisi un bon numero")
        #Ouvrir le fichier en y enregistrer la liste
        with open("file_plat.txt", "wb") as file:
            pickle.dump(list_plat, file)



    def supprimer(list_plat):
        #Suppression d'un element de la liste
        i = 0
        for p in list_plat:
            print(f"Numero: {i}, Nom: {p.name}, Prix: {p.price}")
            i += 1
        while True:
            try:
                s = int(input("Choisir le numero du plat a SUPPIMER ou un nombre negatif pour quitter"))
            except ValueError:
                print("Vous n'avez pas fourni un bon numero")
            else:
                break
        if (s > -1) and (s < i+1):
            list_plat.pop(s)
            print("Plat supprime avec succes")
        else:
            print("Vous n'avez pas choisi un bon numero")
        #Ouvrir le fichier en y enregistrer la liste
        with open("file_plat.txt", "wb") as file:
            pickle.dump(list_plat, file)


def option(ch, list_plat):
    if ch == "1":
        Plat.ajouter(list_plat)
        print("=========*****111")
    elif ch == "2":
        print("=========*****222")
        Plat.lister(list_plat)
    elif ch == "3":
        print("=========*****333")
        Plat.modifier(list_plat)
    elif ch == "4":
        print("=========*****333")
        Plat.supprimer(list_plat)
    else:
        print("Choix non pris en compte!")
