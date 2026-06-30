# data_cleaner.py

import pandas as pd  # import de mon module chérie

"""analyse des fichiers pour detecter les anomalies,
    et pour plutard les nettoyer"""


def get_missing_values(df):

    # Retourne le nombre de valeurs manquantes pour chaque colonne.

    return df.isna().sum()


def missing_percentage(df):
    """
    Retourne le pourcentage de valeurs manquantes
    pour chaque colonne.
    """

    return round(df.isna().mean() * 100, 2)


def get_duplicates_counts(df):
    """
    Compte le nombre de doublons.
    """

    return int(df.duplicated().sum())


def get_data_types(df):
    """
    Retourne les types de données, mais personnellement,
    je prefère le dir en englais /dəra:/ n' estce pas gloire,
    ou j ai totalement oublier l anglais.
    """

    return df.dtypes


"""nettoyage des case vides"""


def fill_missing_values(df, fill_values=None):

    for col in df.columns:

        if col in (fill_values or {}):

            df[col] = df[col].fillna(fill_values[col])

        else:

            if pd.api.types.is_numeric_dtype(df[col]):

                df[col] = df[col].fillna(0)

            else:

                df[col] = df[col].fillna("indefinite")

    return df


def drop_missing_values(df):
    """
    Supprime toutes les lignes
    contenant au moins un NaN.
    pour voir à quoi ressemblerais un dataframe sans cases vides
    """

    return df.dropna()


# ==================================
# DOUBLONS
# ==================================


def delete_duplicates(df):
    """
    Supprime les doublons.
    """

    return df.drop_duplicates()


# ==================================
# CONVERSION DES TYPES
# ==================================


def convert_to_numeric(df, column):
    """
    Convertit une colonne en numérique.
    """

    df = df.copy()

    df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def convert_to_string(df, column):
    """
    Convertit une colonne en texte.
    """

    df = df.copy()

    df[column] = df[column].astype(str)

    return df


# ==================================
# RAPPORT GLOBAL
# ==================================


def get_cleaning_report(df):
    """
    Résumé rapide du dataset par notre application
    DATA ANALYSIS FILES.
    """

    report = {
        "rows": df.shape[0],  # ou si je prefere len(df)
        "columns": df.shape[1],  # et len(df.columns)
        "missing_values": int(df.isna().sum().sum()),  # cad valeures manquantes
        "duplicates": int(df.duplicated().sum()),  # nombres des doublons
        "memory_mb_used": round(
            df.memory_usage(deep=True).sum() / (1024 * 1024), 2
        ),  # une astuste de copilot pour savoir la memoire ram utilisé lors d une analyse
    }

    return report
