def findAllElementInNestedList(data, element_to_find, index=[]):
    indexes = []
    for i, item in enumerate(data):
        if item == element_to_find:
            indexes.append(index + [i])
        elif isinstance(item, list):
            indexes.extend(findAllElementInNestedList(item, element_to_find, index + [i]))
    return indexes


def find_all_element_in_nested_tuple(data, element_to_find, index=[]):
    indexes = []
    for i, item in enumerate(data):
        if item == element_to_find:
            indexes.append(index + [i])
        elif isinstance(item, tuple):
            indexes.extend(find_all_element_in_nested_tuple(item, element_to_find, index + [i]))
    return indexes


def find_all_element_in_nested_structure(data, element_to_find, index=[]):
    indexes = []

    if isinstance(data, (list, tuple)):
        for i, item in enumerate(data):
            if item == element_to_find:
                indexes.append(index + [i])
            elif isinstance(item, (list, tuple)):
                indexes.extend(find_all_element_in_nested_structure(item, element_to_find, index + [i]))

    return indexes



'''
# Test the function with nested lists

nested_list=[['banana', 'cherry'],0,[0 , 1, 9 + 6j, ['banana', 'cherry']]]
element=['banana','cherry']
results = find_all_element_in_nested_list(nested_list, element)

if results:
    print(f'{element} foi encontrado em:{results}')
else:
    print(f'{element} não foi encontrado')


# Test the function with nested tuples

nested_tuple=(('banana', 'cherry'),0,(0 , 1, ('banana', 'cherry')))
element=('banana','cherry')
results = find_all_element_in_nested_tuple(nested_tuple, element)


if results:
    print(f'{element} foi encontrado em:{results}')
else:
    print(f'{element} não foi encontrado')


# Test the function with nested lists and tuples
nested_structure = [1, (2, 3, ['banana','cherry']), 6, [7, [8, ('banana','cherry')]]]
element_to_find = ('banana','cherry')  # Replace with the element you want to find
results = find_all_element_in_nested_structure(nested_structure, element_to_find)

if results:
    print(f"The element {element_to_find} was found at these indexes:", results)
else:
    print(f"The element {element_to_find} was not found in the nested structure.")
'''
