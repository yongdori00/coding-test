from itertools import combinations_with_replacement

num, n = map(int, input().split())
list_num = map(str, range(1, num + 1))
print('\n'.join(list(map(' '.join, combinations_with_replacement(list_num, n)))))