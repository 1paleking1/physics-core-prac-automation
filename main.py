import matplotlib.pyplot as plt
import numpy as np


class ErrorBars:
    
    def __init__(self, x, y, xquant, yquant):
        self.x = x
        self.y = y
        self.xquant = xquant
        self.yquant = yquant

    def set_uncertainty(self, quant):
        if quant == "time":
            self.unc

    


class ResultsGraph:

    def __init__(self, x, y, title, xlabl, ylabl):
        self.x = x
        self.y = y
        self.title = title
        self.xlabl = xlabl
        self.ylabl = ylabl
        
    def plot_graph(self):

        plt.title(self.title)

        plt.xlabel(self.xlabl)
        plt.ylabel(self.ylabl)

        plt.scatter(self.x, self.y, marker="x", s=25)

        plt.plot(np.unique(self.x), np.poly1d(np.polyfit(self.x, self.y, 1))(np.unique(self.x))) # line of best fit

        plt.show()


g = ResultsGraph(
    [1, 2, 3],
    [1, 2, 3],
    "title",
    "x",
    "y"
)

g.plot_graph()

