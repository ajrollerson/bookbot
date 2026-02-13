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