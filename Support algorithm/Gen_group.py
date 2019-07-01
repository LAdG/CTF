#n=int(4806464622629061490274792062060831148273872862719)
#print(n)
import math
import random

#number=int(4806464622629061490274792062060831148273872862719)

#for i in range(2, int(math.sqrt(number)) + 1): # обычно делитель не будет больше корня
#    while (number % i == 0): # while, а не if
#        print(i)
#        number //= i # убираем множитель из числа
#
#if (number != 1): # но один делитель может быть больше корня
#    print (number)

#def mmi(a, m):
#    """
#    mmi(a, m) -> x, such as ax % m = 1
#    mmi is a Modular Multiplicative Inverse
#    See http://en.wikipedia.org/wiki/Modular_multiplicative_inverse
#    """
#    gcd, x, q = egcd(a, m)
#    if gcd != 1:
#        # The a and m are not coprimes, so the inverse doesn't exist
#        return None
#    else:
#        return (x + m) % m

#def egcd(a, b):
#    """
#    egcd(a, b) -> d, x, y, such as d == gcd(a, b) == ax + by
#    egcd is an Extended Greatest Common Divisor
#    http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
#    """
#    if b == 0:
#        return (a, 1, 0)
#    else:
#        d, x, y = egcd(b, a % b)
#        return d, y, x - y * (a / b)

def euklid(x,y):
    a2=1
    a1=0
    b2=0
    b1=1
    while y!=0:
        q=int(x//y)
        r=int(x-q*y)
        a=int(a2-q*a1)
        b=int(b2-q*b1)
        x=y
        y=r
        a2=a1
        a1=a
        b2=b1
        b1=b
    d=x
    a=a2
    b=b2
    if b<0:
        b=x-b
    return b

k=int(1*euklid(2089361,1727))
a=int((3*k)%2089361)
b=int((2*k)%2089361)
print('a:',a)
print('b:',b)

def Jacobi(a,n):
    g=1
    c=0
    s=0
    cicle=0
    Jac=2
    while (Jac!=0) or (Jac!=1) or (Jac!=1):
        k=0
        if a==0:
            Jac=0
            break
        if a==1:
            Jac=g
            break
        if a%2==1:
            a1=a
        else:
            while a%2!=1:
                a1=a/2
                a=a1
                k+=1
        if k%2==0:
            s=1
        if k%2==1:
            if (n%8==1) or (n%8==7):
                s=1
            if (n%8==3) or (n%8==5):
                s=-1
        if a1==1:
            Jac=g*s
            break
        if (n%4==3) and (a%4==3):
            s=-s
        a=n%a1
        n=a1
        g=g*s
    return Jac

x=Jacobi(2691286213133933098492023117552300938263367144325,4806464622629061490274792062060831148273872862719)
#print('x:',x)
n=0
while n!=-1:
    y=random.randint(1,4806464622629061490274792062060831148273872862719-1)
    n=Jacobi(y,4806464622629061490274792062060831148273872862719)
print('y:',y)

def mod_exp(base, exponent, modulus):
    """
    mod_exp(b, e, m) -> value of b**e % m
    Calculate modular exponentation using right-to-left binary method.
    http://en.wikipedia.org/wiki/Modular_exponentiation#Right-to-left_binary_method
    """
    result = 1
    while exponent > 0:
        if (exponent & 1) == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
        print('base:',base)
        print('exponent:',exponent)
    print('result:',result)
    return result

def xsquaremodp(a,n,p):
    k=0
    h=0
    s=p-1
    cicle=0
    while s%2!=1:
        h=int(s/2)
        s=int(s/2)
        k+=1
    q=int((h+1)/2)
    a1=mod_exp(a,q,p)
    a2=euklid(p, a)
    if a2<0:
        a2=p+a2
    N1=mod_exp(n,h,p)
    print('k:',k)
    print('a2:',a2)
    print('h:',h)
    print('a1:',a1)
    print('N1:',N1)
    N2=1
    j=0
    l=0
    while l<=(k-2):
        b=int((a1*N2)%p)
        c=int((a2*(b**2))%p)
        d=mod_exp(c,pow(2,k-2-l),p)
        print('b:',b)
        print('c:',c)
        print('d:',d)
        if d==1:
            j=0
        if d==(p-1):
            j=1
        N2=int((N2*(mod_exp(N1,pow(2,l)*j,p)))%p)
        l+=1
        print('l:',l)
    x=int((a1*N2)%p)
    return x

#x=xsquaremodp(int(2115178409495128391782768944508530210010505718396),int(2727878771570635667470624789506652556429696443279),int(4806464622629061490274792062060831148273872862719))
#x=xsquaremodp(14,5,193)
#x=chast(111,3309827395359073677575056443294178612811407223396,4707712943677762896513347918837402781112937456366,2403232311314530745137396031030415574136936432223)
x=0
if mod_exp(1460608099654978979279369363498468306046158122449,2,4806464622629061490274792062060831148273872862719)==2115178409495128391782768944508530210010505718396:
    x=1
else:
    x=-1
print('x:',x)
