import numpy as np

arr = np.random.uniform(0, 10, size=20)

rounded_arr = np.round(arr, 2)
print("Original array (rounded):")
print(rounded_arr)

min_val = np.min(rounded_arr)
max_val = np.max(rounded_arr)
median_val = np.median(rounded_arr)

print(f"\nMinimum value: {min_val}")
print(f"Maximum value: {max_val}")
print(f"Median value: {median_val}")


modified_arr = rounded_arr.copy()
modified_arr[modified_arr < 5] = modified_arr[modified_arr < 5] ** 2
print("\nArray after squaring elements less than 5:")
print(np.round(modified_arr, 2))

def numpy_alternate_sort(array):
    sorted_arr = np.sort(array)
    result = []

    left = 0
    right = len(sorted_arr) - 1

    while left <= right:
        if left == right:
            result.append(sorted_arr[left])
        else:
            result.append(sorted_arr[left])
            result.append(sorted_arr[right])
        left += 1
        right -= 1

    return np.array(result)

alt_sorted_arr = numpy_alternate_sort(rounded_arr)
print("\nAlternating sort (smallest, largest, second smallest, ...):")
print(np.round(alt_sorted_arr, 2))
