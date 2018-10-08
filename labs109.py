
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


if __name__ == "__main__":
    pass