import logging
import pandas as pd
import yaml
import re

################
# File Reading #
################

def read_config_file(filepath):
    """
    Reads a YAML configuration file and returns the data.
    """
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)
            return None

def replacer(string, char):
    """
    Replace multiple occurrences of a character in a string with a single occurrence.
    """
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def col_header_val(df, table_config):
    """
    Standardizes column names by:
    - Lowercasing all column names
    - Replacing non-word characters with underscores
    - Removing extra underscores
    - Checking column name and length validation against the YAML config
    """
    df.columns = df.columns.str.lower()  # Lowercase all column names
    df.columns = df.columns.str.replace('[^\w]', '_', regex=True)  # Replace non-word chars with '_'
    df.columns = list(map(lambda x: x.strip('_'), list(df.columns)))  # Strip underscores at both ends
    df.columns = list(map(lambda x: replacer(x, '_'), list(df.columns)))  # Remove extra underscores

    expected_col = list(map(lambda x: x.lower(), table_config['columns']))
    expected_col.sort()

    # Sort columns of the dataframe
    df.columns = list(map(lambda x: x.lower(), list(df.columns)))
    df = df.reindex(sorted(df.columns), axis=1)

    if len(df.columns) == len(expected_col) and list(expected_col) == list(df.columns):
        print("Column name and column length validation passed.")
        return 1
    else:
        print("Column name and column length validation failed.")
        mismatched_columns_file = list(set(df.columns).difference(expected_col))
        print("Columns in file but not in YAML:", mismatched_columns_file)
        missing_yaml_file = list(set(expected_col).difference(df.columns))
        print("Columns in YAML but not in file:", missing_yaml_file)
        logging.info(f'df columns: {df.columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0


def convert_to_datetime(df, column_name):
    """
    Convert a specified column in the DataFrame to datetime format.
    """
    try:
        df[column_name] = pd.to_datetime(df[column_name])
        print(f"Successfully converted {column_name} to datetime.")
    except Exception as e:
        print(f"Error converting {column_name} to datetime: {e}")
    return df


def check_missing_values(df):
    """
    Check for missing values in the DataFrame.
    """
    missing_values = df.isnull().sum()
    print(f"Missing values:\n{missing_values}")
    return missing_values


def summary_statistics(df):
    """
    Generate summary statistics for the DataFrame.
    """
    stats = df.describe()
    print(f"Summary statistics:\n{stats}")
    return stats
