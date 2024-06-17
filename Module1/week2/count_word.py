def count_word(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line_file in file:
            words = line_file.lower().strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


file_path = 'p1_data.txt'
print(count_word(file_path))
