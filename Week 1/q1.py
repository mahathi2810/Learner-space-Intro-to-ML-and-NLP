import numpy as np

array = np.random.randint(1, 51, size=(5, 4))
print("Original array:")
print(array)

anti_diagonal = [array[i, array.shape[1] - 1 - i] for i in range(min(array.shape))]
print("\nAnti-diagonal elements:")
print(anti_diagonal)

row_max = np.max(array, axis=1)
print("\nMaximum value in each row:")
print(row_max)

mean_value = np.mean(array)
filtered_elements = array[array <= mean_value]
print(f"\nOverall mean of the array: {mean_value:.2f}")
print("Elements less than or equal to the mean:")
print(filtered_elements)

def numpy_boundary_traversal(matrix):
    rows, cols = matrix.shape
    result = []

    for j in range(cols):
        result.append(matrix[0][j])
    
    for i in range(1, rows):
        result.append(matrix[i][cols - 1])
    
    if rows > 1:
        for j in range(cols - 2, -1, -1):
            result.append(matrix[rows - 1][j])
    
    if cols > 1:
        for i in range(rows - 2, 0, -1):
            result.append(matrix[i][0])
    
    return result

boundary_elements = numpy_boundary_traversal(array)
print("\nBoundary elements in clockwise order:")
print(boundary_elements)
