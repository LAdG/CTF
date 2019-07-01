import math
import hashlib

def add_chain(n):
    a=0
    b=[]
    while n!=0:
        a=int(math.floor(math.log2(n)))
        n=int(int(n)-int(pow(2,a)))
        b.append(a)
    b.reverse()
    return b

def sum_chain(c,e):
    len=0
    result=0
    while len<e:
        gen=1
        d=0
        while d!=c[len]:
            gen=int(int(gen)+int(gen))
            d+=1
        result=int(int(result)+int(gen))
        len+=1
    return result

x=add_chain(4806464622629061490274796446790981398827884839419)
count=len(x)
y=sum_chain(x,count)
print(x)
print(y)

#import hashlib
#result = hashlib.md5(b'Python rocks!')
#print(int(result.hexdigest(),16))
# b'\x14\x82\xec\x1b#d\xf6N}\x16*+[\x16\xf4w'
