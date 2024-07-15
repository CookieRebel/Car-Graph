import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize, LinearSegmentedColormap

# Function to list all .xlsx files in the current directory
def list_excel_files():
    files = [f for f in os.listdir('.') if f.endswith('.xlsx') and not f.startswith('~')]
    return files

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

        # Define custom colormap for mileage
        cmap = LinearSegmentedColormap.from_list("mileage_cmap", ["green", "yellow", "red", "purple"])

        # Plot the data with best fit line and color indicating mileage
        plt.figure(figsize=(12, 8))

        norm = Normalize(vmin=0, vmax=df_cars['Mileage (km)'].max())

        sc = None
        for unique_type in unique_types:
            subset = df_cars[df_cars[types_identifier] == unique_type]
            sc = plt.scatter(subset['Year'], subset['Price ($AUD)'], label=unique_type, marker=symbols[unique_type], c=subset['Mileage (km)'], cmap=cmap, norm=norm, s=100, alpha=0.6)

        plt.colorbar(sc, label='Mileage (km)')

        # Fit a line to the data
        x = df_cars['Year']
        y = df_cars['Price ($AUD)']
        coefficients = np.polyfit(x, y, 1)
        polynomial = np.poly1d(coefficients)
        best_fit_line = polynomial(x)

        # Fit a curve to the data (2nd degree polynomial)
        curve_coefficients = np.polyfit(x, y, 2)
        curve_polynomial = np.poly1d(curve_coefficients)
        best_fit_curve = curve_polynomial(x)

        # Plot the best fit line
        plt.plot(x, best_fit_line, color='#ADD8E6', linestyle='dashed', linewidth=1, label='Best fit line')

        # Plot the best fit curve
        plt.plot(np.sort(x), curve_polynomial(np.sort(x)), color='blue', linestyle='dotted', linewidth=1, label='Best fit curve')

        # Customizing the x-axis and y-axis
        plt.xticks(ticks=range(df_cars['Year'].min(), df_cars['Year'].max() + 1), labels=[str(year)[-2:] for year in range(df_cars['Year'].min(), df_cars['Year'].max() + 1)])
        plt.yticks(range(int(df_cars['Price ($AUD)'].min() // 10000 * 10000), int(df_cars['Price ($AUD)'].max() // 10000 * 10000 + 10000), 10000))

        plt.xlabel('Model Year')
        plt.ylabel('Price ($AUD)')
        plt.title(f'Model Year vs Price for {name} (Color indicates mileage)')
        plt.legend()
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        plt.show()
