# load_file.py conçu avec soin

import os
import pandas as pd

try:
    import magic

    # verification correct de l'import
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False


# ==========================
# CONFIGURATION
# ==========================

MAX_MB = 100
MAX_ROWS = 1_000_000
MAX_COLUMNS = 200
MAX_RAM_USAGE_MB = 500

DATA_EXTENSIONS = [".csv", ".xlsx"]

ALLOWED_MIME_TYPES = {
    "text/csv",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "text/plain",
}


# ==========================
# FONCTIONS PRIVÉES
# ==========================
def _nettoyage_vip(df):
    df = df.dropna(how="all")
    df = df.dropna(axis=1, how="all")
    return df


def _valid_file(file_path):
    """Vérifie que le fichier existe."""

    if not os.path.exists(file_path):
        raise FileNotFoundError("Fichier introuvable")


def _valid_extension(file_path):
    """Vérifie l'extension."""

    ext = os.path.splitext(file_path)[1].lower()

    if ext not in DATA_EXTENSIONS:
        raise ValueError(f"Extension non autorisée : {ext}")

    return ext


def _check_file_size(file_path):
    """Vérifie la taille du fichier."""

    size_bytes = os.path.getsize(file_path)

    size_mb = size_bytes / (1024 * 1024)

    if size_mb > MAX_MB:
        raise ValueError(
            f"Fichier trop volumineux pour cette application pour le moment ({size_mb:.2f} Mo)"
        )


def _check_mime_type(file_path):
    """Vérifie le vrai type du fichier."""

    if not MAGIC_AVAILABLE:
        return

    mime = magic.from_file(file_path, mime=True)

    if mime not in ALLOWED_MIME_TYPES:
        raise ValueError(f"Type MIME non autorisé : {mime}")


def _check_dataframe(df):
    """Vérifie le DataFrame chargé."""

    if df.empty:
        raise ValueError("Le fichier est vide")

    if len(df.columns) > MAX_COLUMNS:
        raise ValueError(f"Trop de colonnes pour le moment ({len(df.columns)})")

    if len(df) > MAX_ROWS:
        raise ValueError(f"Trop de lignes pour le moment ({len(df)})")

    ram_usage = df.memory_usage(deep=True).sum()

    ram_mb = ram_usage / (1024 * 1024)

    if ram_mb > MAX_RAM_USAGE_MB:
        raise ValueError(f"DataFrame trop lourd ({ram_mb:.2f} Mo)")


def _read_file(file_path, extension):
    """Lit le fichier avec Pandas."""

    try:

        if extension == ".csv":
            return pd.read_csv(file_path)

        if extension == ".xlsx":
            return pd.read_excel(file_path)

    except Exception as e:
        raise ValueError(f"Erreur de lecture : {e}")


# ==========================
# FONCTION PRINCIPALE
# ==========================


def load_file(file_path):
    """
    Charge un CSV ou Excel
    et retourne un DataFrame sécurisé,
    et plut tard du pdf .
    """

    _valid_file(file_path)

    extension = _valid_extension(file_path)

    _check_file_size(file_path)

    _check_mime_type(file_path)

    df = _read_file(file_path, extension)
    df = _nettoyage_vip(df)

    _check_dataframe(df)

    return df
