# Veridion Challenge 2

## Project: Furniture Stores Extraction

### Goal
Develop a model capable of extracting product names from furniture store websites.

### Inputs
- A list of URLs from furniture store sites.

### Outputs
- A list of product names extracted from each URL.

## Insights

**Veridion** provides the most comprehensive database of company data, gathered by AI with human precision.

Upon downloading a data sample, I needed to clarify whether the product names to extract were specific ("Hamar Plant Stand") or generic ("Plant Stand"). Inspection of the data sample led to the conclusion that "Plant Stand" is the target.

![Veridion Data Sample: Data Dictionary - Product & Services](https://github.com/cetusian/NER-product-names/assets/73785144/634efa8c-c9e8-4008-9461-ae49199691b8)
*Veridion Data Sample: Data Dictionary - Product & Services*

![Veridion Data Sample: Products & Services Sample](https://github.com/cetusian/NER-product-names/assets/73785144/83a4ac06-a4bd-4b3f-8c48-3562dd7241cc)
*Veridion Data Sample: Products & Services Sample*

This challenge offers an opportunity to improve the extraction process, as some product names are currently not captured correctly.

![Wrong product name example](https://github.com/cetusian/NER-product-names/assets/73785144/cf3b0399-74af-4033-809f-94203e5acc2b)
*Veridion Data Sample: Products & Services Sample - Wrong product name example*

![Entity Recognizers](https://github.com/cetusian/NER-product-names/assets/73785144/5c425609-f475-4016-8fed-13d86ad95694)
*Veridion Entity Recognizers - the basis for building the model to identify 'PRODUCTS' entities.*

## Guidelines

1. Create a NER (Named Entity Recognition) model.
2. Train the NER model to find 'PRODUCT' entities.
3. Use ~100 pages from the URLs list for training data.
4. Develop a method to tag sample products.
5. Use the model to extract product names from unseen pages.
6. Showcase the solution.

## The Process

1. **URL Verification**:
   - Verified URLs to ensure they were functional using [verify_urls.py](https://github.com/cetusian/NER-product-names/blob/main/verify_urls.py), producing [valid_urls.csv](https://github.com/cetusian/NER-product-names/blob/main/valid_urls.csv) and [invalid_urls.csv](https://github.com/cetusian/NER-product-names/blob/main/invalid_urls.csv).

2. **Data Scraping**:
   - Used [scraper.py](https://github.com/cetusian/NER-product-names/blob/main/scraper.py) to scrape data from the valid URLs, resulting in [extracted_product_data.csv](https://github.com/cetusian/NER-product-names/blob/main/extracted_product_data.csv).

3. **Data Cleaning**:
   - Cleaned the scraped data with [clean_data.py](https://github.com/cetusian/NER-product-names/blob/main/clean_data.py).

4. **Data Organization**:
   - Automated the labeling process in an unorthodox manner to avoid manual annotation with [organize_data.py](https://github.com/cetusian/NER-product-names/blob/main/organize_data.py), producing [organized_product_data.csv](https://github.com/cetusian/NER-product-names/blob/main/organized_product_data.csv). There's a long story behind it.
   - Converted organized data to a list format using [to_list.py](https://github.com/cetusian/NER-product-names/blob/main/to_list.py), resulting in [product_names.txt](https://github.com/cetusian/NER-product-names/blob/main/product_names.txt).

5. **Text Annotation**:
   - Annotated text using product_names.txt and extracted_product_data.csv with [ner_tags.py](https://github.com/cetusian/NER-product-names/blob/main/ner_tags.py), inspired by the wnut17 dataset structure.

6. **Data Splitting**:
   - Split the annotated data into training and validation sets (80%/20%) using [split_data.py](https://github.com/cetusian/NER-product-names/blob/main/split_data.py), resulting in [train_data.json](https://github.com/cetusian/NER-product-names/blob/main/train_data.json) and [val_data.json](https://github.com/cetusian/NER-product-names/blob/main/val_data.json).

7. **Model Training**:
   - Fine-tuned `distilbert-base-uncased` on the dataset [Fine_tune_distilbert_NER_Furniture.ipynb](https://github.com/cetusian/NER-product-names/blob/main/Fine_tune_distillbert_NER_Furniture.ipynb).

8. **Model Testing and Solution Showcase**:
   - Used the fine-tuned model to extract product names from the valid URLs and created some graphs about the products [testing_ner.ipynb](https://github.com/cetusian/NER-product-names/blob/main/testing_ner.ipynb).

## The Model and the Dataset

The model and the dataset can be found on Hugging Face:
- [model](https://huggingface.co/cetusian/ner-model-furniture-v2)
- [dataset](https://huggingface.co/datasets/cetusian/ner-furniture-names)

![Screenshot 2024-06-04 05 02 22](https://github.com/cetusian/NER-product-names/assets/73785144/afa3c287-c19e-4a39-b535-a1a6b5824a54)

![Screenshot 2024-06-04 05 02 58](https://github.com/cetusian/NER-product-names/assets/73785144/4bde5a90-a9ee-4e63-ad86-732b92d493bc)

### Takeaways

- created my first dataset from scratch;
- fine-tuned my first LLM model;
- deployed both on HuggingFace;
- applied to my first machine learning internship;
- confidence in working constantly with bash, vim, hf, different types of data;
- understood how fine-tuning works for NER;
- understood how LLM are processing data;
