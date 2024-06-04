import pandas as pd
import csv

# File paths
input_csv_path = 'extracted_clean_product_data.csv'
output_csv_path = 'organized_product_data.csv'

# Read the existing CSV file
data_df = pd.read_csv(input_csv_path)

# List to store the reorganized results
results = []

# Iterate through each row and reorganize the data
for index, row in data_df.iterrows():
    url = row['url']
    
    # Add main product title
    if row['main_product_title']:
        results.append({'url': url, 'type': 'main_product_title', 'text': row['main_product_title']})
    
    # Add main product description
    if row['main_product_description']:
        results.append({'url': url, 'type': 'main_product_description', 'text': row['main_product_description']})
    
    # Add other product names
    if row['other_product_names']:
        other_product_names = row['other_product_names'].split('; ')
        for other_product in other_product_names:
            results.append({'url': url, 'type': 'other_product_name', 'text': other_product})

# Write the reorganized results to a new CSV file
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['url', 'type', 'text']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print(f"Reorganization completed. Organized product data saved to {output_csv_path}")

