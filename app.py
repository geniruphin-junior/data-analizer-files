# app.py - Assemblé par Ruphin pour l'équipe Data-Analyzer
import os
import streamlit as st
import pandas as pd
import random
import plotly.express as px

# IMPORTATION DE MES MODULES (MON CERVEAU PANDAS & GRAPHIQUE)

from utils.load_file import load_file
from utils.data_cleaner import (
    get_cleaning_report,
    delete_duplicates,
    fill_missing_values,
)
from utils.get_results import get_info
from utils.visualiseur.plotly_graphs import Visualizer

# ===========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(page_title="Data-Analyzer files", page_icon="📊", layout="wide")

# STYLE CSS (Design sombre futuriste et pro conçue par GLOIRE)
st.markdown(
    """
<style>
.main { background-color: #0E1117; color: white; }
.stButton>button { width: 100%; border-radius: 10px; height: 50px; font-size: 18px; font-weight: bold;margin:auto 2rem }
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
            "🏠 Accueil",
            "📊 graphiques",
            "👁‍🗨 Analyse détaillée",
            "👂 Synthèse IA",
            "🤝 collaboration",
        ],
    )
    st.divider()
    st.subheader("🔗 Liens annexes")
    st.markdown(
        "- [Streamlit](https://streamlit.io)\n"
        "- [Ruphy.com](https://github.io/my_site_web)\n"
        "- [Redit](https://redit.com/geniruphin)\n"
        "- [Devchat](https://devchat-ruphin.web.app)\n"
        "- [Dépot GitHub du projet](https://github.geniruphin-junior/data-files.git)"
    )

# ==========================================
# PAGE 1 : ACCUEIL (Guide simple)
# ==========================================
if section.endswith("Accueil"):
    st.title("🚀 Bienvenue sur Data-Analyzer Files")
    st.write(
        "**L’assistant intelligent pour explorer, nettoyer et visualiser vos données rapidement.**"
    )

    # --- Guide utilisateur ---
    st.markdown("""
    ### 🧭 Guide rapide
    1. Importez votre fichier CSV ou Excel.  
    2. Analysez vos données avec nos outils automatiques.  
    3. Visualisez vos résultats dans des graphiques interactifs futuristes.  
    4. Collaborez avec votre équipe ou sur le projet grâce à la section dédiée.  
    5. Explorez les dev ressources : [Firebase](https://firebase.google.com)  |  [Copilot](https://copilot.microsoft.com)
    """)

    # variable d'upload
    uploaded_file = st.file_uploader(
        "📂 Importer un fichier CSV ou Excel (plus tard PDF et Word)",
        type=["csv", "xlsx"],
    )

    # --- Démo avant upload ---
    if not uploaded_file and "df" not in st.session_state:
        st.info(
            "💡 Pas encore de fichier ? Voici une démo  pour découvrir l’application."
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

        fig = Visualizer(demo_df)
        fig._bar_chart(demo_df.columns[0], demo_df.columns[2], "popularité")

        # 2️⃣ Courbe interactive
        fig._line_chart(
            demo_df.columns[0], demo_df.columns[3], "📈 Likes GitHub par langage"
        )

        # 3️⃣ Scatter futuriste
        fig._scatter(
            demo_df.columns[4],
            demo_df.columns[5],
            "🌌 Clients vs Années pour devenir Senior",
            demo_df.columns[3],
        )

        # 4️⃣ part de chaque language sur github
        fig._pie_chart(
            col1=demo_df.columns[0],
            col2=demo_df.columns[2],
            title="Part de chaque langage sur github",
        )

        # --- IA fictive ---
        st.subheader("🤖 Simulation IA")
        st.write(
            "**DataBOt :** Bonjour GéniRuphin 👋, j’ai analysé les langages de programmation. Voici mes observations :"
        )
        st.success("✅ Python et JavaScript dominent en popularité et en likes.")
        st.warning(
            "⚠️ C++ reste puissant mais demande plus d’années pour  avoir un bon niveau et est concurencé par rust."
        )
        st.info(
            "💡 TypeScript est stratégique : rapide à maîtriser et très demandé en web moderne."
        )

        # --- Bloc code pour installation ---
        st.subheader("💻 Commandes utiles")
        st.code(
            """
# Cloner le dépôt GitHub ou votre fork
git clone https://github.com/geniruphin-junior/data-analizer-files.git

# Installer les librairies nécessaires
pip install -r requirements.txt

# Entrer dans le dossier du projet 
cd data-analizer-files

# Lancer l'app avec web 
streamlit run app.py

# Lancer l'app en ligne de commande
python main.py
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
            col1, col2, col3, col4, col5 = st.columns(5)
            lignes = col1.metric("Lignes", f"{report['rows']:,}")
            colonnes = col2.metric("Colonnes", report["columns"])
            cases = col3.metric("Cases vides", report["missing_values"])
            doublons = col4.metric("Doublons détectés", report["duplicates"])
            ram = col5.metric("Memoire Usage/Mo", report["memory_mb_used"])

            # --- Boutons de nettoyage et la logique de leurs affichage ---
            if report["missing_values"] > 0 or report["duplicates"] > 0:
                st.subheader("🧹 Nettoyage rapide")
                if report["duplicates"] > 0:
                    if st.button("🗑️ Enlever les doublons"):
                        df_actuel = delete_duplicates(df_actuel)
                        st.session_state["df"] = df_actuel
                        st.success("✅ Doublons supprimés.")

                if report["missing_values"] > 0:
                    if st.button("🧩 Remplir les valeurs vides"):
                        df_actuel = fill_missing_values(df_actuel)
                        st.session_state["df"] = df_actuel
                        st.success(
                            "✅ Valeurs vides remplacées (0 pour numériques, 'indefinite' pour chaînes)."
                        )
            else:
                st.info(
                    "how,Bravo votre fichier est deja propre plus bésoin de le nettoyer"
                )

            # --- Aperçu des données ---
            st.subheader("👀 Aperçu rapide du DataFrame")
            st.write("Voici les premieres lignes de votre dataframe ")
            count = st.number_input(
                "Voulez-vous visualiser combien des lignes pour avoir une vue d'ensemble sur votre fichier : ?",
            )

            st.dataframe(
                df_actuel.head(int(count)) if count > 5 else df_actuel.head(),
                use_container_width=True,
            )
            st.write("Les dernires lignes de votre dataframe")
            st.dataframe(df_actuel.tail(), use_container_width=True)

            # --- Graphique automatique ---
            st.subheader("📉 Aperçu graphique automatique")
            cols_num = []
            cols_str = []
            for col in df_actuel.columns:
                try:
                    converted = pd.to_numeric(df_actuel[col], errors="raise")
                    df_actuel[col] = converted
                    cols_num.append(col)
                except (ValueError, TypeError):
                    if df_actuel[col].dtype == "object":
                        cols_str.append(col)
            if cols_num and cols_str:
                col_x = cols_str[0]
                col_y = cols_num[0]
                df_grouped = df_actuel.groupby(col_x)[col_y].mean().reset_index()
                fig_auto = px.bar(
                    df_grouped,
                    x=col_x,
                    y=col_y,
                    color=col_x,
                    title=f"Graphique de : {col_y} par {col_x}",
                    template="plotly_dark",
                    color_discrete_sequence=cyberpunk_colors,
                )
                st.plotly_chart(fig_auto, use_container_width=True)
            else:
                info, button = st.columns(2)

                info.info("Votre fichier ne permet pas de genérer des graphiques")
                button.button("Graphiques")


# ==========================================
# PAGE 2 : 📊 GRAPHIQUES (INTERACTIF & STABLE) EN ATTENTE ET MODIFICATION
# ==========================================
elif section.endswith("graphiques"):
    st.title("📊 Graphiques dynamiques et interactifs")

    # Démo fictive si il n'ya pas d'upload de fichier
    if not "df" in st.session_state:
        st.warning(
            "⚠️ Importez d’abord un fichier sur la page d’accueil ou utilisez la démo."
        )
        st.write("Voici une démo des graphiques")
        st.dataframe(
            pd.DataFrame({"Exemple": ["A", "B", "C"], "Valeurs": [10, 20, 15]})
        )
        st.bar_chart(pd.DataFrame({"Valeurs": [10, 20, 15]}, index=["A", "B", "C"]))

    # Vraie visualision apres juste upload
    else:
        df = st.session_state["df"].copy()

        # detection des differents types de collones et on les transforme en liste
        cols_num = df.select_dtypes(include="number").columns.tolist()
        cols_str = df.select_dtypes(exclude="number").columns.tolist()

        st.subheader("🎛️ Configuration du graphique")

        # selection des colonnes pour visualisation
        col_x = st.selectbox("Choisir une colonne catégorielle (X)", df.columns)
        col_y = st.selectbox("Choisir une colonne numérique (Y)", df.columns)
        fig = Visualizer(df)  # on creer un objet  fig pour la visualisation

        if col_x in cols_num and col_y in cols_str:
            fig._bar_chart(
                col1=col_y, col2=col_x, title=f"barchart de {col_x} par {col_y}"
            )
            fig._pie_chart(col1=col_y, col2=col_x, title="part de chaque variable")
        elif col_x in cols_num and col_y in cols_num:
            fig._scatter(
                col1=col_x,
                col2=col_y,
                title=f"Scatter de {col_x} par {col_y}",
                colsize=cols_num[0],
            )
            if st.button("show corr"):
                st.info(
                    f"la correlation entre la colonne {col_x} et {col_y} est de {df[[col_x,col_y]].corr()*100}"
                )

            fig._scatter(
                col1=col_y,
                col2=col_x,
                title=f"Scatter de {col_y} par {col_x}",
                colsize=cols_num[0],
            )

        elif col_x in cols_str and col_y in cols_str:
            fig._hist_chart(col=col_x, title=f"distribution de la variable {col_x}")
            fig._hist_chart(col=col_y, title=f"distribution de la variable {col_y}")
        else:
            st.info("soyez sur que la ciollone cible est celle choisie en premiere")

        # --- Mémoire session_state ---
        st.session_state["last_graph"] = {"x": col_x, "y": col_y}
        st.success(f"🧠 Mémoire sauvegardée : graphique {col_y} par {col_x}")
# ==========================================
# PAGE 3 : ANALYSE DÉTAILLÉE
# ==========================================
elif section.endswith("Analyse détaillée"):
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
            else st.info("Aucune collone numérique trouvée")
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
                "Doublons": info_calculée["Doublons"],
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

            # st.pie_chart(df_group.set_index(group_col)["mean"])

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
elif section.endswith("Synthèse IA"):
    st.title("🤖 Mode Intelligence Artificielle")

    # Simulation IA futuriste
    st.info(
        "Cette section est en cours de développement. Bientôt, vos calculs Pandas et vos modèles IA seront injectés ici pour générer des synthèses automatiques."
    )

    # Démo fictive pour rassurer l'utilisateu    st.subheader("🎬 Démonstration IA fictive")
    salutation = st.text_input("User : ")
    if salutation:
        st.write(
            "**IA DataBot :** Bonjour Ruphin 👋, j’ai analysé ton DataFrame. Voici mes observations :"
        )
        question = st.text_input("Ruphin : ")
        if question:
            st.success(
                "✅ Les données montrent une tendance positive sur la colonne 'Ventes'."
            )
            st.warning(
                "⚠️ Attention : la colonne 'Croissance (%)' présente des valeurs manquantes qui pourraient fausser l'analyse."
            )
            st.info(
                "💡 Pas pour l'insatant bientôt, cette section utilisera une clé API pour générer des synthèses réelles basées sur vos données."
            )
# ==========================================
# PAGE 5 : COLLABORATION
# ==========================================
elif section.endswith("collaboration"):
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
        "**IA DataBot :** Alice, imagine que tu viens d’exporter ton rapport. Voici à quoi ca ressemble :"
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
    st.write(demo_collab.to_dict())
    st.write(
        "**DataBot :** mais avec nos outils  regarde un exemple de ce que ça donne \n et sans mentir la comparaison est gigantesque car ça c'est plus lisible\nmoderne et adapté à tes besoins tu peux manipuler ce tableau le filtrer dans l'app et meme l'enregistre selon tes goûts "
    )
    st.dataframe(demo_collab, use_container_width=True)
    st.write(
        "**DataBot : ** Et voici à quoi ressemble un code de data pour faire de bonnes analyses plutot simple n'est ce pas\n car avec nos outils vous n'allez pas juste les utiliser mais vous aller connaitre leurs structures internes et meme les modifier selon vos goûts"
    )
    st.code(
        "import pandas as pd\nimport numpy as np\nimport plotly.express as px\ndf = pd.DataFrame(demo_collab)\ndf['contributions'] = np.linspace(1,10,7)\nfig = px.bar(df,x='Utilisateur',y='contributions'title='Les contributeurs et leurs contributions')\nfig.show()",
        language="python",
    )

    st.info(
        "Fonctionnalités en cours de développement. L'objectif est de permettre aux gens de collaborer en temps réel sur leurs fichiers."
    )
