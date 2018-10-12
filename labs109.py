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
    items = list(items)  # tester is feeding tuples, not lists
    if items == sorted(items) and len(items) == len(set(items)):
        return True
    return False


def double_until_all_digits(n, giveup=1000):
    all_digits = '0123456789'
    found = False
    for i in range(giveup + 1):
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


def create_zigzag(rows, cols, start=1):
    result = []
    for r in range(rows):
        row = list(range(start + r * cols, start + (r + 1) * cols))
        if r % 2 == 1:
            row = row[::-1]
        result.append(row)
    return result


def contains_bingo(card, numbers, centerfree=False):
    checklist = []
    size = len(card)
    for i in range(size):
        checklist.append([card[i][j] for j in range(size)])             # Rows
        checklist.append([card[j][i] for j in range(size)])             # Cols
    checklist.append([card[i][i] for i in range(size)])                 # Diag 1
    checklist.append([card[len(card)-1-i][i] for i in range(size)])     # Diag 2
    for check in checklist:
        cross_check = [True if num in numbers or (num == card[2][2] and centerfree) else False for num in check]
        if all(cross_check):
            return True
    return False


def group_equal(items):
    result = []
    current = []
    while len(items) > 0:
        x = items.pop(0)
        if x in current:
            current.append(x)
        else:
            if current :
                result.append(current)
            current = [x]
    if current:
        result.append(current)
    return result


if __name__ == "__main__":
    # print(caps_lock_stuck('CHAPTER'))
    # print(scrabble_value("hello", [1, 1, 1, 1, 1]))
    # print(scrabble_value("world", [1, 3, 1, 1, 1]))
    # print(create_zigzag(3, 5))
    # print(create_zigzag(10, 1))
    # print(create_zigzag(4, 2))

    '''
    print(contains_bingo([
            [38, 93, 42, 47, 15], [90, 13, 41, 10, 56], [54, 23, 87, 70, 6], [86, 43, 48, 40, 92], [71, 24, 44, 1, 34]
                        ],
        [1, 2, 3, 4, 6, 8, 12, 13, 15, 16, 19, 21, 22, 24, 28, 34, 38, 40, 41, 42, 43, 45, 47, 49, 51, 53, 55, 57, 58,
         62, 65, 66, 69, 70, 72, 82, 83, 84, 86, 88, 95, 97], True))


    print(contains_bingo([
        [89, 23, 61, 94, 67],
        [19, 85, 90, 70, 32],
        [36, 98, 57, 82, 20],
        [76, 46, 25, 29, 7],
        [55, 14, 53, 37, 44]
    ],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 31, 33,
         35, 36, 37, 38, 39, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64,
         65, 68, 70, 71, 73, 75, 76, 77, 79, 81, 82, 84, 85, 86, 87, 88, 89, 90, 91, 94, 98]))
    '''
    print(group_equal([1, 1, 4, 4, 4, "hello", "hello", 4]))
    print(group_equal([1, 2, 3, 4]))
    print(group_equal([1]))
    print(group_equal([]))