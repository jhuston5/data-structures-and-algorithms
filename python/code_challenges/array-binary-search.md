# array-binary-search Code Challenge 03
<!-- Description of the challenge -->
Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Whiteboard](/python/img/code-challenge-03-array-binary-search.png)

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
We used binary search, setting start and ending variables equal to the length of the array, then created a while loop that iterated while the start was less than end. We then used conditional logic to cut the array in half using the len function, then set the appropriate variable equal to the midpoint + or - 1 until we found the value and its index, then returned that index.

Big O = (O log n)

## Collaboration

Worked with Brandon Mizutani to develop algorithm and work through whiteboarding.


