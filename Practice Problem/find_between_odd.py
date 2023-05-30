def calculate_odd_sum(x, y):
    odd_sum = 0

    # Swap x and y if x is greater
    if x > y:
        x, y = y, x

    for num in range(x + 1, y):
        if num % 2 != 0:
            odd_sum += num

    return odd_sum


# Taking multiple test cases and inputs from the user
num_test_cases = int(input())

for _ in range(num_test_cases):
    inputs = input()
    x, y = map(int, inputs.split())

    result = calculate_odd_sum(x, y)
    print(result)
