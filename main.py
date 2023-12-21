def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_counts = character_count(text)
    print(f"--- Begin Report of {book_path} ---")
    print("The book has " + str(num_words) + " words.")
    generate_count_report(character_counts)
    print(f"--- End Report ---")

def get_book_text(book_path):
    with open(book_path) as file:
        text = file.read()
    return text

def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    character_counts = {}
    for character in text.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def generate_count_report(character_counts):
    characters = list(character_counts.keys())
    characters.sort()
    for character in characters:
        if character.isalpha():
            print(f"The {character} character was found {character_counts[character]} times")
        else:
            pass

main()