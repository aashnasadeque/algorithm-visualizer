def quicksort(arr):
    """
    Quicksort algorithm: Sorts an array using the divide-and-conquer approach.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    """
    Mergesort algorithm: Recursively divides and merges an array.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Helper function for Mergesort: Merges two sorted arrays.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapsort(arr):
    """
    Heapsort algorithm: Uses a heap structure to sort an array.
    """
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def bubblesort(arr):
    """
    Bubble Sort algorithm: Repeatedly swaps adjacent elements if they are in the wrong order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def timsort(arr):
    """
    TimSort algorithm: Uses Python's built-in sorted() method.
    """
    return sorted(arr)

def radix_sort(arr):
    """
    Radix Sort algorithm: Efficiently sorts integers using counting sort on each digit.
    """
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def counting_sort(arr, exp):
    """
    Helper function for Radix Sort: Performs counting sort based on a specific digit.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test_data)
    print("Quicksort:", quicksort(test_data[:]))
    print("Mergesort:", mergesort(test_data[:]))
    print("Heapsort:", heapsort(test_data[:]))
    print("Bubblesort:", bubblesort(test_data[:]))
    print("TimSort:", timsort(test_data[:]))
    print("Radix Sort:", radix_sort(test_data[:]))
