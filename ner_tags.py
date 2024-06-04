import csv
import json
import re

def load_product_names(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        product_names = [line.strip() for line in file if line.strip()]
    return product_names

def load_csv_data(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader]
    return rows

def tokenize(text):
    # Simple tokenization by splitting on whitespace and punctuation
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    return tokens

def tag_tokens(tokens, product_names):
    ner_tags = [0] * len(tokens)
    for product in product_names:
        product_tokens = tokenize(product)
        for i in range(len(tokens) - len(product_tokens) + 1):
            if tokens[i:i + len(product_tokens)] == product_tokens:
                ner_tags[i] = 1  # B-product
                for j in range(1, len(product_tokens)):
                    ner_tags[i + j] = 2  # I-product
    return ner_tags

def chunk_tokens(tokens, max_length):
    chunks = []
    for i in range(0, len(tokens), max_length):
        chunks.append(tokens[i:i+max_length])
    return chunks

def generate_json(csv_data, product_names, output_file_path, max_chunk_length):
    json_data = []
    for idx, row in enumerate(csv_data):
        combined_text = ' '.join(row.values())  # Combine all columns into a single text
        tokens = tokenize(combined_text)
        token_chunks = chunk_tokens(tokens, max_chunk_length)
        for chunk_idx, chunk in enumerate(token_chunks):
            ner_tags = tag_tokens(chunk, product_names)
            json_data.append({
                'id': f"{idx}_{chunk_idx}",  # Unique ID for each chunk within a row
                'tokens': chunk,
                'ner_tags': ner_tags
            })
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4)

# File paths
csv_file_path = 'extracted_product_data.csv'
txt_file_path = 'product_names.txt'
output_file_path = 'ner_dataset.json'
max_chunk_length = 50  # Define the maximum length for each token chunk

# Load data
product_names = load_product_names(txt_file_path)
csv_data = load_csv_data(csv_file_path)

# Generate JSON
generate_json(csv_data, product_names, output_file_path, max_chunk_length)

print(f'JSON file has been created at {output_file_path}')

