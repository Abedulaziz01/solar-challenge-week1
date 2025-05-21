import os
import pandas as pd

def load_data():
    # Get path relative to this file (utils.py)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming Data folder is at the project root level, one directory above 'app'
    project_root = os.path.abspath(os.path.join(base_dir, '..'))
    data_folder = os.path.join(project_root, 'Data')

    print("Looking for data folder at:", data_folder)

    if not os.path.exists(data_folder):
        raise FileNotFoundError(f"Data folder not found: {data_folder}")

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
