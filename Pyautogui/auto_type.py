def draw_pyramid(rows):
    for i in range(1, rows + 1):
        print("#" * i)


rows = int(input())

draw_pyramid(rows)
