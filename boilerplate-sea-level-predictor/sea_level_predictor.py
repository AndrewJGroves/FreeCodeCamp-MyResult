import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv",parse_dates=True)

    # Create scatter plot
    x=df["Year"]
    y=df["CSIRO Adjusted Sea Level"]
    plt.scatter(x,y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x,y)
    line_x = np.arange(x.min(), 2050)
    line_y = slope*line_x + intercept
    plt.plot(line_x, line_y,label='Full')

    # Create second line of best fit
    x1=df.loc[df["Year"] >= 2000 , 'Year']
    y1=df.loc[df["Year"] >= 2000 , 'CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x1,y1)
    line_x1 = np.arange(x1.min(), 2050)
    line_y1 = slope*line_x1 + intercept
    plt.plot(line_x1, line_y1,label='Ti')


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.savefig('sea_level_plot.png')
    return plt.gca()