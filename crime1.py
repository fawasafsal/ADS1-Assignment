import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('US_Crime_Rates_1960_2014.csv')


def multiple_crime_rates():
    # Line plot for multiple crime rates
    plt.figure(figsize=(12, 8))

    plt.plot(data['Year'], data['Violent'], label='Violent')
    plt.plot(data['Year'], data['Property'], label='Property')
    plt.plot(data['Year'], data['Murder'], label='Murder')
    plt.plot(data['Year'], data['Robbery'], label='Robbery')

    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.title('Crime Rates Over Time (1960-2014)')
    plt.legend()
    plt.grid(True)
    plt.show()


def total_crimes_selected_years():
    # Selecting specific years for comparison
    selected_years = [1980, 1990, 2000, 2010, 2014]
    selected_data = data[data['Year'].isin(selected_years)]

    # Plotting a bar chart for total crimes in selected years
    plt.figure(figsize=(10, 6))
    plt.bar(selected_data['Year'], selected_data['Total'], color='skyblue')

    plt.xlabel('Year')
    plt.ylabel('Total Number of Crimes')
    plt.title('Total Crimes in Selected Years (1980, 1990, 2000, 2010, 2014)')
    plt.grid(axis='y')
    plt.show()


def crime_types_2014():
    # Selecting data for the year 2014
    crime_types = ['Violent', 'Property', 'Murder']
    crime_counts_2014 = data[data['Year'] ==
                             2014][crime_types].values.flatten()

    # Plotting a pie chart for crime types in the year 2014
    plt.figure(figsize=(8, 8))
    plt.pie(crime_counts_2014, labels=crime_types, autopct='%1.1f%%',
            startangle=140, colors=['lightcoral', 'lightgreen', 'lightskyblue'])
    plt.title('Distribution of Crime Types in 2014')
    plt.show()


# Call the functions to produce the respective visualizations
multiple_crime_rates()
total_crimes_selected_years()
crime_types_2014()
