import pandas as pd
import re

def clean_text(text):
    # Remove unwanted symbols and text patterns
    # This example removes all characters that are not letters, digits, or whitespace
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def clean_csv(input_file, output_file):
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Apply the cleaning function to all text columns
    text_columns = df.select_dtypes(include=['object']).columns
    for col in text_columns:
        df[col] = df[col].apply(lambda x: clean_text(str(x)))

    # Save the cleaned CSV file
    df.to_csv(output_file, index=False)
    print(f"Cleaned CSV saved to {output_file}")

if __name__ == "__main__":
    # Input and output file paths
    input_csv = 'extracted_product_data.csv'
    output_csv = 'extracted_product_data.csv'
    
    clean_csv(input_csv, output_csv)

