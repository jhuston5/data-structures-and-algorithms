# Quick Sort - Code Challenge 28

[8,4,23,42,16,15]

This Quick Sort allows the pivot to be in any position in the list.

Parameters are a list, the left, and the right. So we would pass in (list, 0, len(list) - 1)
We include a conditional that will call the recursion as long as left is less than right.

We create a position variable that calls a partition method taking the same parameters (list, left, right)
We then define the partition method to find the partition, then recursively call quick sort.

Taking an example list in the partition method:
ex_list = [8,4,23,42,16,15]

Partition takes in (ex_list, 0, 5) and sets a pivot variable equal to the list[right].
pivot = 15

Next a low variable will track the largest index of numbers lower than the defined pivot. low = left - 1
low = -1

Iterate through the list from left to right.
Conditional: if list[i] <= pivot, increment low and call a new method, swap(list, i, low)
Loop:
list[i] is 8 <= pivot is 15
low += 1 (-1 => 0)
swap
list[i] is 4 <= pivot is 16
low +=1 (0 => 1)
swap
list[i] is 23 <= pivot is 42
low +=1 (1 => 2)
swap

Exit the iterative loop, then call swap again(list, right, low+1)

Return the pivot index point
return low + 1 (3)

The swap function creates a temp variable, sets the current list index to it, then swaps the list[i] to list[low]. To finish it off, list[low] is reset to the temp variable.

<!--
ALGORITHM QuickSort(list, left, right)
    if left < right
        // Partition the listay by setting the position of the pivot value
        DEFINE position <-- Partition(list, left, right)
        // Sort the left
        QuickSort(list, left, position - 1)
        // Sort the right
        QuickSort(list, position + 1, right)

ALGORITHM Partition(list, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- list[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if list[i] <= pivot
            low++
            Swap(list, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(list, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(list, i, low)
    DEFINE temp;
    temp <-- list[i]
    list[i] <-- list[low]
    list[low] <-- temp -->
