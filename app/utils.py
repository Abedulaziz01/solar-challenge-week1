import pandas as pd
import os

def load_data():
    # Use current working directory + data
    data_folder = os.path.join(os.getcwd(), 'data')

    # Check if path exists
    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"Data folder not found: {data_folder}")

    # Load each country's file
    csv_files = {
        'TOgo': 'togo_cleaned.csv',
        'Benin': 'benin_cleaned.csv',
        'Sierra Leone': 'sierraleone_cleaned.csv',
   
    }

    data_dict = {}

    for country, file in csv_files.items():
        file_path = os.path.join(data_folder, file)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")

        df = pd.read_csv(file_path)
        df['Country'] = country
        data_dict[country] = df

    combined_df = pd.concat(data_dict.values(), ignore_index=True)

    return combined_df, data_dict
