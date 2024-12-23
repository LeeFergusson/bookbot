""" main.py - Main entry point for the bookbot project """

def main():
    """Main entry point for the bookbot project"""
    contents = read_file("books/frankenstein.txt")
    print(contents)

def read_file(file_path):
    """Reads a file and returns the contents as a string"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

main()
