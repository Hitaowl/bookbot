def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    dict_list = dict_to_list(char_count)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"---Begin report of {book_path} ---")
    print (f" {num_words} words found in the document")
    for entry in dict_list:
        print(f"The '{entry["character"]}' character was found {entry["count"]} times")
    print("--- End report ---")



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    lowered_text = text.lower()
    char_count = {}
    for character in lowered_text:
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def dict_to_list(dict):
    dict_list = []
    for line in dict:
        if line.isalpha() == True:
            new_line = {"character":line, "count": dict[line]}
            dict_list.append(new_line)
    return dict_list


main()