def find_closeness(l1, l2):
    min_len_list = min(len(l1), len(l2))
    result = []
    for index in range(min_len_list):
        if l1[index] != l2[index]:
            break
        result.append(l1[index])

    return len(result)


def loop_list_combinations():
    """
    Determining the number of combinations A=n!/k!*(n - k)!
    and return sum of all closeness count
    """
    count_of_lists = int(input()) * 2
    lists = []
    for i in range(1, count_of_lists + 1):
        stdin = input()
        if i % 2 == 0:
            lists.append(list(map(int, stdin.split())))

    result_sum = 0

    left = 0
    right = left + 1
    while left < len(lists):
        if right > len(lists) - 1:
            left += 1
            right = left + 1
            continue

        result_sum += find_closeness(lists[left], lists[right])
        right += 1

    print(result_sum)


def main():
    loop_list_combinations()


if __name__ == '__main__':
    main()
