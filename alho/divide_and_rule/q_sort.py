# https://stepik.org/lesson/13249/step/6?unit=3434
from random import uniform
import bisect
# uniform(a, b) returns a <= x <= b


def quick_sort(data, left, right):
    m, i, j = int(uniform(left, right)), left, right
    while i <= j:
        while data[i] < data[m]:
            i += 1
        while data[j] > data[m]:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i += 1
            j -= 1
    if left < j:
        quick_sort(data, left, j)
    if i < right:
        quick_sort(data, i, right)

    return data

n_sectors, m_dots = list(map(int, input().split()))

a, b = [], []

for item in range(0, n_sectors):
    left, right = list(map(int, input().split()))
    a.append(left)
    b.append(right)

dots = list(map(int, input().split()))

sections_l = quick_sort(a, 0, len(a) - 1)
sections_r = quick_sort(b, 0, len(b) - 1)

result = []
for dot in dots:
    m = bisect.bisect_right(a, dot)
    n = bisect.bisect_left(b, dot)
    result.append(str(m - n))

print(' '.join(result))