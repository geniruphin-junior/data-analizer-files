import plotly.express as px
import plotly.graph_objects as go


# classe principale des graphiques basiques
class Visualizer:
    def __init__(self, dataFrame, title):
        self.dataFrame = dataFrame
        self.title = title

    # Méthode pour scatter
    def _scatter(self, col1: str, col2: str, colsize: str) -> str:
        fig = px.scatter(self.dataFrame, x=col1, y=col2, size=colsize)
        fig.show()
        return fig

    # Méthode pour barres
    def _bar_chart(self, col1: str, col2: str):
        fig = px.bar(self.dataFrame, x=col1, y=col2, color=col1, title=self.title)
        fig.show()
        return fig

    # Méthodes pour line(evolution d'une variable)
    def _line_chart(self, col1: str, col2: str):
        fig = px.line(self.dataFrame, x=col1, y=col2, title=self.title)
        fig.show()
        return fig

    # Méthode pour histogramme pour la mesure des variables d'un datatest
    def _hist_chart(self, col: str, bins=10):
        fig = px.histogram(
            self.dataFrame, x=col, title=self.title, color=col, nbins=bins
        )
        fig.show()
        return fig

    # Méthode pour la part de chaque variable
    def _pie_chart(self, col1: str, col2: str):
        fig = px.pie(self.dataFrame, names=col1, values=col2, title=self.title)
        fig.show()
        return fig
