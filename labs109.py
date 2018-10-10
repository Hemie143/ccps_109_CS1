
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


if __name__ == "__main__":
    pass
