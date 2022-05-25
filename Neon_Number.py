n=int(input())
temp=n
s=0
k=n*n
while k>0:
    r=k%10
    s=s+r
    k=k//10
if s==temp:
    print("Neon Number")
else:
    print("Not Neon Number")