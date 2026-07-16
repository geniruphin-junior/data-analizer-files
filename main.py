import pandas as pd
from pathlib import Path
import os
from utils.load_file import load_file

file = input("Voulez vous analyser quel fichier à partir du dossier data ? : ")
folder = "data"
root = os.path.join(folder, file)

try:
    if os.path.exists(root):
        df = load_file(root)
        print(df)
    else:
        raise FileNotFoundError
except FileNotFoundError:
    print("Fichier non existant")
