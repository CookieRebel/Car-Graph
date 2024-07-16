# Car Price Analysis Script

This script allows you to visualize car price data from an Excel file. You can generate scatter plots that show the relationship between car price and either model year or mileage. The script also allows you to prefill the car name based on the filename and saves the generated plots with a specific naming convention.

## Features

- List all `.xlsx` files in the current directory.
- Prefill the car name based on the filename.
- Generate scatter plots for:
  - Price vs. Year with mileage as the color.
  - Price vs. Mileage with year as the color.
- Save the generated plots with a specific filename format including the date.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/CookieRebel/car-price-plotter.git
    cd car-price-plotter
    ```

2. **Install the required Python packages**:
    ```bash
    pip install pandas matplotlib numpy openpyxl
    ```

## Usage

1. **Ensure your car price data is in an Excel file (`.xlsx` format) in the current directory**. The filename should follow the format: `car_name_year.xlsx`, for example, `mini_s_convertible_2015+.xlsx`.

2. **Run the script**:
    ```bash
    python car_price_analysis.py
    ```

3. **Follow the prompts**:
    - Select the Excel file you want to analyze by entering the corresponding number.
    - The script will prefill the car name based on the filename. You can either accept the suggested name or enter a new one.
    - Choose the type of graph you want to generate:
      - Enter `1` for a Price vs. Year graph.
      - Enter `2` for a Price vs. Mileage graph.

4. **View and save the plots**:
    - The generated plot will be displayed. You can save the plot using the save icon in the plot window. The suggested filename, including the date, will be set automatically.

## Excel File Format

The Excel file should have the following columns:

- **Year**: The model year of the car.
- **Model**: The make and model of the car.
- **Variant**: The variant of the car model.
- **Description**: A description of the car.
- **Price ($AUD)**: The price of the car in Australian dollars.
- **Mileage (km)**: The mileage of the car in kilometers.
- **Seller Type**: The type of seller (e.g., Private, Dealer).
- **Location**: The location of the seller.
- **Source**: The source where the car listing was found.
- **Comment**: Additional comments about the car.
- **Comment 2**: Additional comments about the car (second comment field).

### Example Row

| Year | Model       | Variant  | Description                   | Price ($AUD) | Mileage (km) | Seller Type | Location | Source  | Comment | Comment 2 |
|------|-------------|----------|-------------------------------|--------------|--------------|-------------|----------|---------|---------|-----------|
| 1995 | Porsche 911 | 993      | Carrera Manual R              | 148998       | 93000        | Private     | NaN      | Carsales| NaN     | NaN       |

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy
- openpyxl

## License

This project is licensed under the MIT License.

