import plotly.express as px
import plotly.graph_objects as go
from color import cyberpunk_colors


# classe principale des graphiques basiques
class Visualizer:
    def __init__(self, dataFrame, title):
        self.dataFrame = dataFrame
        self.title = title

    # Méthode pour scatter
    def _scatter(
        self, col1: str, col2: str, colsize: str, template="plotly_dark"
    ) -> str:
        fig = px.scatter(
            self.dataFrame, x=col1, y=col2, size=colsize, template=template
        )
        fig.show()
        return fig

    # Méthode pour barres
    def _bar_chart(self, col1: str, col2: str, template="plotly_dark"):
        fig = px.bar(
            self.dataFrame,
            x=col1,
            y=col2,
            color=col1,
            title=self.title,
            template=template,
        )
        fig.show()
        return fig

    # Méthodes pour line(evolution d'une variable)
    def _line_chart(self, col1: str, col2: str, template="plotly_dark"):
        fig = px.line(
            self.dataFrame, x=col1, y=col2, title=self.title, template=template
        )
        fig.show()
        return fig

    # Méthode pour histogramme pour la mesure des variables d'un datatest
    def _hist_chart(self, col: str, bins=10, template="plotly_dark"):
        fig = px.histogram(
            self.dataFrame,
            x=col,
            title=self.title,
            color=col,
            nbins=bins,
            template=template,
        )
        fig.show()
        return fig

    # Méthode pour la part de chaque variable
    def _pie_chart(
        self,
        col1: str,
        col2: str,
        template="plotly_dark",
    ):
        fig = px.pie(
            self.dataFrame, names=col1, values=col2, title=self.title, template=template
        )
        fig.show()
        return fig
