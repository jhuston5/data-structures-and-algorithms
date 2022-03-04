# Merge Sort

Merge Sorting is an algorithm that subdivides data to its lowest level and sorts, all in a recursive fashion.

It will take in an input array or list and then sort from there. It has a Big O notation time complexity of O(n.logn).

Take a sample unsorted list: [8,4,27,23,42,16,15]

This list will be sorted to: [4,8,15,16,23,27,42]

We start by splitting the list in half by finding the midpoint using the length of the list. These halves are then passed recursively back into merge_sort.
Left 1:
merge_sort([8,4,27,23])
Right 1:
merge_sort([42,16,15])

Left 2:
merge_sort([8,4])
merge_sort([27,23])

Right 2:
merge_sort([42,16])
merge_sort([15])

At the lowest level our last recursive function will look as follows:

- Skip additional merge_sort calls
- call merge([8], [4], [8,4])
- Iterates and sees that left[0] is > right[0] (8 > 4)
- sets the list[0] to 4.
- Iterates again, which sets list[1] to 8.

End with list = [4,8]

Continues up, so the next merge calls: merge([4,8], [23,27], [8,4,27,23])
Left[0] is less than right[0] (4 < 23)
list[0] = 4
list = [4,4,27,23]

left[1] <= right[0] (8 < 23)
list[1] = 8
list = [4,8,27,23]

i = left.length, so we set remaining values in list to right.
