import os
from collections import Counter

os.system('clear')

"""
1. adding
2. Find added card from another player cards
3. calculating

1. Remove card from player cards
2. Calculating
"""


def main():
    first_stdin = tuple(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    steps = [input() for x in range(first_stdin[2])]
    result = []

    for step in steps:
        step = step.split(' ')
        operand = 'add' if int(step[0]) == 1 else 'remove'
        player = step[1]
        value = int(step[2])

        if operand == 'add':
            if player == 'A':
                A.append(value)
            if player == 'B':
                B.append(value)

        if operand == 'remove':
            if player == 'A':
                A.remove(value)
            if player == 'B':
                B.remove(value)

        count_elements = calculate(A, B)
        result.append(str(count_elements))

    print(' '.join(result))


def calculate(a, b):
    list_a = Counter(a)
    list_b = Counter(b)
    C = list_a - list_b
    D = list_b - list_a
    return len(list(C.elements())) + len(list(D.elements()))


if __name__ == '__main__':
    main()
