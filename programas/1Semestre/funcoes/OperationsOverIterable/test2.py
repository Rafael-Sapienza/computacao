import copy

def update_nested_list(A, indices, value):
    ACopy = copy.deepcopy(A)
    current_list = ACopy

    # Traverse the nested structure using the provided indices
    for index in indices[:-1]:
        current_list = current_list[index]

    # Update the value at the final index
    current_list[indices[-1]] = value
    return ACopy

# Example usage:
my_list = [1,[2,3]]
index_to_change = [1, 1]

my_list = update_nested_list(my_list, index_to_change, 'a')

# Verify the change
print(my_list)
