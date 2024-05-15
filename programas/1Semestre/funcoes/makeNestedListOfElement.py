'''
def nested_list(A, depth=None, length=None):
    i=1
    if depth is None:
        depth = len(A)
    if length is None:
        length = A[-i]

    if depth == 1:
        return [0] * A[0]
    else:
        my_list = []
        i=0
        return [nested_list(A, depth=depth-1, length=A[-i-1]) for _ in range(length)]

# Define your list A
A = [2,1,3]  # Replace with your desired list

# Call the function with A as an argument
result = nested_list(A)
print(result)
'''

'''
def make_Nested_Lists_of_Zeros(A):
    if len(A) == 1:
        return [0] * A[0]
    else:
        B = A
        A.pop()
        return [make_Nested_Lists_of_Zeros(A) for _ in range(B[-1])]
A=[2,2,1]
print(make_Nested_Lists_of_Zeros(A))
'''

'''
def nested_list(A, depth=None, length=None):
    if depth is None:
        depth = len(A)
    if length is None:
        length = A[-1]

    if depth == 1:
        return [0] * A[0]
    else:
        my_list = []
        return [nested_list(A, depth=depth-1, length=A[-depth]) for _ in range(length)]

# Define your list A
A = [2,3,4]  # Replace with your desired list

# Call the function with A as an argument
result = nested_list(A)
print(result)
'''

'''
def makeNestedListOfElement(element, nestedListOfElement, depth=None, length=None,i=-1):
    if depth is None:
        depth = len(nestedListOfElement)
    if length is None:
        length = nestedListOfElement[i]

    if depth == 1:
        return [element] * nestedListOfElement[0]
    else:
        return [makeNestedListOfElement(element, nestedListOfElement, depth=depth-1, length=A[i-1],i=i-1) for _ in range(length)]
'''

#'''
def makeNestedListOfElement(element, A):
    i = 0
    result = element
    for i in range(len(A)):
        result = [result]*A[i]
    return result
#'''

# Define your list A
A = [2,3,2]  # Replace with your desired list

# Call the function with A as an argument
result = makeNestedListOfElement(0,A)
print(result)