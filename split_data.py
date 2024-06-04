import json
import random

def split_data(json_file, train_ratio=0.8):
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Shuffle the data
    random.shuffle(data)

    # Calculate the number of samples for training and validation
    num_samples = len(data)
    num_train_samples = int(num_samples * train_ratio)

    # Split the data
    train_data = data[:num_train_samples]
    val_data = data[num_train_samples:]

    return train_data, val_data

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Replace 'your_data.json' with the path to your JSON file
json_file = 'ner_dataset.json'

# Split the data
train_data, val_data = split_data(json_file)

# Save the training and validation data to separate files
save_data(train_data, 'train_data.json')
save_data(val_data, 'val_data.json')

print("Data split and saved successfully!")

