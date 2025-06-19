import pandas as pd

def filter_unique_titles(file1, file2, column1, column2, output_file):
    """
    This function compares two CSV files and filters the unique titles from the second file
    that do not exist in the first file.
    
    Parameters:
    - file1: str, path to the first CSV file.
    - file2: str, path to the second CSV file.
    - column1: str, the column name for titles in the first CSV file.
    - column2: str, the column name for titles in the second CSV file.
    - output_file: str, path to save the filtered CSV file with unique titles.
    """
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Convert titles to lowercase for case-insensitive comparison
    df1[column1] = df1[column1].str.lower()
    df2[column2] = df2[column2].str.lower()

    # Extract titles from both DataFramesÂ
    titles_df1 = set(df1[column1])
    titles_df2 = set(df2[column2])

    # Find titles in the second DataFrame that do not exist in the first DataFrame
    unique_titles = titles_df2.difference(titles_df1)

    # Filter the second DataFrame to keep only rows with titles that are unique
    df2_unique = df2[df2[column2].isin(unique_titles)]

    # Write the filtered DataFrame back to a new CSV file
    df2_unique.to_csv(output_file, index=False)

    print(f"Filtered unique titles saved to {output_file}")

# Example usage
file1 = 'path_to_first_file.csv'
file2 = 'path_to_second_file.csv'
column1 = 'Title'  # Column name for titles in the first file
column2 = 'title'  # Column name for titles in the second file
output_file = 'filtered_unique_titles.csv'

filter_unique_titles(file1, file2, column1, column2, output_file)
