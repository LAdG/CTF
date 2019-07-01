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

def xgcd(b, a):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while a != 0:
        q, b, a = int(b // a), a, int(b % a)
        x0, x1 = x1, int(x0 - q * x1)
        y0, y1 = y1, int(y0 - q * y1)
    #if y0<0:
    #    y0=b-y0
    return y0

def mod_exp(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent & 1) == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
        #print('base:',base)
        #print('exponent:',exponent)
    #print('result:',result)
    return result

def add_point(a,b,module,P1,P2):
    P3 = ['None', 'None']
    if P1[0] == P2[0] and P1[1] == P2[1]:
        la = int(((int(((int((3*(int((mod_exp(P1[0],2,module)) % module)) % module)) + a))) % module) * (xgcd(module, ((2*P1[1]) % module))))%module)
    else:
        la = int((int((P2[1] - P1[1])) * int(xgcd(module, ((P2[0] - P1[0]) % module)))) % module)
    P3[0] = (mod_exp(la,2,module) - P1[0] - P2[0]) % module
    P3[1] = (la * (P1[0] - P3[0]) - P1[1]) % module
    #Проверка корней
    if (mod_exp(P3[1],2,module) != ((mod_exp(P3[0],3,module) + ((a*P3[0]) % module) + b)) % module):
        print('Bad', 'P1:',P1,'P2:',P2,'P3:',P3)
        print('la:', la)
    return P3

def sum_chain(a,b,c,e,module,gen):
    len=0
    result=['None', 'None']
    while len<e:
        d=0
        while d!=c[len]:
            gen=add_point(a,b,module,gen,gen)
            d+=1
        if result==['None', 'None']:
            result=gen
        else:
            result=add_point(a,b,module,result,gen)
        len+=1
    return result

optext=open('Document1.docx','rb')
parameters=open('parameters','r')
seed=open('seed','r+')
key=open('key','r')
sign=open('sign1','w')
pam=parameters.readlines()
k=key.read()
opt=optext.read()
a=int(pam[0])
b=int(pam[1])
module=int(pam[2])
gen=[int(pam[3]),int(pam[4])]
order=int(pam[5])
Q=[int(pam[6]),int(pam[7])]
s=seed.read()
#a=1
#b=1
#module=5
#gen=[0,1]
pt=add_chain(1043476)
G=sum_chain(a,b,pt,len(pt),module,gen)
print(G)
count=2
P1=gen
P2=gen
P3=['None','None']
while count<=2092255:
    P3=add_point(a,b,module,P1,P2)
    P1=P3
    count+=1
    print(P3)
    print('count:',count)
#print(add_point(a,b,module,sum_chain(a,b,add_chain(286245805),len(add_chain(286245805)),module,gen),gen))
print(gen)
print(a)
print(b)
print(module)
P1=gen


count=2
#while P3[0]!=0:#and(P3[1]!=35307784)):
#    P3=add_point(a,b,module,P1,P2)
#    P1=P3
#    count+=1
    #print('count:',count)
print('count:',count)
l=[]
l.append(gen)
count=1
while count<1447:
#while count<4:
    if count==1:
        l.append(add_point(a,b,module,gen,gen))
    else:
        l.append(add_point(a,b,module,l[count-1],gen))
        #print(l[count-1])
    count+=1
buf=l[1446]
print(buf)
alpha=[buf[0],int(int(module)-int(buf[1]))]
gamma=alpha
x=l.count(gamma)
count=1
while count<1447:
#while count<4:
    if x!=0:
        n=int(int(int(1447)*int(count))+int(int(l.index(gamma))+1))
        #n=int(int(int(4)*int(count))+int(int(l.index(gamma))+1))
        break
    else:
        gamma=add_point(a,b,module,gamma,alpha)
        x=l.count(gamma)
        count+=1
        if count==1447:
            print(count)
print(n)

#Z=add_point(a,b,module,sum_chain(a,b,add_chain(int(a*int(s))),len(add_chain(int(a*int(s)))),module,gen),sum_chain(a,b,add_chain(int(b*int(s))),len(add_chain(int(b*int(s)))),module,sum_chain(a,b,add_chain(int(s)),len(add_chain(int(s))),module,gen)))
#hash1 = hashlib.md5(str(Z[0]).encode())
#s=int(hash1.hexdigest(),16)
#R=sum_chain(a,b,add_chain(int(s)),len(add_chain(int(s))),module,gen)
#r=int(R[0]%order)
#hm=hashlib.md5(opt)
#hm=int(hm.hexdigest(),16)
#sgn=int((int((int(s)*int(hm))%order)+int((int(k)*int(r))%order))%order)
#Verify
#Q1=[int(Q[0]),int(int(module)-int(Q[1]))]
#ag=int((int(xgcd(int(order),int(hm)))*int(sgn))%order)
#aq=int((int(xgcd(int(order),int(hm)))*int(r))%order)
#lg=add_chain(ag)
#lq=add_chain(aq)
#G1=sum_chain(a,b,lg,len(lg),module,gen)
#Q1=sum_chain(a,b,lq,len(lq),module,Q1)
#R1=add_point(a,b,module,G1,Q1)
#if R1[0]==r:
#    print('True')
#else:
#    print('False')
