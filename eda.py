import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your CSV file
file_path = 'insurance.csv'

try:
    # Load the dataset into a DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    print(df.head())

    # Display summary statistics
    print("\nSummary statistics:")
    print(df.describe())

    # Display information about the dataset
    print("\nInformation about the dataset:")
    print(df.info())

    # Check for missing values
    print("\nMissing values in each column:")
    print(df.isnull().sum())

    # Display the distribution of numerical columns
    print("\nDistribution of numerical columns:")
    df.hist(bins=30, figsize=(10, 10))
    plt.show()

    # Display the correlation matrix
    print("\nCorrelation matrix:")
    corr_matrix = df.corr()
    print(corr_matrix)

    # Plot a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix Heatmap')
    plt.show()

    # Plot pairplot for numerical columns
    print("\nPairplot of numerical columns:")
    sns.pairplot(df)
    plt.show()

except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
