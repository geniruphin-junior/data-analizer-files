import os

# Structure du projet
structure = {
    "data-analyzer": [
        "app.py",
        "requirements.txt",
        "README.md",
        "utils/file_loader.py",
        "utils/data_cleaner.py",
        "utils/visualizer.py",
        "assets/.gitkeep",  # pour garder le dossier vide dans git
        "sample_data/.gitkeep",
    ]
}


def create_structure(structure):
    for root, files in structure.items():
        # Créer le dossier racine
        os.makedirs(root, exist_ok=True)
        for file in files:
            # Créer les sous-dossiers si besoin
            path = os.path.join(root, file)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            # Créer le fichier vide
            with open(path, "w", encoding="utf-8") as f:
                if file.endswith(".py"):
                    f.write("# " + file + "\n")
                elif file == "requirements.txt":
                    f.write(
                        "streamlit\npandas\nmatplotlib\nopenpyxl\nPyPDF2\npython-docx\n"
                    )
                elif file == "README.md":
                    f.write(
                        "# Data Analyzer Project\n\nProjet d'analyse de fichiers avec Streamlit, Pandas et Matplotlib fait par des jeunes.\n"
                    )

    print("✅ Structure du projet créée avec succès !")


if __name__ == "__main__":

    create_structure(structure)
