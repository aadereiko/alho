def fib_mod(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev, prev_prev = 1, 0
    # print('i', 'c', '%3', '%4', '%5')

    for i in range(2, n + 1):
        current = prev_prev + prev
        # print(i, current, current % 3, current % 4, current % 5)
        print(i, current, current % 5, 5)

        prev_prev, prev = prev, current

    return current

def main():
    n = int(input())
    print(fib_mod(n))


if __name__ == "__main__":
    main()