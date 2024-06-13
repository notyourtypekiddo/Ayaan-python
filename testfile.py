n = int(input(""))
arr = [int(i) for i in input().split()]
MaxElement2 = 0
MaxElement = 0
for i in arr:
    if i > MaxElement:
        MaxElement = i

for j in arr:
    if j > MaxElement2 and j != MaxElement: 
        MaxElement2 = j
print(MaxElement2)