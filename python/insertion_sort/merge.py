"""ALGORITHM Mergesort(list)
    DECLARE n <-- list.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- list[0...mid]
      DECLARE right <-- list[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, list)

ALGORITHM Merge(left, right, list)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            list[k] <-- left[i]
            i <-- i + 1
        else
            list[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in list to remaining values in right
    else
       set remaining entries in list to remaining values in left
"""


def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n // 2
        left = list[0:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list


if __name__ == "__main__":
    new_list = [8, 4, 27, 23, 42, 16, 15]
    print(merge_sort(new_list))
