def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number_of_words = count_words(text)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{number_of_words} words found in the document")
    chars = list_dict(count_characters(text))
    for dict in chars:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times")
    print("--- End report ---")

def count_words(text):
    return len(text.split())
        

def book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def count_characters(text):
    using = text.lower()
    alphabet = list(map(chr, range(97, 123)))
    dict = {}
    for c in alphabet:
        count = using.count(c)
        dict[c] = count
    return dict

def sortin(dict):
    return dict["num"]

def list_dict(dict):
    list_dict = []
    for key in dict:
        char = key
        num = dict[key]
        list_dict.append({"char": key, "num": num})
    list_dict.sort(reverse=True, key=sortin)
    return list_dict

main()