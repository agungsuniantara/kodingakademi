def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def smallest_of_array(arr, start, end):
    if end == start + 1:
        return arr[start]

    smallest_of_left = smallest_of_array(arr, start, (start + end) // 2)
    smallest_of_right = smallest_of_array(arr, (start + end) // 2, end)

    if (smallest_of_left < smallest_of_right):
        return smallest_of_left
    else:
        return smallest_of_right

if __name__ == "__main__":
    arr = [15, 8, 23, 4, 42, 16]
    sorted_arr = merge_sort(arr)
    print("array after sorting : ")
    for element in sorted_arr:
        print(element, end=" ")
    print()

    min_element = smallest_of_array(sorted_arr, 0, len(sorted_arr))
    print("min element : ", min_element)