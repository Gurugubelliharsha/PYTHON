#Write a program to print largest number among three numbers.
a,b,c=map(int,input().split())
max1= a if a>b else b
max2= a if a>c else c
print(max1) if max1>max2 else print(max2)