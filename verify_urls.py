import csv
import requests
from requests.exceptions import RequestException

def is_valid_url(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except RequestException:
        return False

def read_urls_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return [row[0] for row in reader]


def write_urls_to_csv(file_path, urls):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for url in urls:
            writer.writerow([url])


def main(input_csv, valid_output_csv, invalid_output_csv):
    urls = read_urls_from_csv(input_csv)
    valid_urls = []
    invalid_urls = []

    for url in urls:
        if is_valid_url(url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    write_urls_to_csv(valid_output_csv, valid_urls)
    write_urls_to_csv(invalid_output_csv, invalid_urls)

    print(f"Total valid URLs: {len(valid_urls)}")
    print(f"Total invalid URLs: {len(invalid_urls)}")

if __name__ == "__main__":
    input_csv = "furniture_stores_pages.csv" 
    valid_output_csv = "valid_urls.csv"
    invalid_output_csv = "invalid_urls.csv"

    main(input_csv, valid_output_csv, invalid_output_csv)

