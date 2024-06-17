def count_chars(word):
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


string = 'Happiness'
print(count_chars(string))

string = 'smiles'
print(count_chars(string))
