n=int(input())
s=0
su=0
p=n**2
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
a=s**2
while a>0:
    r1=a%10
    su=su*10+r1
    a=a//10
if p==su:
    print("True")
else:
    print("False")