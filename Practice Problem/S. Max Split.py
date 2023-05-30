def countBalancedString(S):
    count_L = 0
    count_R = 0
    balanced_strings = []

    for char in S:
        if char == 'L':
            count_L += 1
        else:
            count_R += 1

        if count_L == count_R:
            balanced_strings.append(S[:count_L + count_R])
            S = S[count_L + count_R:]
            count_L = 0
            count_R = 0

    print(len(balanced_strings))

    for string in balanced_strings:
        print(string)


S = input()

countBalancedString(S)
