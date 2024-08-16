def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    print(text)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(characters_count):
    sorted_list = []
    for ch in character_count:
        sorted_list.append({"char": ch, "num": character_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def character_count(text):
    characters = {}
    for character in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def get_book(path):   
    with open(path) as f:
        return f.read()

def get_words(text):
    words = file_contents.split()
    return len(words)


main()