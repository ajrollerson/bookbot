from stats import word_count
from stats import character_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"Found {word_count(text)} total words")
    print(character_count(text))
if __name__ == "__main__":
    main()