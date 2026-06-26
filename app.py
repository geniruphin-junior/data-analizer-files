# app.py - Assemblé par Ruphin pour l'équipe Data-Analyzer
import os
import streamlit as st
import pandas as pd
import random
import plotly.express as px

# ==========================================
# IMPORTATION DE MES MODULES (MON CERVEAU PANDAS)
# ==========================================
from utils.load_file import load_file
from utils.data_cleaner import (
    get_cleaning_report,
    delete_duplicates,
    fill_missing_values,
)
from utils.info import get_info

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(page_title="Data-Analyzer files", page_icon="📊", layout="wide")

# STYLE CSS (Design sombre futuriste et pro conçue par GLOIRE)
st.markdown(
    """
<style>
.main { background-color: #0E1117; color: white; }
.stButton>button { width: 100%; border-radius: 10px; height: 50px; font-size: 18px; font-weight: bold; }
.sidebar .sidebar-content { background-color: #111827; }
h1 { color: #4CAF50; }
</style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# LA SIDEBAR (MENU DE NAVIGATION)
# ==========================================
with st.sidebar:
    st.title("📌 Menu & navigation")
    section = st.radio(
        "Aller vers",
        [
            "Accueil",
            "📊graphiques",
            "Analyse détaillée",
            "Synthèse IA",
            "collaboration",
        ],
    )
    st.divider()
    st.subheader("🔗 Liens annexes")
    st.markdown(
        "- [Streamlit](https://streamlit.io)\n"
        "- [Pandas](https://pydata.org)\n"
        "- [NumPy](https://numpy.org)\n"
        "- [Matplotlib](https://matplotlib.org)\n"
        "- [Scikit-learn](https://scikit-learn.org)\n"
        "- [TensorFlow](https://www.tensorflow.org)\n"
        "- [PyTorch](https://pytorch.org)\n"
        "- [Dépot GitHub du projet](https://github.geniruphin-junior/data-files.git)"
    )

# ==========================================
# PAGE 1 : ACCUEIL (Guide simple)
# ==========================================
if section == "Accueil":
    st.title("🚀 Bienvenue sur Data-Analyzer Files")
    st.write(
        "**L’assistant intelligent pour explorer, nettoyer et visualiser vos données.**"
    )

    # --- Guide utilisateur ---
    st.markdown("""
    ### 🧭 Guide rapide
    1. Importez votre fichier CSV ou Excel.  
    2. Analysez vos données avec nos outils automatiques.  
    3. Visualisez vos résultats dans des graphiques interactifs futuristes.  
    4. Collaborez avec votre équipe ou sur le projet grâce à la section dédiée.  
    5. Explorez les dev ressources : [Firebase](https://firebase.google.com) | [Copilot](https://copilot.microsoft.com)
    """)

    uploaded_file = st.file_uploader(
        "📂 Importer un fichier CSV ou Excel (plus tard PDF et Word)",
        type=["csv", "xlsx"],
    )

    # --- Démo avant upload ---
    if not uploaded_file and "df" not in st.session_state:
        st.info(
            "💡 Pas encore de fichier ? Voici une démo futuriste pour découvrir l’application."
        )

        demo_df = pd.DataFrame(
            {
                "Langage": ["Python", "JavaScript", "C++", "TypeScript", "Java", "Go"],
                "Domaine": [
                    "Data Science",
                    "Web",
                    "Systèmes",
                    "Web Frontend",
                    "Entreprise",
                    "Cloud",
                ],
                "Utilisateurs GitHub (k)": [1200, 950, 800, 600, 1100, 400],
                "Likes (k)": [500, 420, 300, 280, 450, 150],
                "Clients": [300, 250, 180, 220, 310, 140],
                "Années pour devenir Senior": [4, 3, 5, 3, 6, 4],
            }
        )
        st.subheader("🎬 Démonstration instantanée")
        st.dataframe(demo_df, use_container_width=True)

        # Palette cyberpunk fixe
        cyberpunk_colors = [
            "#FF007F",
            "#00F0FF",
            "#9D00FF",
            "#39FF14",
            "#FF00F0",
            "#FF0033",
        ]

        # 1️⃣ Barres néon futuristes
        fig1 = px.bar(
            demo_df,
            x="Langage",
            y="Utilisateurs GitHub (k)",
            color="Langage",
            title="🚀 Popularité GitHub par langage",
            template="plotly_dark",
            color_discrete_sequence=cyberpunk_colors,
        )
        st.plotly_chart(fig1, use_container_width=True)

        # 2️⃣ Courbe interactive
        fig2 = px.line(
            demo_df,
            x="Langage",
            y="Likes (k)",
            markers=True,
            title="📈 Likes GitHub par langage",
            template="plotly_dark",
            color_discrete_sequence=cyberpunk_colors,
        )
        st.plotly_chart(fig2, use_container_width=True)

        # 3️⃣ Scatter futuriste
        fig3 = px.scatter(
            demo_df,
            x="Clients",
            y="Années pour devenir Senior",
            size="Utilisateurs GitHub (k)",
            color="Langage",
            hover_name="Domaine",
            title="🌌 Clients vs Années pour devenir Senior",
            template="plotly_dark",
            color_discrete_sequence=cyberpunk_colors,
        )
        st.plotly_chart(fig3, use_container_width=True)

        # 4️⃣ part de chaque language sur github
        fig4 = px.pie(
            demo_df,
            names="langage",
            values="Utilsateurs Github (K)",
            title="Part de chaque langage sur github",
        )
        st.plotly_chart(fig4, use_container_width=True)

        # --- IA fictive ---
        st.subheader("🤖 Simulation IA")
        st.write(
            "**DataBOt :** Bonjour Ruphin 👋, j’ai analysé les langages de programmation. Voici mes observations :"
        )
        st.success("✅ Python et JavaScript dominent en popularité et en likes.")
        st.warning(
            "⚠️ C++ reste puissant mais demande plus d’années pour devenir senior."
        )
        st.info(
            "💡 TypeScript est stratégique : rapide à maîtriser et très demandé en web moderne."
        )

        # --- Bloc code pour installation ---
        st.subheader("💻 Commandes utiles")
        st.code(
            """
# Cloner le dépôt GitHub ou votre fork
git clone https://github.com/geniruphin-junior/data-files.git

# Installer les librairies nécessaires
pip install -r requirements.txt
        """,
            language="bash",
        )

    # --- Après upload : vraies données ---
    if uploaded_file:
        temp_path = os.path.join(".", uploaded_file.name)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Chargement et validation des données..."):
            try:
                st.session_state["df"] = load_file(temp_path)
                st.success("✅ Données chargées avec succès !")
            except Exception as e:
                st.error(f"Erreur : {e}")
            # quoi qu'il se passe on efface le fichier créé
            finally:

                if os.path.exists(temp_path):
                    os.remove(temp_path)

        if "df" in st.session_state:
            df_actuel = st.session_state["df"]
            report = get_cleaning_report(df_actuel)

            # --- Métriques globales ---
            st.subheader("⚙️ Métriques globales de mon Data Cleaner")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Lignes", f"{report['rows']:,}")
            col2.metric("Colonnes", report["columns"])
            col3.metric("Cases vides", report["missing_values"])
            col4.metric("Doublons détectés", report["duplicates"])

            # --- Boutons de nettoyage ---
            st.subheader("🧹 Nettoyage rapide")
            if st.button("🗑️ Enlever les doublons"):
                df_actuel = delete_duplicates(df_actuel)
                st.session_state["df"] = df_actuel
                st.success("✅ Doublons supprimés.")

            if st.button("🧩 Remplir les valeurs vides"):
                df_actuel = fill_missing_values(df_actuel)
                st.session_state["df"] = df_actuel
                st.success(
                    "✅ Valeurs vides remplacées (0 pour numériques, 'indefinite' pour chaînes)."
                )

            # --- Aperçu des données ---
            st.subheader("👀 Aperçu rapide du DataFrame")
            st.dataframe(df_actuel.head(5), use_container_width=True)
            st.dataframe(df_actuel.tail(5), use_container_width=True)

            # --- Graphique automatique ---
            st.subheader("📉 Aperçu graphique automatique")
            for col in df_actuel.columns:
                df_actuel[col] = pd.to_numeric(df_actuel[col], errors="coerce")

            cols_num = df_actuel.select_dtypes(include="number").columns.tolist()
            cols_str = df_actuel.select_dtypes(include="object").columns.tolist()

            if cols_num and cols_str:

                col_x = cols_str[0]
                col_y = cols_num[0]
                fig_auto = px.bar(
                    df_actuel.groupby(col_x)[col_y].mean().reset_index(),
                    x=col_x,
                    y=col_y,
                    color=col_x,
                    title=f"Graphique de : {col_y} par {col_x}",
                    template="plotly_dark",
                    color_discrete_sequence=cyberpunk_colors,
                )
                st.plotly_chart(fig_auto, use_container_width=True)
            else:
                st.info(
                    "Votre fichier ne permet pas de genérer des graphiques automatiques, consulter la section graphique"
                )


# ==========================================
# PAGE 2 : 📊 GRAPHIQUES (INTERACTIF & STABLE)
# ==========================================
elif section == "📊graphiques":
    st.title("📊 Graphiques dynamiques et interactifs")

    if "df" not in st.session_state:
        st.warning(
            "⚠️ Importez d’abord un fichier sur la page d’accueil ou utilisez la démo."
        )
        st.write("Voici une démo des graphiques")
        st.dataframe(
            pd.DataFrame({"Exemple": ["A", "B", "C"], "Valeurs": [10, 20, 15]})
        )
        st.bar_chart(pd.DataFrame({"Valeurs": [10, 20, 15]}, index=["A", "B", "C"]))
    else:
        df = st.session_state["df"].copy()  # on fait une copie
        for col in df.columns:  # on repère les colonnes nécessaires
            if df[col].dtype != "object":
                df[col] = pd.to_numeric(df[col], errors="coerce")

        cols_num = df.select_dtypes(
            include="number"
        ).columns.tolist()  # je les transforme en liste
        cols_str = df.select_dtypes(exclude="number").columns.tolist()

        st.subheader("🎛️ Configuration du graphique")
        # selection des colonnes pour visualisation
        col_x = st.selectbox("Choisir une colonne catégorielle (X)", cols_str)
        col_y = st.selectbox("Choisir une colonne numérique (Y)", cols_num)

        grouped = (
            df.groupby(col_x)[col_y]
            .mean()
            .sort_values(ascending=False)
            .to_frame()  # du plus grand au plus petit
        )

        cyberpunk_palette = [  # palette des couleurs
            "#FF007F",
            "#00F0FF",
            "#9D00FF",
            "#39FF14",
            "#FF00F0",
            "#FF0033",
            "#00FFCC",
            "#FFFF00",
        ]
        grouped["Couleur"] = (
            cyberpunk_palette * (len(grouped) // len(cyberpunk_palette) + 1)
        )[
            : len(grouped)
        ]  # calcul  de coloration

        st.info(f"📊 Graphique généré : **{col_y}** par **{col_x}**")
        st.bar_chart(grouped, y=col_y, color="Couleur")

        # --- Mémoire session_state ---
        st.session_state["last_graph"] = {"x": col_x, "y": col_y}
        st.success(f"🧠 Mémoire sauvegardée : graphique {col_y} par {col_x}")
# ==========================================
# PAGE 3 : ANALYSE DÉTAILLÉE
# ==========================================
elif section == "Analyse détaillée":
    st.title("🔬 Analyse détaillée & Statistiques avancées")

    # Si aucun fichier n'est chargé, je bloque poliment
    if "df" not in st.session_state:
        st.warning("⚠️ Veuillez d'abord importer un fichier sur la page d'Accueil.")
    else:
        df_actuel = st.session_state["df"]

        # --- Configuration du GroupBy ---
        st.subheader("📊 Configuration de l'analyse croisée (Group By)")
        col_g, col_t = st.columns(2)
        group_col = col_g.selectbox(
            "Sélectionner la colonne de regroupement", df_actuel.columns
        )
        cols_numeriques = df_actuel.select_dtypes(include="number").columns.tolist()
        target_col = (
            col_t.selectbox(
                "Sélectionner la colonne cible (Numérique)", cols_numeriques
            )
            if cols_numeriques
            else None
        )

        # --- Calcul via mon module get_info ---
        info_calculée = get_info(
            df_actuel, group_col=group_col, target_col=target_col, max_rows=1000
        )

        # --- Types et valeurs manquantes ---
        st.subheader("🧬 Types des colonnes et valeurs manquantes")
        types_df = pd.DataFrame(
            {
                "Type de données": info_calculée["dtypes"],
                "Cases Manquantes": info_calculée["missing_values"],
            }
        )
        st.dataframe(types_df.T, use_container_width=True)

        # --- Résultats du groupby ---
        if "groupby" in info_calculée:
            st.subheader(
                f"📈 Résultat de l'analyse collective : {target_col} par {group_col}"
            )
            df_group = pd.DataFrame(info_calculée["groupby"])
            st.dataframe(df_group, use_container_width=True)

            # Graphique basé sur les moyennes
            st.bar_chart(df_group.set_index(group_col)["mean"])

            # Mémoire session_state : je garde le dernier groupby
            st.session_state["last_analysis"] = {
                "group": group_col,
                "target": target_col,
            }
            st.success(
                f"🧠 Mémoire sauvegardée : analyse de {target_col} par {group_col}"
            )

# ==========================================
# PAGE 4 : SYNTHÈSE IA (EN ATTENTE DE SCRIPT)
# ==========================================
elif section == "Synthèse IA":
    st.title("🤖 Mode Intelligence Artificielle")

    # Simulation IA futuriste
    st.info(
        "Cette section est en cours de développement. Bientôt, vos calculs Pandas et vos modèles IA seront injectés ici pour générer des synthèses automatiques."
    )

    # Démo fictive pour rassurer l'utilisateur
    st.subheader("🎬 Démonstration IA fictive")
    st.write(
        "**IA DataBot :** Bonjour Ruphin 👋, j’ai analysé ton DataFrame. Voici mes observations :"
    )
    st.success("✅ Les données montrent une tendance positive sur la colonne 'Ventes'.")
    st.warning(
        "⚠️ Attention : la colonne 'Croissance (%)' présente des valeurs manquantes qui pourraient fausser l'analyse."
    )
    st.info(
        "💡 Bientôt, cette section utilisera une clé API pour générer des synthèses réelles basées sur vos données."
    )
# ==========================================
# PAGE 5 : COLLABORATION
# ==========================================
elif section == "collaboration":
    st.title("🤝 Collaboration & Partage")
    st.write(
        "Cette section permet de travailler en équipe sur vos données ou de collaborer avec nous."
    )

    # --- Options de collaboration ---
    st.subheader("📤 Export & Partage")
    st.markdown("""
    - Exporter vos résultats vers un fichier **CSV** ou **Excel**  
    - Partager vos analyses avec vos collègues via un **lien sécurisé**  
    - Intégrer vos dashboards dans des outils comme **Notion**, **Slack**, ou **Teams**  
    - Gérer les accès et la sécurité pour un travail collaboratif
    """)

    # --- Démo fictive ---
    st.subheader("🎬 Démonstration de collaboration")
    st.write(
        "**IA DataBot :** Alice, imagine que tu viens d’exporter ton rapport. Voici ce que tes collègues verront  :"
    )
    demo_collab = pd.DataFrame(
        {
            "Utilisateur": [
                "Alice",
                "Bob",
                "Charlie",
                "claude",
                "pascal",
                "daniel",
                "julie",
            ],
            "Action": [
                "Consulté le rapport",
                "Ajouté un commentaire",
                "Partagé sur Slack",
                "Ajouter d'autres données",
                "Recevoir tout le rapport clean",
                "Nettoyer le rapport",
                "Soumettre les données à un algorithme",
            ],
        }
    )
    st.dataframe(demo_collab, use_container_width=True)
    st.code(
        "import pandas as pd\nimport numpy as np\nimport plotly.express as px\ndf = pd.DataFrame(demo_collab)\ndf['contributions'] = np.linspace(1,10,7)\nfig = px.bar(df,x='Utilisateur',y='contributions'title='Les contributeurs et leurs contributions')\nfig.show()",
        langage="python",
    )

    st.info(
        "Fonctionnalités en cours de développement. L'objectif est de permettre aux gens de collaborer en temps réel sur leurs fichiers."
    )
