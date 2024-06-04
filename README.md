# Veridion Challenge 2

#### Project: Furniture Stores Extraction

**Goal**: a new model that is able to extract products from Furniture Stores.

**Inputs**: a list of URLs from furniture store sites.

**Outputs**: a list of product names extracted from every URL.

#### Insights

**Veridion** - provides the most complete database of company data. Gathered by AI with human precision.

I downloaded a data sample in order to know what I am supposed to find on the websites. It was a bit of confusion as I didn't know if the product names would be "Hamar Plant Stand" or "Plant Stand". After inspecting the data sample I came to the conclusion that "Plant Stand" is the target.
![image](https://github.com/cetusian/NER-product-names/assets/73785144/634efa8c-c9e8-4008-9461-ae49199691b8)
*Veridion Data Sample: Data Dictionary - Product & Services*

![image](https://github.com/cetusian/NER-product-names/assets/73785144/83a4ac06-a4bd-4b3f-8c48-3562dd7241cc)
*Veridion Data Sample: Products & Services Sample*

Also, this challenge could provide useful solutions and insights for the company as some of the names are not captured well:
![image](https://github.com/cetusian/NER-product-names/assets/73785144/cf3b0399-74af-4033-809f-94203e5acc2b)
*Veridion Data Sample: Products & Services Sample - Wrong product name example*
![image](https://github.com/cetusian/NER-product-names/assets/73785144/e294a98e-32d7-46f6-87cb-8cce6dde10b8)

Please correct me if I am wrong.

The last thing that I found was Veridion's Entity Recognizers which is what I am going to build today for finding the entities named 'PRODUCTS'.
![image](https://github.com/cetusian/NER-product-names/assets/73785144/5c425609-f475-4016-8fed-13d86ad95694)

#### Guidelines

- create a NER (Named Entity Recognition) model;
- train the NER model to find the entities: 'PRODUCT';
- training data > ~100 pages from the URLs list;
- a way to tag some sample products;
- use the model to extract product names from unseen pages;
- showcase the solution.

#### Process

1. The urls had to be verified in order to start working with them, and also to have a clear view of what am I doing. So I created this script [verify_urls.py](https://github.com/cetusian/NER-product-names/blob/main/verify_urls.py) to get [valid_urls.csv](https://github.com/cetusian/NER-product-names/blob/main/valid_urls.csv) and [invalid_urls.csv](https://github.com/cetusian/NER-product-names/blob/main/invalid_urls.csv).
2. I used the valid_urls.csv as input for the [scraper.py](https://github.com/cetusian/NER-product-names/blob/main/scraper.py), and I scraped as much as I knew after I inspected some websites's structure. This is where I got the scraped data from the valid websites: [extracted_product_data.csv](https://github.com/cetusian/NER-product-names/blob/main/extracted_product_data.csv).
3. Cleaned the extracted_product_data.csv using [clean_data.py](https://github.com/cetusian/NER-product-names/blob/main/clean_data.py).
4. Hand annotation was awful even with tools, so I wanted to be creative and save myself some pain (there's a whole story about how I ended up here). I created [organize_data.py](https://github.com/cetusian/NER-product-names/blob/main/organize_data.py) to get [organized_product_data.csv](https://github.com/cetusian/NER-product-names/blob/main/organized_product_data.csv). The plan wasn't going as I wanted so I created [to_list.py](https://github.com/cetusian/NER-product-names/blob/main/to_list.py) to finally get [product_names.txt](https://github.com/cetusian/NER-product-names/blob/main/product_names.txt). The whole point of this was to automate getting the labels for the furniture names through a very unorthodox method.
5. It was time for text annotation using product_names.txt and extracted_product_data.csv; I made the script for text annotation and dataset structure [ner_tags.py](https://github.com/cetusian/NER-product-names/blob/main/ner_tags.py). My inspiration was the wnut17 dataset and I tried to copy its structure. (max_chunk_length = 50 helped in being able to fine-tune the model on colab. It was a trial and error until I found this also).
6. The output of the previous code [ner_dataset](ner_dataset.json) got split into two json files: [train_data.json](https://github.com/cetusian/NER-product-names/blob/main/train_data.json) and [val_data.json](https://github.com/cetusian/NER-product-names/blob/main/val_data.json) using this script [split_data.py](https://github.com/cetusian/NER-product-names/blob/main/split_data.py) - 80% training and 20% validation.
7. Fine-tuned distilbert-base-uncased on my data: [Fine_tune_distilbert_NER_Furniture.ipynb](https://github.com/cetusian/NER-product-names/blob/main/Fine_tune_distillbert_NER_Furniture.ipynb).
8. Used the fine-tuned model to get the list of product names extracted from the valid urls [testing_ner.ipynb](https://github.com/cetusian/NER-product-names/blob/main/testing_ner.ipynb).

 


---
* [ ] Correctness
* [ ] Going the extra mile
* [ ] Robustness: let the program do the talking
* [ ] Code quality
* [ ] Creativity
* [ ] Presentation

