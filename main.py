from collections import Counter
import string

def output_char_count(char_counter):
    for char, count in char_counter.items():
        if char not in list(string.ascii_lowercase):
            continue
        print(f"The '{char}' character was found {count} times")

def count_words(text: str):
    return len(text.split())

def count_characters(text: str):
    counter = Counter(text.lower())
    return dict(sorted(counter.items(), key=lambda item: item[1], reverse=True)) 

def main():
    path_to_file = "./books/frankenstein.txt"
    
    print("--- Begin report of books/frankenstein.txt ---")
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document")
        char_count = count_characters(file_contents)
        output_char_count(char_count)
    print("--- End report ---")


main()
