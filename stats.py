def get_word_count(book: str):
    words = book.split()
    return len(words)


def get_char_counts(book: str):
    chars: dict[str, int] = {}

    for char in book:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars


def get_char_dicts(char_counts: dict[str, int]):
    char_dicts = []

    for char, count in char_counts.items():
        entry = {"char": char, "num": count}
        char_dicts.append(entry)

    return char_dicts 


def sort_char_dicts(char_dicts: list[dict[str, int]]):
    char_dicts.sort(reverse=True, key=sort_by)

    return char_dicts 


def sort_by(items):
    return items["num"]
