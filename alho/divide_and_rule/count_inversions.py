def insert_index(data, element):
    l, r = 0, len(data) - 1
    while l <= r:
        if data[r] >= element:
            return r + 1
        if data[l] < element:
            return l
        m = (l + r) // 2
        if data[m] < element:
            r = m - 1
        elif data[m] > element:
            l = m + 1
        elif data[m] == element:
            return m + 1
    return -1


amount = int(input())
numbers = list(map(int, input().split()))

amount_inversion = 0

if len(numbers) > 1:
    sorted_copy = [numbers[-1]]
    # print(numbers)

    for index in range(2, amount + 1):
        index_to_put = insert_index(sorted_copy, numbers[-index])
        count_of_less = len(sorted_copy) - index_to_put
        amount_inversion += count_of_less
        # print(numbers[-index], count_of_less, 'kek')
        sorted_copy[index_to_put:index_to_put] = [numbers[-index]]
        # print(sorted_copy, 'sorted copy')
    print(amount_inversion)

else:
    print(0)

