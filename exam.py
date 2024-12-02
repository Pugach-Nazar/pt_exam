
def ar_prog_sum(a, b, n):
    if n < 1:
        raise ValueError("Кількість членів прогресії має бути більшою або рівною 1.")
    
    res = 0
    for i in range(n):
        res += a + i * b
    return res


def main():
    a = input("Введіть n щоб вийти, будь яку клафішу щоб продовжити: ")
    while(a != "n"):
        try:
            a = float(input("Введіть перший елемент прогресії: "))
            b = float(input("Введіть різницю прогресії: "))
            n = int(input("Введіть кількість членів прогресії: "))
        
            result = ar_prog_sum(a, b, n)
            print(f"Сума перших {n} членів прогресії: {result}")
        except ValueError as e:
            print(f"Помилка: {e}")
        
        a = input("Введіть n щоб вийти, будь яку клафішу щоб продовжити: ")


if __name__ == "__main__":
    main()

