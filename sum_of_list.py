# Sum of a List
# Isabelle Kwan
# November 21, 2022

# Input: list of integers numList
# Return: sum of integers in numList

# Solved with a loop
def listSum(numList):
    summ = 0
    for num in numList:
        summ += int(num)

    return summ

print(listSum([1,2,3,4,5,6]))

# Recursion
def listSum_recur(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum_recur(numList[1:])
    
print(listSum_recur([1,2,3,4,5,6]))
