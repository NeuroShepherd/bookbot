from stats import character_counter

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
   
 
frank_text = get_book_text("books/frankenstein.txt")

counted_chars = character_counter(frank_text)

print(counted_chars)

sorties = sorted(counted_chars.items(), key=lambda item: item[1], reverse=True)

print(sorties)