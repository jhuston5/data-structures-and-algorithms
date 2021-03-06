# Code Challenge 17 - Breadth First Traversal

This app creates a function that traverses a tree at each height of the tree, returning each value in order (breadth first)

### Functions:

- breadthFirst()

### Tests:

- Test if the a tree with only a root value will be returned a single list value
- Test for a multiple values
- Test for multiple values as part of a binary search tree

## Author: Joshua Huston

## Links and Resources

![Whiteboard](/python/img/code-challenge-17.png)

## Reflections and Comments

I made a couple of whiteboards here. Visualizing the step by step process of first the root value being enqueued, followed by its left and right, then dequeuing the root and moving down the height of the tree in that fashion made understanding the problem domain much easier.


# Code Challenge 16 - Max Value

This app creates a function that finds the maximum value in an unordered binary tree.

### Functions:

- max_val(): finds a maximum value within an unordered binary tree.

### Tests:

- Test if the a tree with only a root value will be returned as max
- Test for a max left leaf
- Test for a max right leaf
- Test for a max right-middle leaf
- Test for a max left-middle leaf

## Author: Joshua Huston

## Links and Resources

![Whiteboard](/python/img/code-challenge-16.png)

## Reflections and Comments

My whiteboard was extremely helpful for this lab. I was able to create a visualization that made sense to me, which made writing a clear algorithm and code far simpler for me. One challenge was finding a way to store the max variable in a recursive function, and the way I solved was to make the maxixum a nonlocal variable. Hopefully that is not a big programming worst practice!
# Code Challenge 15 - Trees

This app creates a Binary Tree class, as well as a Binary Search tree.

### Functions:

- in_order: left > root > right
- pre_order: root > left > right
- post_order: left > right > root
- add: adds value to binary tree
- contains: checks if value is in the tree, returns boolean

### Tests:

- empty root
- single root
- in_order
- pre_order
- post_order
- add
- contains

## Author: Joshua Huston

## Links and Resources

![Whiteboard](/python/img/code-challenge-15.png)

## Reflections and Comments

Tough lab here - trying to continue visualizing recursive functions and build them out appropriately. Overall, lots of learning in this lab.


