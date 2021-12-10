# Insert and shift an array in middle at index Code Challenge 02

<!-- Description of the challenge -->
Write a function called insertShiftArray which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Whiteboard](img/code-challenge-02-insert-shift-array.png)

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
We found the midpoint of the given array using the len function, then ran a for loop from the midpoint to the end of the array. We inserted the new value into the middle, then reassigned the replaced value to make it the insertion on the next for loop.
We then appended the final element and returned the modified array.

## Collaboration

Worked with Wenhao Piao to develop algorithm and work through whiteboarding.
