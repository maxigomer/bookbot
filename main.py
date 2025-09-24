from stats import (
    count_words,
    count_character,
    sort_dictionary
)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    content = get_book_text("/home/chrono/bootdev/bookbot/books/frankenstein.txt")
    count = count_words(content)

    print(f"Found {count} total words")
    # print(sort_dictionary(count_character(content)))
    sorted_dict = sort_dictionary(count_character(content)) 

    for d in sorted_dict:
        print(f"{d["char"]}: {d["num"]}")


main()