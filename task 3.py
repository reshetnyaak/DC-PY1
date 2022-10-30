a = ['a', 'b', 'c', 'd']


def delete(list_, index_):
    clipboard = []
    for i in range(len(list_)):
        if i is not index_:
            clipboard.append(list[i])
    return clipboard

print(delete(a, 1))
print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]


