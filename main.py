def main():

    book_path = 'books/frankenstein.txt'
    
    book_text = get_book_txt(book_path)

    no_of_words = get_num_words(book_text)

    no_of_char = get_char_num_dict(book_text)

    
    chars = [{"name" : key , "num" : value} for key , value in no_of_char.items()]

    chars.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")

    print (f"{no_of_words} words found in this document\n")

    for data in chars:
        
        if not data['name'].isalpha():
            continue
        print( f"The {data['name']} character was found {data['num']} times")
    
    print("--- End report ---")

def sort_on(dict):

    return dict['num']


def get_num_words(text):
    
    return len(text.split())


def get_book_txt(path):

    with open(path) as f:

        return f.read()


# def get_char_num(text):

#     abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     text_string = text.lower()

#     char_ocur_dict = {}

#     for char in abc:

#         count = text_string.count(char)
        
#         char_ocur_dict[char] = count

#     return char_ocur_dict

def get_char_num_dict(text):
    
    text_str = text.lower()

    char_dict = {}

    for c in text_str:

        if c in char_dict:

            char_dict[c] += 1

        else:
            
            char_dict[c] = 1

    return char_dict


main()