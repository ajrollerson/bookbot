
def count_words(text):
    words = text.split()
    return len(words)  

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    total_word_count = count_words(file_contents)
 
    print(f'Total number of words: {total_word_count}')

if __name__ == "__main__":
    main()