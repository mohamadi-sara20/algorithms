from math import comb, factorial

def stirling_sec(m, n):
    total = 0
    for i in range(n):
        exp = (-1)**i * comb(n, n-i) * (n-i)**m
        total += exp
    return total // factorial(n)


if __name__ == "__main__":
    print(stirling_sec(3, 2))
    print(stirling_sec(7, 2))