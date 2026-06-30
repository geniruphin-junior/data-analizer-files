import pandas as pd


def get_info(data: pd.DataFrame, group_col=None, target_col=None, max_rows=1000):
    """
    Module d'analyse pour Streamlit préparé  pour gloire
    Retourne infos + statistiques + groupby optionnel.
    """

    if not isinstance(data, pd.DataFrame):
        raise TypeError("data doit être un DataFrame pandas")

    df = data.copy()

    # sécurité RAM important pour nous qui avons 4go de ram vive
    if len(df) > max_rows:
        df = df.head(max_rows)

    info = {
        "rows": df.shape[0],
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isna().sum().to_dict(),
        "head": df.head(10).to_dict(orient="records"),  # utile pour streamlit
        "tail": df.tail(5).to_dict(orient="records"),  # utile pour streamlit
    }

    # stats numériques
    numerics = df.select_dtypes(include="number")
    if not numerics.empty:
        info["stats"] = numerics.describe().to_dict()

    # GROUPBY (nouvelle partie importante,si plut tard un client mais le groupe et la colllone de refference)
    if group_col and target_col:
        if group_col in df.columns and target_col in df.columns:

            group_result = (
                df.groupby(group_col)[target_col]
                .agg(["sum", "mean", "max", "min", "count"])
                .reset_index()  # une astuce donnné par notre prof utile pour les tables
            )

            info["groupby"] = group_result.to_dict(orient="records")

    return info  # on retourne les informations dans l interface de gloire
