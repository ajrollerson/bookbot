
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


def generate_report(character_count):
    char_list = []
    for character, count in character_count.items():
        if character.isalpha():
            char_list.append({"char": character, "num": count})
    
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 

    total_word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    sum_char_count = sum(character_count.values())
    char_list = generate_report(character_count)


    print("---Start of report ---")
    print(f'Total number of words: {total_word_count}')
    
    for entry in char_list:
        print(f"The '{entry['char']}' character was found {entry['num']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()