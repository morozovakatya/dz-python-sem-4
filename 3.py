list1 = [1, 4, 3, 1, 4, 7, 7, 9, 5]
list2 = []

for i in range(len(list1)):
    f = True
    for j in range(len(list1)):
        if list1[i] == list1[j] and i != j:
            f = False
            break
    if f == True:
        list2.append(list1[i])
print(list2)