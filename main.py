from stats import get_word_count, get_char_count, sorted_dictionaries
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents        

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    word_count = get_word_count(book)
    characters_dict = get_char_count(book)
    sorted_character_count = sorted_dictionaries(characters_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_count_dictionary in sorted_character_count:
        character = character_count_dictionary["char"]
        count = character_count_dictionary["num"]
        if(character.isalpha()):
            print(f"{character}: {count}")
    print("============= END ===============")
    
main()