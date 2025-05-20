import sys
import re

def col_to_num(col_str):
    """
    Convert Excel-style column (e.g., 'BC') to its numerical index (e.g., 55).
    """
    num = 0
    for c in col_str:
        num = num * 26 + (ord(c) - ord('A') + 1)
    return num


def num_to_col(num):
    """
    Convert numerical column index (e.g., 55) to Excel-style column (e.g., 'BC').
    """
    letters = []
    while num > 0:
        num -= 1
        letters.append(chr(ord('A') + (num % 26)))
        num //= 26
    return ''.join(reversed(letters))


def main():
    input = sys.stdin.readline
    n = int(input())
    # Pattern to detect RxCy format, e.g., 'R23C55'
    rxcy = re.compile(r'^R(\d+)C(\d+)$')

    for _ in range(n):
        s = input().strip()
        m = rxcy.match(s)
        # If matches RxCy, convert to Excel-style
        if m:
            row, col_num = m.group(1), int(m.group(2))
            col_str = num_to_col(col_num)
            sys.stdout.write(f"{col_str}{row}\n")
        else:
            # Otherwise it's Excel-style like 'BC23'
            # Split into letters and digits
            i = 0
            while i < len(s) and s[i].isalpha():
                i += 1
            col_str = s[:i]
            row_num = s[i:]
            col_num = col_to_num(col_str)
            sys.stdout.write(f"R{row_num}C{col_num}\n")

if __name__ == '__main__':
    main()