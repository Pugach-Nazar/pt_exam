
def ar_prog_sum(a, b, n):
    if n < 1:
        raise ValueError("Кількість членів прогресії має бути більшою або рівною 1.")
    
    res = 0
    for i in range(n):
        res += a + i * b
    return res

print(ar_prog_sum(2, 3, 4))

