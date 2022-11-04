# TODO решить с помощью list comprehension и распечатать его
import pprint

def solve(n):
    return [dict(bin=bin(x),dec=x, hex= hex(x), oct=oct(x)) for x in range(n + 1)]

num = 15
pprint.pprint(solve(num))
