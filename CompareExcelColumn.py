import pandas as pd


def compare_columns(file_path, sheet_name, column_c, column_e):
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Extract values from columns C and E
    values_c = set(df[column_c])
    values_e = set(df[column_e])

    # Find values in column E that are not present in column C
    missing_values = values_e - values_c
    print(missing_values.__len__())
    print("Missing values in column E:")
    for value in missing_values:
        print(value)


# Example usage:
file_path = "C:/Users/amin/Documents/Worksheet -Dilruba Apu - 11-2-24.xlsx"
sheet_name = "published"
column_c = "Mongo"
column_e = "SQL"
compare_columns(file_path, sheet_name, column_c, column_e)
