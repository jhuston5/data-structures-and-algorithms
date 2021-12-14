def array_binary_search(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) / 2
        if arr[mid] < val:
            left = mid + 1
        elif arr[mid] > val:
            right = mid - 1
        else:
            return mid
    return -1
