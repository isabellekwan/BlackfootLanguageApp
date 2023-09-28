# Binary Search
# Isabelle Kwan
# November 23, 2022

def binarySearch(lst,item):
    low = 0
    high = len(lst)-1
    found = False

    while low <= high and not found:
        mid = (low+high)//2
        if lst[mid] == item:
            found = True
        else:
            if item < lst[mid]:
                high = mid-1
            else:
                low = mid+1
                
    return found

print(binarySearch([1,2,3],0))
