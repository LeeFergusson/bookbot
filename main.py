""" main.py - Main entry point for the bookbot project """
import sys

def main():
    """Main entry point for the bookbot project"""
    file_name = sys.argv[1]
    contents = read_file(file_name)
    print(contents)
    word_count = count_words(contents)
    characters = count_unique_characters(contents)
    print_report(file_name, word_count, characters)

def read_file(file_path):
    """Reads a file and returns the contents as a string"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def count_words(string):
    """Counts the number of words in a sting and returns the count"""
    return len(string.split())

def count_unique_characters(string):
    """ Counts the number of unique characters in a string and returns a
    dictionary with the counts
    """
    result = {}

    for character in string:
        lower_character = character.lower()
        if lower_character.isalpha():
            if lower_character in result:
                result[lower_character] += 1
            else:
                result[lower_character] = 1
    return result

def sort_characters(characters):
    """ Returns the value of the first element in a dictionary"""
    return characters[1]

def print_report(file_name, word_count, unique_characters):
    """Prints a report of the word count and unique characters"""
    print(f"--- Report for {file_name} ---")
    print("Word Count: ", word_count)
    char_list = list(unique_characters.items())
    char_list.sort(reverse=True, key=sort_characters)

    for char in char_list:
        print(f"The '{char[0]}' character appears {char[1]} times.")

    print("--- End of Report ---")

main()
