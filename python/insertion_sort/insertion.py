"""InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp"""


def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]

        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
    return list


if __name__ == "__main__":
    new_list = [8, 4, 23, 42, 16, 15]
    print(insertion_sort(new_list))
