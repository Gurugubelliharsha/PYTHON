#Write a program to find Armstrong number or not
n=int(input())
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res+r*r*r
if temp==res:
    print('armstrong')
else:
    print('not a armstrong')