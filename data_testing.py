import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

if __name__ == '__main__':
    # This file is used only for testing data generation
    data = pd.read_csv('voters.csv')
    fig = px.box(data, 'Income')
    fig.show()
    print(data['Income'].mean())
