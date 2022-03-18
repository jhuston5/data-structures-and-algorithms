# Code Challenge 32
<!-- Description of the challenge -->
Write a function called tree_intersection which takes an two binary trees as an argument. Utilize a hashmap to find values that intersect between the two trees.

## Whiteboard Process
<!-- Embedded whiteboard image -->

![Whiteboard](/python/img/code-challenge-32-tree-intersection.png)

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->
Added all nodes in the first tree to a hashmap, then called the contains function to check if values in the second tree were within the first.

## Collaboration
