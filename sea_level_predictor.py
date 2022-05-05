import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    # Create scatter plot


    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(x=x, y=y)



    # Create first line of best fit
    first = linregress(x=x, y=y)

    predict_x = pd.Series([i for i in range(1880,2051)])
    plt.plot(predict_x, first.intercept + first.slope*predict_x, color='red')

    # Create second line of best fit

    new_df = df[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']


    second = linregress(x=new_x, y=new_y)
    new_predict_x = pd.Series([i for i in range(2000,2051)])
    plt.plot(new_predict_x, second.intercept + second.slope*new_predict_x, color='blue')

    # Add labels and title
    
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()