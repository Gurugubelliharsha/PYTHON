#Write a program to palindrome or not.
n=int(input())
temp=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res*10+r
if temp==res:
    print('palindrome')
else:
    print('not a palindrome')