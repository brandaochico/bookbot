from stats import get_word_count, get_char_counts, get_char_dicts, sort_char_dicts

def get_book_text(path: str):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    book = get_book_text(path)
    num_words = get_word_count(book)
    print(f'Found {num_words} total words')

    print("--------- Character Count -------")
    char_counts = get_char_counts(book)
    char_dicts = get_char_dicts(char_counts)
    sorted = sort_char_dicts(char_dicts)
    
    for d in sorted:
        if not d["char"].isalpha():
            continue

        print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")

main()
