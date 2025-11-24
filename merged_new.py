# Q1
def euler_phi(n):
    r = n
    p = 2
    while p*p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            r -= r//p
        p += 1
    if n > 1:
        r -= r//n
    return r

print("1:", euler_phi(36))



# Q2
def mobius(n):
    if n == 1:
        return 1
    c = 0
    i = 2
    while i*i <= n:
        if n % i == 0:
            if (n//i) % i == 0:
                return 0
            c += 1
            n//=i
        else:
            i+=1
    if n > 1:
        c+=1
    return 1 if c % 2 == 0 else -1

print("2:", mobius(30))



# Q3
def divisor_sum(n):
    s = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i+=1
    return s

print("3:", divisor_sum(28))



# Q4
def prime_pi(n):
    if n < 2:
        return 0
    p = [True]*(n+1)
    p[0] = p[1] = False
    import math
    for i in range(2, int(math.isqrt(n))+1):
        if p[i]:
            for j in range(i*i, n+1, i):
                p[j] = False
    return sum(p)

print("4:", prime_pi(30))



# Q5
def legendre_symbol(a, p):
    return pow(a, (p-1)//2, p)

print("5:", legendre_symbol(5, 11))
# Q1
def factorial(n):
    if n < 0:
        return None
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

print("1:", factorial(5))



# Q2
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print("2:", is_palindrome(121))



# Q3
def mean_of_digits(n):
    s = str(abs(n))
    d = [int(i) for i in s]
    return sum(d) / len(d)

print("3:", mean_of_digits(12345))



# Q4
def digital_root(n):
    n = abs(n)
    while n >= 10:
        s = 0
        while n:
            s += n % 10
            n //= 10
        n = s
    return n

print("4:", digital_root(9876))



# Q5
def sum_proper_divisors(n):
    if n <= 1:
        return 0
    t = 1
    import math
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            t += i
            o = n // i
            if o != i:
                t += o
    return t

def is_abundant(n):
    return sum_proper_divisors(n) > n

print("5:", is_abundant(12))
import math
from typing import List

# Q6
def proper_divisors(n: int) -> List[int]:
    if n <= 1:
        return []
    divs = [1]
    limit = int(math.isqrt(n))
    for d in range(2, limit + 1):
        if n % d == 0:
            divs.append(d)
            other = n // d
            if other != d and other != n:
                divs.append(other)
    return sorted([d for d in divs if d < n])

def is_deficient(n: int) -> bool:
    return sum(proper_divisors(n)) < n

print("6:", is_deficient(12))


# Q7
def is_harshad(n: int) -> bool:
    if n == 0:
        return False
    s = sum(int(ch) for ch in str(abs(n)))
    return s != 0 and (n % s == 0)

print("7:", is_harshad(18))


# Q8
def is_automorphic(n: int) -> bool:
    sq = n * n
    return str(sq).endswith(str(n))

print("8:", is_automorphic(25))


# Q9
def is_pronic(n: int) -> bool:
    if n < 0:
        return False
    k = int((math.isqrt(1 + 4 * n) - 1) // 2)
    return k * (k + 1) == n

print("9:", is_pronic(20))


# Q10
def prime_factors(n: int) -> List[int]:
    n0 = n
    if n <= 1
# Q11
def count_distinct_prime_factors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        count += 1
    return count

n11 = 60
print("11:", count_distinct_prime_factors(n11))


# Q12
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_prime_power(n):
    for p in range(2, n + 1):
        if is_prime(p):
            power = p
            while power <= n:
                if power == n:
                    return True
                power *= p
    return False

n12 = 27
print("12:", is_prime_power(n12))


# Q13
def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    m = 2**p - 1
    return is_prime(m)

p13 = 5
print("13:", is_mersenne_prime(p13))


# Q14
def twin_primes(limit):
    twins = []
    for i in range(2, limit):
        if is_prime(i) and is_prime(i + 2):
            twins.append((i, i + 2))
    return twins

limit14 = 30
print("14:", twin_primes(limit14))


# Q15
def number_of_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
        i += 1
    return count

n15 = 36
print("15:", number_of_divisors(n15))
# Q16
def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

print("16:", aliquot_sum(12))


# Q17
def aliquot_sum(n):
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

def are_amlicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

print("17:", are_amlicable(220, 284))


# Q18
def multiplicative_persistence(n):
    steps = 0
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps

print("18:", multiplicative_persistence(39))


# Q19
def divisor_count(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

def is_highly_composite(n):
    div_n = divisor_count(n)
    for i in range(1, n):
        if divisor_count(i) >= div_n:
            return False
    return True

print("19:", is_highly_composite(12))


# Q20
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

print("20:", mod_exp(2, 10, 1000))
[19:03, 24/11/2025] NILANJANA: # Q21
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

print("21:", mod_inverse(3, 11))


# Q22
def chinese_remainder(moduli, remainders):
    M = 1
    for m in moduli:
        M *= m
    result = 0
    for m, r in zip(moduli, remainders):
        Mi = M // m
        inv = mod_inverse(Mi, m)
        result += r * Mi * inv
    return result % M

print("22:", chinese_remainder([3, 4, 5], [2, 3, 1]))


# Q23
def quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

print("23:", quadratic_residue(2, 7))


# Q24
def order(a, n):
    if a % n == 0:
        return None
    for k in range(1, n):
        if pow(a, k, n) == 1:
            return k
    return None

print("24:", order(2, 7))


# Q25
def is_fibonacci_prime(n):
    def is_fib(x):
        import math
        return int(math.isqrt(5*x*x + 4))*2 == 5*x*x + 4 or int(math.isqrt(5*x*x - 4))*2 == 5*x*x - 4

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return is_fib(n)

print("25:", is_fibonacci_prime(13))
# Q26
def lucas_sequence(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    seq = [2, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

print("26:", lucas_sequence(10))


# Q27
def is_perfect_power(n):
    if n <= 1:
        return False
    for a in range(2, int(n**0.5) + 1):
        b = 2
        while a**b <= n:
            if a**b == n:
                return True
            b += 1
    return False

print("27:", is_perfect_power(64))


# Q28
def collatz_length(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1
    return steps

print("28:", collatz_length(12))


# Q29
def polygonal_number(n, s):
    return ((s - 2) * n * (n - 1)) // 2 + n

print("29:", polygonal_number(5, 6))


# Q30
def is_carmichael(n):
    if n < 2:
        return False
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("30:", is_carmichael(561))
# Q31
def digital_root(n):
    while n > 9:
        s = 0
        for d in str(n):
            s += int(d)
        n = s
    return n

print("31:", digital_root(9876))



# Q32
def is_harshad(n):
    s = sum(int(d) for d in str(n))
    return n % s == 0

print("32:", is_harshad(21))



# Q33
def tribonacci(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    if n == 2:
        return [0,1,1]
    seq = [0,1,1]
    for i in range(3, n):
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq

print("33:", tribonacci(10))



# Q34
def is_smith_number(n):
    def prime_factors_sum(x):
        t = 0
        f = 2
        while x > 1:
            while x % f == 0:
                for d in str(f):
                    t += int(d)
                x //= f
            f += 1
        return t

    digit_sum = sum(int(d) for d in str(n))
    return digit_sum == prime_factors_sum(n)

print("34:", is_smith_number(666))
