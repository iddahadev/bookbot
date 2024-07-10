def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    words = get_words_count(book_content)
    characters_occurence = get_characters_occurence(book_content)
    sorted_letters_occurence = get_sorted_letters_occurence_list(characters_occurence)

    print_report(book_path, words, sorted_letters_occurence)

def print_report(book_path, words_count, letters_occurence):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_count} words found in the document")
    print()

    for letter_occurence in letters_occurence:
        print(f"The '{letter_occurence["letter"]}' character was found {letter_occurence["occurence"]} times")

    print("--- End report ---")

def get_book_content(file_path):
    with open(file_path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)

def get_characters_occurence(text):
    dict = {}
    lower_cased_text = text.lower()
    for character in lower_cased_text:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict


def sort_on(dict):
        return dict["occurence"]

def get_sorted_letters_occurence_list(characters_occurence):
    letters_list = []
    for char, occurence in characters_occurence.items():
        if char.isalpha():
            letter_dict = { "letter": char, "occurence": occurence }
            letters_list.append(letter_dict)
    
    letters_list.sort(reverse=True, key=sort_on)
    return letters_list

main()