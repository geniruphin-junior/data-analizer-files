import plotly.express as px
import plotly.graph_objects as go

cyberpunk_colors = [
    "#FF007F",
    "#00F0FF",
    "#9D00FF",
    "#39FF14",
    "#FF00F0",
    "#FF0033",
]


# classe principale des graphiques basiques
class Visualizer:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    # Méthode pour scatter
    def _scatter(
        self,
        col1: str,
        col2: str,
        title: str,
        colsize: str,
        template="plotly_dark",
        colors=cyberpunk_colors,
    ) -> str:
        fig = px.scatter(
            self.dataFrame,
            x=col1,
            y=col2,
            size=colsize,
            template=template,
            color_discrete_sequence=colors,
        )

    # Méthode pour barres
    def _bar_chart(
        self,
        col1: str,
        col2: str,
        title: str,
        template="plotly_dark",
        colors=cyberpunk_colors,
    ):
        fig = px.bar(
            self.dataFrame,
            x=col1,
            y=col2,
            title=title,
            color=col1,
            template=template,
            color_discrete_sequence=colors,
        )

    # Méthodes pour line(evolution d'une variable)
    def _line_chart(
        self,
        col1: str,
        col2: str,
        title: str,
        template="plotly_dark",
        colors=cyberpunk_colors,
    ):
        fig = px.line(
            self.dataFrame,
            x=col1,
            y=col2,
            title=title,
            template=template,
            color_discrete_sequence=colors,
        )

    # Méthode pour histogramme pour la mesure des variables d'un datatest
    def _hist_chart(
        self,
        col: str,
        title: str,
        bins=10,
        template="plotly_dark",
        colors=cyberpunk_colors,
    ):
        fig = px.histogram(
            self.dataFrame,
            x=col,
            title=title,
            color=col,
            nbins=bins,
            template=template,
            color_discrete_sequence=colors,
        )

    # Méthode pour la part de chaque variable
    def _pie_chart(self, col1: str, col2: str, title: str, template="plotly_dark"):
        fig = px.pie(
            self.dataFrame, names=col1, values=col2, title=title, template=template
        )


"""fig1 = px.bar(
    demo_df,
    x="Langage",
    y="Utilisateurs GitHub (k)",
    color="Langage",
    title="🚀 Popularité GitHub par langage",
    template="plotly_dark",
    color_discrete_sequence=cyberpunk_colors,
)"""
