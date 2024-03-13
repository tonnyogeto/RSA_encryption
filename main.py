
import random
import math

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        
    return True

def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
        
    raise ValueError("mod_inverse does not exist")

p, q = generate_prime(1000, 5000), generate_prime(1000, 5000)

while p == q:
    q = generate_prime(1000, 5000)

n = p * q
phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

print("Public key: ", e)
print("Private key: ", d)
print("n: ", n)
print("phi of n : ", phi_n)
print("p", p)
print("q", q)

message = input("Enter the message to be encrypted: ")

message_encoded = [ord(ch) for ch in message]
ciphertext = [pow(ch, e, n) for ch in message_encoded]

print("Ciphertext:", ciphertext)

message_encoded = [pow(ch, d, n) for ch in ciphertext]
decrypted_message = "".join(chr(ch) for ch in message_encoded)

print("Decrypted message:", decrypted_message)
