import sys
from stats import get_word_count, get_chars_dict, sort_counted_chars

def main():
    check_args()
    book_path = sys.argv[1]
    # book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    num_chars = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(num_chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    sorted_vals = sort_counted_chars(num_chars)
    for val in sorted_vals:
    	if val[0].isalpha():
		    print(f"{val[0]}: {val[1]}")
                
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def check_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

main()
