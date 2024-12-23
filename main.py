""" main.py - Main entry point for the bookbot project """

def main():
    """Main entry point for the bookbot project"""
    contents = read_file("books/frankenstein.txt")
    print(contents)
    print("Word Count: ", count_words(contents))

def read_file(file_path):
    """Reads a file and returns the contents as a string"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def count_words(string):
    """Counts the number of words in a sting and returns the count"""
    return len(string.split())

main()
