list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
index_of_max = 0
for i in range(len(list_numbers)):
    if list_numbers [i] > list_numbers[index_of_max]:
        index_of_max = i

swp = list_numbers[-1]
list_numbers[-1] = list_numbers[index_of_max]
list_numbers[index_of_max] = swp

print(list_numbers)
