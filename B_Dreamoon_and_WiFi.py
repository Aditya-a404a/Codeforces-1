import sys
import math

def main():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()

    n = len(s1)

    # Compute the target position from s1
    answer_position = sum(1 if c == '+' else -1 for c in s1)

    # Compute the current position from s2 and count '?' moves
    final_position = 0
    moves = 0
    for c in s2:
        if c == '?':
            moves += 1
        else:
            final_position += (1 if c == '+' else -1)

    distance = answer_position - final_position

    # If it's impossible to reach, probability = 0
    if (moves + abs(distance)) % 2 != 0 or moves < abs(distance):
        prob = 0.0
    else:
        # Number of '+' moves among the '?' needed to reach the distance
        m = (moves + abs(distance)) // 2
        # Binomial coefficient: choose m out of moves
        ways = math.comb(moves, m)
        # Total possibilities = 2^moves
        prob = ways / (1 << moves)

    # Print with 12 decimal places
    print(f"{prob:.12f}")

if __name__ == "__main__":
    main()
