import pandas as pd
import os


# ---------------------------------------------------------
# MOOC DATA PREPARATION
# Source:
# Kaggle - EdX, Coursera, and Udemy Course Data
# https://www.kaggle.com/datasets/kararhaitham/courses
# ---------------------------------------------------------

INPUT_FILE = "data/mooc/courses.csv"
OUTPUT_FILE = "data/mooc/mooc_processed.csv"


def load_data(file_path):
    """Load the raw MOOC dataset."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path)

    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumns:")
    print(df.columns.tolist())

    return df


def clean_column_names(df):
    """Standardize column names."""
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    return df


def remove_duplicates(df):
    """Remove duplicate course records."""
    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(f"Duplicates removed: {before - after}")

    return df


def remove_empty_rows(df):
    """Remove rows that contain no information."""
    df = df.dropna(how="all")

    return df


def main():

    # Load raw dataset
    df = load_data(INPUT_FILE)

    # Standardize column names
    df = clean_column_names(df)

    # Remove duplicate records
    df = remove_duplicates(df)

    # Remove completely empty rows
    df = remove_empty_rows(df)

    # Create output directory if required
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Save processed dataset
    df.to_csv(OUTPUT_FILE, index=False)

    print("\nMOOC data preparation completed.")
    print(f"Processed dataset saved to: {OUTPUT_FILE}")
    print(f"Final dataset size: {df.shape}")


if __name__ == "__main__":
    main()
