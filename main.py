def main():
    path_to_file = "books/frankenstein.txt"
    text = book_text(path_to_file)
    number_of_words = count_words(text)
    print(text)
    print(f"Wordcount: {number_of_words}")

def count_words(text):
    return len(text.split())
        

def book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()