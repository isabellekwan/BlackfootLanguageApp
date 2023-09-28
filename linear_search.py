# Linear Search
# Isabelle Kwan
# November 23, 2022


# With input and for loop
"""x = int(input("Shoe size: "))

shoeList = [1,2,3,4,5,6,7,12,14,16]

hasShoe = False

for i in range(len(shoeList)):
    if shoeList[i] == x:
        hasShoe = True
        
print(hasShoe)"""


# With Function (return bool)   
def linear_search_bool(lst,search):
    for item in lst:
        if item == search:
            return True
    return False

# With Function (return index)   
def linear_search_index(lst,search):
    i = 0
    while i < len(lst):
        if lst[i] == search:
            return i
        i+=1
    return None
        

# Testing
odd_num_lists = [1,2,3,4,5]
even_num_lists = [1,2,3,4]
empty_num = []

# print(linear_search_bool(odd_num_lists, 3))
# print(linear_search_bool(even_num_lists, 5))
print(linear_search_index(odd_num_lists, 3))        
