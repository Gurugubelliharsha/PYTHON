#Write a method for increment and decrement operators(++, --) 
def inc_dec(n):
    n += 1
    print("After Increment:", n)
    n -= 1
    print("After Decrement:", n)
n=int(input())
print(inc_dec(n))