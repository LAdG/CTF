import random

def rmspp(number, attempts=100):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # Given an odd integer n, let n = 2**r*s+1, with s odd... 
    s = number - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s = s//2
    while attempts:
        # ... choose a random integer a with 1 ≤ a ≤ n-1
        a = random.randint(1, number-1)
        # Unless a**s % n ≠ 1 ...
        if mod_exp(a, s, number) != 1:
            # ... and a**((2**j)*s) % n ≠ -1 for some 0 ≤ j ≤ r-1 
            for j in range(0, r):
                if mod_exp(a, (2**j)*s, number) == number-1:
                    break
            else:
                return False
        attempts -= 1
        continue
    # A prime will pass the test for all a.
    print(number)
    return True

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent & 1) == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

a=0
number = 4806464622629061490274796446790981398827884839533
while a==0:
    b=rmspp(number)
    if b==True:
        print(number)
        a=number
    else:
        a=0
        number-=1
