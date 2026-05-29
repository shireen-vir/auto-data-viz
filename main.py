class AutoDataViz:
    """
    A class used to automate the data visualization process.

    Attributes:
    ----------
    data : DataFrame
        The input data.

    Methods:
    -------
    visualize()
        Creates a visualization based on the input data.
    """

    def __init__(self, data):
        self.data = data

    def visualize(self):
        import matplotlib.pyplot as plt
        import seaborn as sns

        plt.figure(figsize=(10, 8))
        sns.heatmap(self.data.corr(), annot=True)
        plt.title('Correlation Heatmap')
        plt.show()


import pandas as pd

def main():
    data = pd.read_csv('data.csv')
    auto_viz = AutoDataViz(data)
    auto_viz.visualize()


if __name__ == "__main__":
    main()