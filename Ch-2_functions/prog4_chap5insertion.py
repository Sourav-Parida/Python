# Insertion Sort
a = [70,49,31,6,65,81,68]
print("Original list : ", a)
for i in a:
    j = a.index(i)
    while j>0:
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            break
        j = j-1
print("List after sorting : ",a)
