def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        number_of_words = len(file_contents.split())
        print(f"Wordcount: {number_of_words}")
main()
count_words()