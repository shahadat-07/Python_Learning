n = int(input())

my_list = []

user_input = input()

try:
    values = user_input.split()

    my_list = [int(value) for value in values]
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")

countOperation = 0
even = True

while even:
    copy_list = my_list.copy()

    for num in copy_list:
        if num % 2 == 0:
            continue
        else:
            even = False
            break

    if even == True:
        countOperation += 1

    for i in range(len(my_list)):
        my_list[i] = my_list[i] // 2

print(countOperation)
