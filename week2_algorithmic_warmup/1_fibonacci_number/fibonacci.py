# Uses python3
def calc_fib(n):
    if (n <= 1):
        return 1

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
