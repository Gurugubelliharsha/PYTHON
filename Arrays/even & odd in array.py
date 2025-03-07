# Write a method to find number of even number and odd numbers in an array
arr=list(map(int, input().split()))
even_count=0
odd_count=0
for n in arr:
    if n%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even:", even_count, "Odd:", odd_count)