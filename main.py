
def ar_prog_sum(a, b, n):
    if n < 1:
        raise ValueError("n less then 1")
    res = 0
    for i in range(n):
        res += a + i * b
    return res

print(ar_prog_sum(0, 1, 5))

