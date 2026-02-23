import time

def word_count(text):
    text_words = text.split()
    return len(text_words)

def character_count(text):
    ltext = text.lower()
    character_dict = dict()
    for c in ltext:
        if c not in character_dict:
            character_dict[c] = 1
        else:
            character_dict[c] += 1
    return character_dict

    
def sorted_char_dict(character_count):
    char_list = []
    for character, count in character_count.items():
        if character.isalpha():
            char_list.append({"char": character, "num": count})

    def sort_on(dict):
        return dict["num"]
    
    return sorted(char_list, reverse=True, key=lambda d: d['num'])

def estimated_reading_time(text, wpm):
    minutes = word_count(text) / int(wpm)
    seconds = minutes * 60
    return time.strftime("%H:%M:%S", time.gmtime(seconds))




