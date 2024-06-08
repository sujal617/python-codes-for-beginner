list = []
numbers = int(input("enter elements required:"))
for i in range(0,numbers):
    value = int(input())
    list.append(value)
print("orignal list",list)

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            temp = list[i]
            list[i] = list[j];
            list[j] = temp

print("sorted list", list)