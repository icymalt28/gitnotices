import pandas as pd
import requests

# Replace 'YOUR_GOOGLE_DATASET_URL' with the actual URL from Google Dataset Search
google_dataset_url = 'https://github.com/nytimes/covid-19-data'

# Download the dataset from the URL
try:
    response = requests.get(google_dataset_url)
    response.raise_for_status()  # Check for errors in the request
    data = response.json()  # Assuming the data is in JSON format
except requests.exceptions.RequestException as err:
    print(f"Error downloading the dataset: {err}")
    data = None

# Check if the data was successfully loaded
if data is not None:
    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    # Explore the dataset
    print("First few rows of the dataset:")
    print(df.head())

    print("\nInformation about the dataset:")
    print(df.info())

    print("\nSummary statistics of the dataset:")
    print(df.describe())

    # Perform specific analysis based on your dataset
    # For example, if your dataset has a column named 'age', you can calculate the average age:
    if 'age' in df.columns:
        average_age = df['age'].mean()
        print(f"\nAverage Age: {average_age}")

    # If your dataset has a column named 'category', you can count the occurrences of each category:
    if 'category' in df.columns:
        category_counts = df['category'].value_counts()
        print("\nCategory Counts:")
        print(category_counts)

    # Perform further analysis and visualization as needed
    # ...

    # Save the cleaned dataset or analysis results if necessary
    # df.to_csv('cleaned_dataset.csv', index=False)