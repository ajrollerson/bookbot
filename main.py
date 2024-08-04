
def count_words(text):
    words = text.split()
    return len(words)  

def count_characters(text):
    lowered_text = text.lower()
    text_charactercount = {}
    for character in lowered_text:
        if character not in text_charactercount:
            text_charactercount[character] = 1
        else:
            text_charactercount[character] += 1

    return(text_charactercount)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    total_word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    sum_char_count = sum(character_count.values())
 
    print(f'Total number of words: {total_word_count}')
    print(f'Total characters:{character_count}')
    print(f'Sum of characters: {sum_char_count}')

if __name__ == "__main__":
    main()