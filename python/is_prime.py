def is_prime(n):
    """Проверка на натуральное число"""
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def get_smaller_primes(n):
    """Все натуральные до n"""
    smaller_primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            smaller_primes.append(num)
    return smaller_primes 

def eratosthenes(n):
    """Решето Эратосфена"""
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False
    return numbers


def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


print(get_smaller_primes(100000))
# print(eratosthenes(100))