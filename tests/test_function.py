import plotly.express as px
import pandas as pd
import numpy as np
import time


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
        fig.show()
        return fig

    # methode pour histogramme
    def _hist_chart(self, col_num: str, nbins: int = 6):
        fig = px.histogram(self.df, x=col_num, nbins=nbins, color=col_num)
        fig.show()
        return fig


file = "F:\projet_programs\Datascience-for-begginers\Wine Quality Classification\data\winequality-red.csv"

df = pd.read_csv(file)
# donner le nombre des lignes et collones pour mieux savoir les dimmensiosns du dataframe
print(df.shape)

if df.shape[0] > 1000:
    df = df.head(1000)
else:
    df = df.copy()
col = df.columns[0]
# print(int(df[col].mean()))

dataframe = Visualizer(df)
# dataframe._scatter_chart("fixed_acidity", "volatile_acidity", "visualisation")


def diff(a, b):
    print(np.mean(df[a]) - np.mean(df[b]))


start = time.time()

diff("fixed_acidity", "volatile_acidity")

end = time.time()

print(end - start)
