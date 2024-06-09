import pandas as pd

def read_excel_to_df(path):
    """
    Read an Excel file with pandas and store the data in a DataFrame.
    
    Parameters
    ----------
    path : str or other object for read_excel filepath parameter
        Path to Excel file with data
    
    Returns
    -------
    DataFrame
        df with data from the Excel file
    """
   
    df = pd.read_excel(path)
    return df
