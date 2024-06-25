# Define the path to the test dataset
test_data_path = '/Users/zhangyutong/Desktop/UNPC.zh-es.txt/dataset/UNPC.large.train.zh-es'

# Function to count the number of tokens in the file
def count_tokens(file_path):
    total_zh_tokens = 0
    total_es_tokens = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if '\t' in line:
                zh_sentence, es_sentence = line.strip().split('\t')
                # Splitting the sentences into tokens by whitespace
                zh_tokens = zh_sentence.split()
                es_tokens = es_sentence.split()
                total_zh_tokens += len(zh_tokens)
                total_es_tokens += len(es_tokens)
    return total_zh_tokens, total_es_tokens

# Count the number of tokens in the test dataset
num_zh_tokens, num_es_tokens = count_tokens(test_data_path)
print(f"Number of Chinese tokens in the test dataset: {num_zh_tokens}")
print(f"Number of Spanish tokens in the test dataset: {num_es_tokens}")
