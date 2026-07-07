import plotly.express as px
import pandas as pd


# creation de la classe de visualisation
class Visualizer:
    def __init__(
        self, df
    ):  # j'essaie avec le dataframe comme outils pour le constructeur
        self.df = df

    # methode pour barchart
    def _bar_chart(self, col_num: str, col_str: str, title: str) -> str:
        fig = px.bar(df, x=col_str, y=col_str, title=title, color=col_str)
        fig.show()
        return fig

    # methode pour pie_chart
    def _pie_chart(self, names: str, values: int):
        fig = px.pie(self.df, names=names, values=values, title=title)
        fig.show()
        return fig

    # methode pour linechart
    def _line_chart(self, col_num: str, col_str: str, title: str) -> str:
        fig = px.line(self.df, x=col_str, y=col_num, title=title)
        fig.show()
        return fig

    # methode pour  scatter chart
    def _scatter_chart(self, col_num: str, col_str: str, title: str) -> str:
        fig = px.scatter(self.df, x=col_str, y=col_num, title=title)
        fig.show
        return fig

    # methode pour histogramme
    def _hist_chart(self, col_num: str, nbins: int = 6):
        fig = px.histogram(self.df, x=col_num, nbins=nbins, color=col_num)
        fig.show()
        return fig


df = pd.DataFrame({"classe": ["ruphin", "jules", "rodri"], "points": [34, 45, 67]})
dataframe = Visualizer(df)
dataframe._hist_chart("points", 4)
