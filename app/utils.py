import pandas as pd
import os

def load_data():
    # Define the path to your data folder
    data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')

    # List CSVs and create a dictionary
    csv_files = {
        'benin': 'benin_cleaned.csv',
        'togo': 'togo_cleaned.csv',
        'seraleon': 'sierraleone_cleaned.csv',
       
    }

    data_dict = {}

    for country, file in csv_files.items():
        file_path = os.path.join(data_folder, file)
        df = pd.read_csv(file_path)
        df['Country'] = country
        data_dict[country] = df

    # Combine all countries' data
    combined_df = pd.concat(data_dict.values(), ignore_index=True)

    return combined_df, data_dict
