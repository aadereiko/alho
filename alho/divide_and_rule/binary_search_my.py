def bin_search(data, element):
    if len(data):
        l, r = 0, len(data) - 1
        while l <= r:
            m = (l + r) // 2
            if data[m] == element:
                return m
            if data[m] > element:
                r = m - 1
            else:
                l = m + 1
    return -1


first_line = input().split(' ')

amount = int(first_line[0])
array = list(map(int, first_line[1:]))

second_line = input().split(' ')

amount_find = int(second_line[0])
array_find = list(map(int, second_line[1:]))

result = ''
for item in array_find:
    found = bin_search(array, int(item))
    result += f'{-1 if found < 0 else found + 1} '

print(result.rstrip())