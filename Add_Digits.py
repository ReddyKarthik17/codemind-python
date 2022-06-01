n=int(input())
s=0
s1=0
s2=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
while s>0:
    r1=s%10
    s1=s1+r1
    s=s//10
while s1>0:
    r2=s1%10
    s2=s2+r2
    s1=s1//10
print(s2)