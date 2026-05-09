import pandas as pd

def load_data(file_path):
    """
    reads the CSV file then returns a dataframe.
    """              
    # read CSV
    df = pd.read_csv(file_path)

    # erase erroneous data
    df = df.dropna()

    return df