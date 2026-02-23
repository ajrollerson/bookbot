from stats import word_count
from stats import character_count
from stats import sorted_char_dict
from stats import estimated_reading_time
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def generate_report(text, wpm):
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    book = get_book_text(sys.argv[1])
    total_words = word_count(book)
    print(f"Found {total_words} total words")
    print("----------- Reading Time ----------")
    est_reading_time = estimated_reading_time(text, wpm)
    print(f"Estimated reading time is {est_reading_time}")
    print("----------- Character Count ----------")
    character_count_dict = character_count(book)
    sorted_chars = sorted_char_dict(character_count_dict)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book> [estimated wpm if known]")
        sys.exit(1)

    try:
        if len(sys.argv) >= 3:
            wpm = int(sys.argv[2])
            if wpm < 0:
                print("Error: wpm must be above 0! Defaulting to 250")
                wpm = 250
        else:
            wpm = 250
    except (ValueError, IndexError):
        print("Invalid input! Defaulting to 250")
        wpm = 250


    text = get_book_text(sys.argv[1])

    generate_report(text, wpm)
    sys.exit(0)

if __name__ == "__main__":
    main()