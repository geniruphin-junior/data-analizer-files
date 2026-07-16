import pandas as pd
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
import os
from utils.load_file import load_file

file = input("Voulez vous analyser quel fichier à partir du dossier data ? : ")
folder = "data"
root = os.path.join(folder, file)

try:
    if os.path.exists(root):
        df = load_file(root)
        print("Voici les metriques globales de votre fichier :\n")
        report = get_cleaning_report(df)
        resumé = f"Lignes : {report["rows"]}\ncollones :{report["columns"]} \nvaleures manquantes : {report["missing_values"]}\ndoublons : {report["duplicates"]}\nusage mémoire : {report["memory_mb_used"]}"
        print(resumé)
        print(
            f"👀 jetter un oeil à votre fichier voici les premieres lignes :\n{df.head()}"
        )

    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("Fichier non existant")
