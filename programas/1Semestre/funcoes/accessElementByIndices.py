def accessElementByIndices(data, indices):
    try:
        for index in indices:
            data = data[index]
        return data
    except (IndexError, TypeError):
        return None


# Example usage:
C = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
indices = [1, 0, 1]  # The list [1, 4, 5] corresponds to indices [1, 0, 1]
result = accessElementByIndices(C, indices)

if result is not None:
    print(result)
else:
    print("Element not found")