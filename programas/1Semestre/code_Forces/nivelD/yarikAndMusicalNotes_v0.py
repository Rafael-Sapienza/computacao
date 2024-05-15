import math
from icecream import ic

def howManyPairsOfNotesHaveSameCombination(n,A):
    #A eh a lista com as notas a1,..,an
    #n eh len(A)
    counter = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if A[j] + math.log(A[i],2) == A[i] + math.log(A[j],2):
                ic(i,j)
                print(A[i],A[j])
                counter += 1
    return counter
 
 
def solveProblemForAllTestCases(numberOfTestCases):
    for _ in range(numberOfTestCases):
        lengthOfArray = int(input())
        array = [int(r) for r in input().split()]
        numberOfPairs = howManyPairsOfNotesHaveSameCombination(lengthOfArray,array)
        print(numberOfPairs)
 
'''numberOfTestCases = int(input())
solveProblemForAllTestCases(numberOfTestCases)'''
 

n = 19
A = [2, 4, 1, 6, 2, 8, 5, 4, 2, 10, 5, 10, 8, 7, 4, 3, 2, 6, 10]
counter = howManyPairsOfNotesHaveSameCombination(n,A)
ic(counter)
 