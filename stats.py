def get_word_count(text):
    return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(dict):
    return dict["num"]

def sort_counted_chars(counted_dict):
    return sorted(counted_dict.items(), key=lambda x: x[1], reverse=True) 