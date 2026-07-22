import pandas as pd

# import des packages pour le cleaning
from utils.data_cleaner import (
    get_missing_values,
    missing_percentage,
    get_duplicates_counts,
    get_data_types,
    get_cleaning_report,
    fill_missing_values,
    drop_missing_values,
    delete_duplicates,
)

# package pour chargement des fichiers
from utils.load_file import load_file
import os, sys  # systeme

verify = input(
    "Bienvenue sur le mini analyseur virtuel tapez q pour sortir et une autre lettre que Q pour continuer: "
)
if verify == "Q".lower():
    sys.exit(2)
else:
    file = input("Voulez vous analyser quel fichier à partir du dossier data ? : ")
    folder = "data"
    root = os.path.join(folder, file)
    try:
        if not os.path.exists(root):
            raise FileNotFoundError
        df = load_file(root)
        print("Voici les metriques globales de votre fichier :")
        report = get_cleaning_report(df)
        resumé = f"Lignes : {report["rows"]}\ncollones :{report["columns"]} \nvaleures manquantes : {report["missing_values"]}\ndoublons : {report["duplicates"]}\nusage mémoire : {report["memory_mb_used"]}"
        print(resumé)
        verify = input("Voulez vous continuer et passer à l'étape suivante [Y,N]: ")
        if verify == "Y".lower():
            print(
                f"\n👀 jetter un oeil à votre fichier voici les premieres lignes :\n{df.head()}"
            )
            missing = delete_duplicates(df)
            missing = drop_missing_values(df)
        else:
            sys.exit(1)
        verify = input(
            "Maintenat voulez vous passer à votre fichier en mode nettoyage [Y,N] :"
        )

        if verify == "Y".lower():
            print(
                f"\nAprès nettoyage des cases vides, et des doublons voici un appercu sur vos données : \n{missing.head()}"
            )
            sys.exit(0)

    except FileNotFoundError:
        print("Fichier non existant")
