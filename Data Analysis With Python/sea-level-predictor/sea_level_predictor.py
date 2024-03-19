import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = list(range(1880, 2051))
    line_of_best_fit_all = [slope * year + intercept for year in years]
    plt.plot(years, line_of_best_fit_all, label='All Data')

    # Create second line of best fit
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df['Year'][df['Year'] >= 2000],
                                                                                      df['CSIRO Adjusted Sea Level'][
                                                                                          df['Year'] >= 2000])
    years_2000 = list(range(2000, 2051))
    line_of_best_fit_2000 = [slope_2000 * year + intercept_2000 for year in years_2000]
    plt.plot(years_2000, line_of_best_fit_2000, label='2000 Onward')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
