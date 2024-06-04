import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = 'organized_product_data.csv'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Assuming the column name containing product names is 'product_name'
product_names = df['text'].tolist()

# If your CSV has no header
# df = pd.read_csv(csv_file_path, header=None)
# product_names = df[0].tolist()

# Specify the output text file path
output_text_file = 'product_names.txt'

# Write product names to the text file
with open(output_text_file, 'w', encoding='utf-8') as f:
    for product_name in product_names:
        if isinstance(product_name, str):
            f.write(product_name + '\n')
        elif isinstance(product_name, float):
            f.write(str(product_name) + '\n')  # Convert float to string
        # Add more conditions if necessary to handle other data types

print(f'Product names written to {output_text_file}')

