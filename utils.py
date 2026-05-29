import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Loads data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(file_path)

def plot_data(data, x_axis, y_axis):
    """
    Plots the data using seaborn.

    Args:
        data (pd.DataFrame): Data to plot.
        x_axis (str): Name of the column for the x-axis.
        y_axis (str): Name of the column for the y-axis.
    """
    sns.set()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=x_axis, y=y_axis, data=data)
    plt.title('Auto Data Visualization')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()

def main():
    """
    Main function for auto-data-viz.

    This function loads data from a CSV file and plots it using seaborn.
    """
    file_path = 'data.csv'  # replace with your file path
    x_axis = 'column1'  # replace with your column name
    y_axis = 'column2'  # replace with your column name
    data = load_data(file_path)
    plot_data(data, x_axis, y_axis)

if __name__ == '__main__':
    main()