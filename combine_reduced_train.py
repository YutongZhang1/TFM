def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def save_moses_format(dataset, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for example in dataset:
            f.write(f"{example['chinese']}\t{example['spanish']}\n")

# Define the file paths for the training set
file_path_train_zh = '/Users/zhangyutong/Desktop/UNPC.zh-es.txt/UNPC.zh'
file_path_train_es = '/Users/zhangyutong/Desktop/UNPC.zh-es.txt/UNPC.es'
output_path_train = '/Users/zhangyutong/Desktop/UNPC.large.train.zh-es'

# Read the Chinese and Spanish files
chinese_sentences = read_file(file_path_train_zh)
spanish_sentences = read_file(file_path_train_es)

# Ensure both files have the same number of sentences
assert len(chinese_sentences) == len(spanish_sentences), "The number of sentences in both files should be the same."

# Combine the sentences into a single dataset
combined_dataset = [{'chinese': zh.strip(), 'spanish': es.strip()} for zh, es in zip(chinese_sentences, spanish_sentences)]

# Print the final length of the combined dataset
print(f"Final length of the combined dataset: {len(combined_dataset)}")

train_length = 20000 

# Calculate the lengths of the training, validation, and test sets
reduced_combined_dataset_length = int(train_length)

# Ensure the length doesn't exceed the original dataset length
reduced_combined_dataset_length = min(reduced_combined_dataset_length, len(combined_dataset))

# Get the reduced combined dataset
reduced_combined_dataset = combined_dataset[:reduced_combined_dataset_length]

# Print the final length of the reduced combined dataset
print(f"Final length of the reduced combined dataset: {len(reduced_combined_dataset)}")

# Save the reduced combined dataset in Moses format
save_moses_format(reduced_combined_dataset, output_path_train)
print(f"Reduced training set saved to {output_path_train}")
