# Write a function to find the duplicate values of an array
arr = list(map(int, input().split()))
d = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in d:
            d.append(arr[i])
print("Duplicates:", d if d else "No Duplicates")