def get_word_count(book):
    return len(book.split())

def get_char_count(book):
    characters_dict = {}
    for char in book.lower():
        if char in characters_dict:
            characters_dict[char] += 1
        else:
            characters_dict[char] = 1
    return characters_dict

def sort_on(character_count_dictionary):
    return character_count_dictionary["num"]

def sorted_dictionaries(characters_dict):
    dictionary_list = []
    for key in characters_dict:
        dictionary_list.append({"char": key, "num": characters_dict[key]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
        