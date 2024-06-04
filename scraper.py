import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

# File paths
input_csv_path = 'valid_urls.csv'
output_csv_path = 'extracted_product_data.csv'

# Read URLs from CSV
urls_df = pd.read_csv(input_csv_path)

# Function to extract data from a given URL
def extract_product_data(url):
    product_data = {
        'url': url,
        'main_product_title': '',
        'main_product_description': '',
        'other_product_names': []
    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract main product title
            title_element = soup.select_one('h1, h2, .product-title, .product-name')
            if title_element:
                product_data['main_product_title'] = title_element.get_text(strip=True)
            
            # Extract main product description
            description_element = soup.select_one('div.description, div.product-description, p.product-description, span.product-description')
            if description_element:
                product_data['main_product_description'] = description_element.get_text(strip=True)
            
            # Extract other product names (suggestions/related products)
            other_products_elements = soup.select('a.related-product-title, a.product-suggestion, a.product-link, .related-products a, .suggested-products a')
            product_data['other_product_names'] = [item.get_text(strip=True) for item in other_products_elements]
            
            # Fallback to extracting any product names from list items if specific selectors don't work
            if not product_data['other_product_names']:
                list_items = soup.select('li.product-item, li.related-product, li')
                product_data['other_product_names'] = [item.get_text(strip=True) for item in list_items if item.get_text(strip=True)]
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
    return product_data

# List to store the results
results = []

# Iterate over each URL and extract product data
for index, row in urls_df.iterrows():
    url = row['url']
    product_data = extract_product_data(url)
    results.append(product_data)

# Write the results to a new CSV file
with open(output_csv_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['url', 'main_product_title', 'main_product_description', 'other_product_names']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for result in results:
        # Join other product names into a single string separated by ';'
        result['other_product_names'] = '; '.join(result['other_product_names'])
        writer.writerow(result)

print(f"Scraping completed. Extracted product data saved to {output_csv_path}")

