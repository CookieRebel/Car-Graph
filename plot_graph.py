import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize, LinearSegmentedColormap

# Function to list all .xlsx files in the current directory
def list_excel_files():
    files = [f for f in os.listdir('.') if f.endswith('.xlsx') and not f.startswith('~')]
    return files

# Function to plot price vs year with mileage as color
def plot_price_vs_year(df_cars, name, types_identifier, unique_types, symbols, cmap):
    plt.figure(figsize=(12, 8))
    norm = Normalize(vmin=0, vmax=df_cars['Mileage (km)'].max())

    sc = None
    for unique_type in unique_types:
        subset = df_cars[df_cars[types_identifier] == unique_type]
        sc = plt.scatter(subset['Year'], subset['Price ($AUD)'], label=unique_type, marker=symbols[unique_type], c=subset['Mileage (km)'], cmap=cmap, norm=norm, s=100, alpha=0.6)

    plt.colorbar(sc, label='Mileage (km)')

    # Fit and plot best fit line and curve
    x = df_cars['Year']
    y = df_cars['Price ($AUD)']
    plot_best_fit_lines(x, y)

    # Customizing the x-axis and y-axis
    plt.xticks(ticks=range(df_cars['Year'].min(), df_cars['Year'].max() + 1), labels=[str(year)[-2:] for year in range(df_cars['Year'].min(), df_cars['Year'].max() + 1)])
    plt.yticks(range(int(df_cars['Price ($AUD)'].min() // 5000 * 5000), int(df_cars['Price ($AUD)'].max() // 5000 * 5000 + 5000), 5000))

    plt.xlabel('Model Year')
    plt.ylabel('Price ($AUD)')
    plt.title(f'Model Year vs Price for {name} (Color indicates mileage)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()

# Function to plot price vs mileage with year as color
def plot_price_vs_mileage(df_cars, name, types_identifier, unique_types, symbols, cmap):
    plt.figure(figsize=(12, 8))
    norm = Normalize(vmin=df_cars['Year'].min(), vmax=df_cars['Year'].max())

    sc = None
    for unique_type in unique_types:
        subset = df_cars[df_cars[types_identifier] == unique_type]
        sc = plt.scatter(subset['Mileage (km)'], subset['Price ($AUD)'], label=unique_type, marker=symbols[unique_type], c=subset['Year'], cmap=cmap, norm=norm, s=100, alpha=0.6)

    plt.colorbar(sc, label='Year')

    # Fit and plot best fit line and curve
    x = df_cars['Mileage (km)']
    y = df_cars['Price ($AUD)']
    plot_best_fit_lines(x, y)

    plt.xticks(range(int(df_cars['Mileage (km)'].min() // 20000 * 20000), int(df_cars['Mileage (km)'].max() // 20000 * 20000 + 20000), 20000))
    plt.yticks(range(int(df_cars['Price ($AUD)'].min() // 5000 * 5000), int(df_cars['Price ($AUD)'].max() // 5000 * 5000 + 5000), 5000))

    plt.xlabel('Mileage (km)')
    plt.ylabel('Price ($AUD)')
    plt.title(f'Mileage vs Price for {name} (Color indicates year)')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()

# Function to plot best fit line and curve
def plot_best_fit_lines(x, y):
    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)
    best_fit_line = polynomial(x)
    plt.plot(x, best_fit_line, color='#ADD8E6', linestyle='dashed', linewidth=1, label='Best fit line')

    curve_coefficients = np.polyfit(x, y, 2)
    curve_polynomial = np.poly1d(curve_coefficients)
    best_fit_curve = curve_polynomial(x)
    plt.plot(np.sort(x), curve_polynomial(np.sort(x)), color='blue', linestyle='dotted', linewidth=1, label='Best fit curve')

types_identifier = 'Seller Type'
# List .xlsx files and ask the user to pick one
excel_files = list_excel_files()
if not excel_files:
    print("No Excel files found in the current directory.")
else:
    print("Available Excel files:")
    for idx, file in enumerate(excel_files):
        print(f"{idx + 1}: {file}")

    file_index = int(input("Please enter the number of the Excel file to use: ")) - 1
    if file_index < 0 or file_index >= len(excel_files):
        print("Invalid selection. Exiting.")
    else:
        file_path = excel_files[file_index]

        # Name
        name = input("What is the name of the car we are plotting? ")

        # Load the data from the spreadsheet
        df_cars = pd.read_excel(file_path)

        # Define dynamic symbols for different sources
        unique_types = df_cars[types_identifier].unique()
        symbols_list =  ['o', 's', '^', 'd', 'v', 'x', 'P', '*', 'h', 'D'] # Extend this list if more symbols are needed

        # Assign symbols dynamically
        symbols = {source: symbols_list[i] for i, source in enumerate(unique_types)}

        # Define custom colormap
        cmap = LinearSegmentedColormap.from_list("custom_cmap", ["green", "yellow", "red", "purple"])

        # Ask user which graph to generate
        graph_type = input("Which graph do you want to generate? (1 for price vs year, 2 for price vs mileage): ")
        if graph_type == '1':
            plot_price_vs_year(df_cars, name, types_identifier, unique_types, symbols, cmap)
        elif graph_type == '2':
            plot_price_vs_mileage(df_cars, name, types_identifier, unique_types, symbols, cmap)
        else:
            print("Invalid selection. Exiting.")
