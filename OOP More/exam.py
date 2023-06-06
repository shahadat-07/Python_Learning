def count_occurrences(N, list):
    occurrences = {}
    for element in list:
        if element not in occurrences:
            occurrences[element] = 1
        else:
            occurrences[element] += 1

    for i in range(1, M + 1):
        print(occurrences.get(i, 0))

N, M = [int(x) for x in input().split()]
list = [int(x) for x in input().split()]

count_occurrences(N, list)













# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# # Create a dictionary to store the counts
# counts = {}

# # Count the occurrences of each number in A
# for num in A:
#     counts[num] = counts.get(num, 0) + 1

# # Print the count of each number from 1 to M
# for i in range(1, M+1):
#     print(counts.get(i, 0))
