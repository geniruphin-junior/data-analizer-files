# importations utiles
import pandas as pd  # pd c'est convention de l'import
import os  # module systeme

# creations de la variable file indispansablee pour le projet
file = input("donne moi le nom du fichier que tu veux analyser : ")
try:
    # verifie si le chemin existe
    if os.path.exists(file):
        if file.endswith(".csv"):
            data = pd.read_csv(file)
        elif file.endswith(".xlsx"):
            data = pd.read_excel(file)
        else:
            raise ValueError

        """Boucle for pour le remplace ment automatique des case vides exels et csv"""

        """ les sorties apres mon analyse poussé,
        remplacement des cases,stats et autres infos sur un fichier,car pandas et capable de le faire,
         cad faire des calcules et bientot on integre numpy pour le calcule symbolique"""

        # affichages des informations brutes sur le fichier
        print("voici les informations necessaires sur ton fichier : ")
        print(data.info(), "\n")

        # nombre des collones et noms
        print("noms des colonnes :\n")
        print(data.columns, "\n")

        # affichage du head (5lignes) l'echantillon du fichier
        print("voici les premieres lignes de votre programme : \n")
        print(data.head(), "\n")

        # les stats du fichier si il a des int64 et float64
        print("stats \n")
        print(data.describe(), "\n")

        # affichages apres netoyage
        print("Apres nettoyage nous avons trouver :\n")

        print("Lignes completes sans ecases vides :")
        print(data.dropna(axis=0), "\n")

        print("collones completes apres netoyages :\n")
        print(data.dropna(axis=1), "\n")
        # boucle importante pour gerer les espaces vides

        for col in data.columns:

            if data[col].dtype == "int64":
                value = 0

                data[col] = data[col].fillna(value)
            elif data[col].dtype == "flaot64":
                value = 0.0
                data[col] = data[col].fillna(value)
            else:
                data[col] = data[col].fillna("indefinite")

        # apres remplacement des cases et netoyage universelle vides on a:

        print(
            "***apres total netoyage et remplissage des cases par vos valeurs on a : \n"
        )
        print(">> votre tableau devient : ")
        print(data, "\n")
        print(">> voici vos stats apres nettoyage")
        print(data.describe())

    else:
        raise FileNotFoundError

except FileNotFoundError:
    print("fichier introuvable")

except ValueError:
    print("format non supporté")

"""
nb: -enswith :trouver les dernieres lettres d un mots,Raise arreter 
le programme pour passer à l exception"""
