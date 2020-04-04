# To create keys for RSA, one does the following steps:
# 1. Picks (randomly) two large prime numbers and calls them p and q.
# 2. Calculates their product and calls it n.
# 3. Calculates the totient of n ; it is simply ( p −1)(q −1).
# 4. Picks a random integer that is coprime to ) φ(n and calls this e. A simple way is to
# just pick a random number ) > max( p,q .
# 5. Calculates (via the Euclidean division algorithm) the multiplicative inverse of e
# modulo ) φ(n and call this number d. 

from math import gcd
import random

def isPrime(x):
    return 2 in [x,2**x%x]

def coprime(a, b):
    return gcd(a, b) == 1

def modinv(e, phi):
    d_old = 0; r_old = phi
    d_new = 1; r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None

p, q = 13, 17

print("p =", p)
print("q =", q)

n = p * q

print("n =", n)

phi_n = (p-1)*(q-1)

print("φ(n) =", phi_n)

primes = [i for i in range(1,n) if isPrime(i)]

coprimes = []

for x in primes:
    if (coprime(x, n)):
        coprimes.append(x)

e = random.choice(coprimes)

print("e =",e)

d = modinv(e, phi_n)

print("d =",d)

print("Public Key is (", n, ",", e, ")")
print("Private Key is (", n, ",", d, ")")
