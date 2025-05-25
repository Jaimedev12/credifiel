import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'dataDomiciliacion/ProcessConfig_202505161644.csv'

"""
catbank_202505161900.csv:
    id virtual de cada banco

CatMotivosRespuestaBanco_202505161627.csv:
    Motivos de respuesta para un cobro

CatStatusOptDirectDebit_202505161318:
    Códigos de estatus de un cobro



"""

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Show basic info
print("Basic Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Show summary statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Show number of missing values per column
print("\nMissing Values per Column:")
print(df.isnull().sum())

# Show most frequent values for each column
print("\nMost Frequent Values per Column:")
for col in df.columns:
    print(f"{col}: {df[col].mode()[0]}")