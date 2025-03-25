import sys
# Main Function
def main():
    file_path = file_path_check()
    book_text = get_book_text(file_path)
    word_count = word_counter(book_text)
    char_count = character_counter(book_text)
    sorted_char_count = chars_dict_to_sorted_list(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for char_dict in sorted_char_count:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

#Raises an exception if there is an invalid input
def file_path_check():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]
# Converts file content into a string
def get_book_text(file_path):
    with open(file_path) as book:
        return book.read()

from stats import word_counter
from stats import character_counter
from stats import chars_dict_to_sorted_list

try:
    main()
except Exception as e:
    print(e)