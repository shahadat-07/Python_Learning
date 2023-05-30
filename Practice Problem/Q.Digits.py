def print_digits_reverse(numbers):
    result = []
    for n in numbers:
        digits = []

        while n > 0:
            digit = n % 10
            digits.append(str(digit))
            n //= 10
        result.append(" ".join(digits))


testCase = int(input())

numbers = []
for i in range(testCase):
    numbers.append(int(input()))

output = print_digits_reverse(numbers)

for item in output:
    print(item)
