final_number = int(input())
seq = []

if final_number == 1 or final_number == 2:
    print(1)
    print(final_number)
else:
    result = 0
    for i in range(1, final_number + 1):
        if result + i <= final_number:
            result += i
            seq.append(str(i))
        else:
            delta = final_number - result
            seq[len(seq) - 1] = str(int(seq[len(seq) - 1]) + delta)
            result = result + delta
        if result == final_number:
            break
    print(len(seq))
    print(' '.join(seq))
