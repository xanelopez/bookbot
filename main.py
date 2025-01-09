def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_count_dict = get_char_count(text)
    print(f"--- Report for {path} ---\n")
    print(f"{word_count} words in the document.\n")
    print(f"This is the count of letters:\n ")
    # sort_dat_list(char_count_dict_to_list(char_count_dict))
    print_sorted_list(char_count_dict_to_list(char_count_dict))
    print("--- End report ---")


# pass string, returns length of list made from string split on spaces
def get_word_count(text):
    words = text.split()
    return len(words)

# pass path to book, return content as string
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

# pass string, return a dictionary of character : count (key:value) pairs
def get_char_count(text):
    lowercase_string = text.lower()
    my_dict = {}
    for char in lowercase_string: 
        if char.isalpha(): # if character is alphabetical
            if char in my_dict: # if character already exists in dict
                my_dict[char] += 1 # add one to that key:value
            else:
                my_dict[char] = 1 # character is alpha but not in list, initialize at 1
    print(my_dict)
    return my_dict

# Convert dictionary of chars into a list of dictionaries
# {a = 333, ...} => [{"letter": "a", "num": 333}, ...]

def char_count_dict_to_list(dict):
    list_of_dict = []
    for k in dict:
        list_of_dict.append({"letter": k, "num": dict[k]})
    return list_of_dict

# Take dictionary and return the value of "num"
def sort_on(dict):
    return dict["num"]

# Print each line of sorted list for report
def print_sorted_list(list_of_dict):
    list_of_dict.sort(reverse=True, key=sort_on)
    for dict in list_of_dict:
        print(f"The {dict["letter"]} character was found {dict["num"]} times")


main()

