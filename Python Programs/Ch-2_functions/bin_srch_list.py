#Program for Binary Search in a list/array using Recursion
list = [3,5,7,11,33,66]

def binary_search(list1, element, low, high):
    low=0
    high= len(list1)
    mid=low + (high-low)/2
    if mid==len(list1):
        return False
    elif list1[mid]==element:
        return mid
    elif high==low:
        return False
    elif list1[mid]<element:
        return binary_search(list1, element, min, mid-1)
    elif list1[mid]>element:
        return binary_search(list1, element, mid+1, max)
    else:
        return mid
    
print(binary_search(list,11,0,5))
