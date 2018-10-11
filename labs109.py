import re
from functools import reduce

def ryerson_letter_grade(pct):
    if pct < 50: return 'F'
    if pct < 53: return 'D-'
    if pct < 57: return 'D'
    if pct < 60: return 'D+'

    if pct < 63: return 'C-'
    if pct < 67: return 'C'
    if pct < 70: return 'C+'

    if pct < 73: return 'B-'
    if pct < 77: return 'B'
    if pct < 80: return 'B+'

    if pct < 85: return 'A-'
    if pct < 90: return 'A'
    return 'A+'


def is_ascending(items):
    items = list(items)     # tester is feeding tuples, not lists
    if items == sorted(items) and len(items) == len(set(items)):
        return True
    return False


def double_until_all_digits(n, giveup = 1000):
    all_digits = '0123456789'
    found = False
    for i in range(giveup+1):
        if ''.join(sorted(set(str(n)))) == all_digits:
            found = True
            break
        n *= 2
    if found:
        return i
    return -1


def caps_lock_stuck(text):
    # FAILS
    split_text = re.split('a|A', text)
    for i, t in enumerate(split_text):
        if i % 2 == 1:
            split_text[i] = t.swapcase()
    return ''.join(split_text)


def scrabble_value(word, multipliers):
    _scrabble = {
        "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4,
        "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3,
        "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
        "y": 4, "z": 10
    }
    return sum([reduce(lambda c, m: c * m, x) for x in zip([_scrabble[c] for c in word], multipliers)])

if __name__ == "__main__":
    print(caps_lock_stuck('CHAPTER'))
    print(scrabble_value("hello", [1, 1, 1, 1, 1]))
    print(scrabble_value("world", [1, 3, 1, 1, 1]))
