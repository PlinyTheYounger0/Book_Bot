# Counts the words in a given file
def word_counter(book_text):
    words = book_text.split()
    return len(words)

# Counts the number of letters in a given file
def character_counter(words):
    char_count = {}
    for char in words:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Converts the char_count{} into a list with each character as 1 entry
def chars_dict_to_sorted_list(char_count):
    chars_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_info = {"char": char, "count": count}
            chars_list.append(char_info)
    chars_list.sort(reverse=True, key=lambda dict: dict["count"])
    return chars_list
