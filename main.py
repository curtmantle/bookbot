def main():
    path_to_file = "books/frankenstein.txt"

    file_contents = read_file(path_to_file)
    words = get_words(file_contents)
    word_count = count_words_in_string(words)
    word_dictionary = count_letters(file_contents)
    alpha_list = convert_to_alpha_list(word_dictionary)

    print(f"--- Begin report of {path_to_file} ---")
    print()
    print(f"{word_count} words found in document")
    print()
    for c in alpha_list:
        print(f"The '{c[1]}' character was found {c[0]} times")

    print("--- End Report ---")

def read_file(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_words(text):
    return text.split()

def count_words_in_string(words):
    return len(words)

def count_letters(text):
    word_dictionary = {}

    for c in text:

        lc = c.lower()

        if lc in word_dictionary:
            word_dictionary[lc] += 1
        else:
            word_dictionary[lc] = 1

    return word_dictionary

def convert_to_alpha_list(word_dictionary):

    alpha_list = []

    for c in word_dictionary:
        if c.isalpha():
            alpha_list.append((word_dictionary[c], c))

    alpha_list.sort(reverse=True)

    return alpha_list

main()



