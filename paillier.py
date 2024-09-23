import random
import math
from sympy import mod_inverse

def generate_paillier_keypair(key_length):
    def generate_large_prime(bit_length):
        while True:
            prime_candidate = random.getrandbits(bit_length)
            if is_prime(prime_candidate):
                return prime_candidate

    def is_prime(n, k=5):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        else:
            for _ in range(k):
                a = random.randint(2, n - 2)
                if pow(a, n - 1, n) != 1:
                    return False
            return True

    p = generate_large_prime(key_length // 2)
    q = generate_large_prime(key_length // 2)
    n = p * q
    n_sq = n * n
    lam = (p - 1) * (q - 1) // math.gcd(p - 1, q - 1)
    g = n + 1
    def L(x):
        return (x - 1) // n
    mu = mod_inverse(L(pow(g, lam, n_sq)), n)
    public_key = (n, g)
    private_key = (lam, mu)
    return public_key, private_key
