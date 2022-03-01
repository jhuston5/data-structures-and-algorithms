# Insertion Sort

'''
 InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp'''

[8,4,23,42,16,15]

Round 1
i = 1
j = 0
temp = arr[i(1)] = 4

temp = 4 < arr[j(0)] = 8
    arr[0 + 1] = arr[0] = 8
    j(0) = 0 - 1  = -1

arr[-1 + 1] =>  arr[0] = temp => 4

[4, 8, 23, 42, 16, 15]

Round 2
i = 2
j = 1
temp = arr[i(2)] = 23

    temp = 23 < arr[j(1)] = 8
    exit while

arr[1 + 1] => arr[2] = temp => 23

[4, 8, 23, 42, 16, 15]

Round 3
i = 3
j = 2
temp = arr[i(3)] = 42

    temp = 42 < arr[j(2)] = 23
    exit while
[4, 8, 23, 42, 16, 15]

Round 4
i = 4
j = 3
temp = arr[i(4)] = 16

    temp = 16 < arr[j(3)] = 42
    arr[3(j) + 1] => arr[3(j)] = 42
    j = j(3) - 1 = 2
    [4, 8, 23, 42, 42, 15]

    temp = 16 < arr[j(2)] = 23
    arr[2(j) + 1] => arr[2(j)] = 23
    j = j(2) - 1 = 1
    [4, 8, 23, 23, 42, 15]

    temp = 16 < arr[j(1)] = 8
    exit while

arr[j(1) + 1] => temp = 16
[4, 8, 16, 23, 42, 15]

Round 5
i = 5
j = 4
temp = arr[i(5)] = 15

    temp = 15 < arr[j(4)] = 42
    arr[4(j) + 1] => arr[4(j)] = 42
    j = j(4) - 1 = 3
    [4, 8, 16, 23, 42, 42]

    temp = 15 < arr[j(3)] = 23
    arr[3(j) + 1] => arr[3(j)] = 23
    j = j(3) - 1 = 2
    [4, 8, 16, 23, 23, 42]

    temp = 15 < arr[j(2)] = 16
    arr[2(j) + 1] => arr[2(j)] = 16
    j = j(2) - 1 = 1
    [4, 8, 16, 16, 23, 42]

arr[j(1) + 1] => temp = 15
[4, 8, 15, 16, 23, 42]

// Definitions

Insertion sort iterates through an array using nested for loops.

Insertion sort first takes the array length for the outer loop.

Next, it iterates through that array length starting at a standard index number.

The outside for loop is acting as a pointer. The while loop is sorting everything before the pointer, and does so every time the pointer is shifted ahead.
