from stats import word_count
from stats import character_count
from stats import sorted_char_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def generate_report(text):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    book = get_book_text(sys.argv[1])
    total_words = word_count(book)
    print(f"Found {total_words} total words")
    print("----------- Character Count ----------")
    character_count_dict = character_count(book)
    sorted_chars = sorted_char_dict(character_count_dict)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    generate_report(text)
    sys.exit(0)

if __name__ == "__main__":
    main()