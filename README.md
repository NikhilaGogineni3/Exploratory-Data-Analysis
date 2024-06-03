
# Exploratory Data Analysis (EDA) Project Documentation

## Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on various datasets to uncover insights, identify patterns, and understand the underlying structure of the data. EDA is a crucial step in the data analysis process that helps in summarizing the main characteristics of the data, often with visual methods.

## Datasets Used

In this project, the following datasets were analyzed:

1. **Netflix Movies**: A dataset containing information about movies available on Netflix, including their titles, genres, release years, and ratings.
2. **Housing**: A dataset with various attributes of houses, including the number of bedrooms, bathrooms, square footage, and prices.
3. **Boston Housing**: The famous Boston housing dataset with features such as crime rate, number of rooms, property tax rate, etc., used for predicting house prices.
4. **World Happiness Report**: A dataset that includes happiness scores and rankings of countries around the world, along with various factors contributing to happiness.
5. **Mall Customers**: A dataset with information about customers, including their age, gender, income, and spending score, often used for customer segmentation.
6. **Insurance**: A dataset containing information about insurance policyholders, including their age, gender, BMI, number of children, smoking status, and charges.

## Installation and Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/NikhilaGogineni3/Exploratory-Data-Analysis
    cd Exploratory-Data-Analysis
    ```

2. **Create and Activate Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install Required Libraries**:
    ```sh
    pip install pandas numpy matplotlib seaborn
    ```

## EDA Steps

The following steps were performed in the EDA script (`eda.py`):

1. **Import Libraries**:
    ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    ```

2. **Load Dataset**:
    ```python
    df = pd.read_csv('path_to_your_dataset.csv')
    ```

3. **Basic Data Exploration**:
    ```python
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.columns)
    print(df.isnull().sum())
    ```

4. **Data Visualization**:
    - **Histograms**:
        ```python
        df.hist(bins=50, figsize=(20,15))
        plt.show()
        ```
    - **Correlation Matrix**:
        ```python
        corr_matrix = df.corr()
        sns.heatmap(corr_matrix, annot=True)
        plt.show()
        ```
    - **Pair Plot**:
        ```python
        sns.pairplot(df)
        plt.show()
        ```

5. **Handling Missing Values**:
    ```python
    df = df.dropna()  # Dropping missing values
    ```

6. **Feature Engineering**:
    - Creating new features if necessary:
        ```python
        df['new_feature'] = df['existing_feature'] / df['another_feature']
        ```

## Running the Script

To run the EDA script, use the following command:
```sh
python eda.py
```

## Example Outputs

Here are some example outputs from running the EDA script on different datasets:

### 1. Netflix Movies
- **Summary Statistics**:
    ```python
    df.describe()
    ```

- **Correlation Matrix**:
    ![Correlation Matrix](images/netflix_corr.png)

### 2. Housing
- **Histogram of House Prices**:
    ![Histogram](images/housing_hist.png)

### 3. Boston Housing
- **Pair Plot**:
    ![Pair Plot](images/boston_pairplot.png)

### 4. World Happiness Report
- **Correlation Matrix**:
    ![Correlation Matrix](images/happiness_corr.png)

### 5. Mall Customers
- **Customer Segmentation Plot**:
    ![Segmentation Plot](images/mall_customers_segment.png)

### 6. Insurance
- **Charges vs. Age Scatter Plot**:
    ![Scatter Plot](images/insurance_scatter.png)

## Conclusion

This EDA project provides a comprehensive analysis of various datasets, helping in understanding the data better and preparing it for further modeling and analysis. The visualizations and statistical summaries generated during EDA are crucial for making informed decisions in any data-driven project.

---
