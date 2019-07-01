Seed=open('key', 'r')
Cip=open('random.txt', 'w')
x=int(Seed.read())
a=5000
b=50001
p=10000079
count=1
while count<=p-1:
    x=(a*x+b)%p
    count+=1
    Cip.write(str(x) + '\n')
