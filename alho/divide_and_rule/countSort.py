#https://stepik.org/lesson/13252/step/3?unit=3437

n = int(input())
data = list(map(int, input().split()))
sorted_data = [0 for _ in range(0, len(data))]
b = [0 for _ in range(0, 11)]
for item in data:
    b[item] += 1

for i in range(1, 11):
    b[i] += b[i - 1]

for i in range(1, len(data) + 1):
    item = data[-i]
    sorted_data[b[item] - 1] = str(item)
    b[item] -= 1

print(' '.join(sorted_data))