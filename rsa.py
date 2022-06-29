from Crypto.Util import number
# PyCryptodome

from random import randint as insecure_rand_int

# Converted from Wikipedia's pseudo-code
def mod_mult_inverse(a, n):
  t = 0     
  new_t = 1
  r = n
  new_r = a

  while new_r != 0:
    quotient = r // new_r
    t, new_t = new_t, t - quotient * new_t 
    r, new_r = new_r, r - quotient * new_r

  if r > 1:
    return "a is not invertible"
  if t < 0:
    t = t + n

  return t

# Converted from Wikipedia's pseudo-code
def gcd_euclid(a, b):
  old_r, r = a, b
  old_s, s = 1, 0
  old_t, t = 0, 1
  
  while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s
    old_t, t = t, old_t - quotient * t

  return old_r

# Converted from Wikipedia's pseudo-code
def mod_exp(b, e, m):
  if m == 1:
    return 0
  r = 1
  b = b % m
  while e > 0:
    if e % 2 == 1:
      r = (r*b) % m
    b = (b*b) % m
    e >>= 1
  return r



e = 65537
while True:
  p = number.getPrime(512)
  q = number.getPrime(512)
  phi = (p - 1) * (q - 1)
  if gcd_euclid(e, phi) == 1:
    break

print("p: " + str(p) + "\n")
print("q: " + str(q) + "\n")


n = p * q
print("n: " + str(n) + "\n")
d = mod_mult_inverse(e, phi)
print("d: " + str(d) + "\n")

m = int(input("Message to encrypt:  "))
encrypted_m = mod_exp(m, e, n)
print("\nEncrypted message: " + str(encrypted_m) + "\n")

m = int(input("Message to decrypt:  "))
decrypted_m = mod_exp(m, d, n)
print("\nDecrypted message: " + str(decrypted_m) + "\n")