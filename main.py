def get_book_text(path: String):
    with open(path) as f:
        return f.read()

def get_word_count(book: String):
    words = book.split()
    return len(words)

def main():
    book = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(book)

    print(f'Found {num_words} total words')

main()
