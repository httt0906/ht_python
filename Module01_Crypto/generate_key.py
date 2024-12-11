# 生成密钥

from sympy import isprime, mod_inverse
import random


def generate_prime():
    while True:
        p = random.randint(2 ** 10, 2 ** 12)
        if isprime(p):
            return p


def generate_key_pair():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(1, phi_n)
    d = mod_inverse(e, phi_n)

    return (e, n), (d, n)