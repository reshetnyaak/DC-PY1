def get_unique_list_numbers() -> list[int]:
    res = []
    k = 0
    while (k < 15):
        import random
        beg=-10
        end=10
        item = random.randint(-10, 10)
        if item not in res:
            res.append(item)
            k += 1
    return(res)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
