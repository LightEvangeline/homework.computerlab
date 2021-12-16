x=int(input())
n=0
for i in range (2,x):
    if (x%i==0):
        print('not prime')
        n=1
        break
if (n==0):
    print('prime')
    