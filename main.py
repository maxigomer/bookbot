from stats import (
    count_words,
    count_character,
    sort_dictionary
)
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():

    try:
        content = get_book_text(sys.argv[1])
        count = count_words(content)
        print(f"Found {count} total words")
        sorted_dict = sort_dictionary(count_character(content)) 

        for d in sorted_dict:
            print(f"{d["char"]}: {d["num"]}")

    except Exception:
        print("Usage: pyhton3 main.py <path_to_book>")
        sys.exit(1)


main()