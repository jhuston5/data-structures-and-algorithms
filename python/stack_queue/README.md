
# Code Challenge 11 - PseudoQueue

This app creates a PseudoQueue data structures and implements the following functions.

## PseudoQueue

Functions:

- Enqueue
- Dequeue

Tests:

- Enqueue into an empty list
- Enqueue multiple values
- Dequeue a single value
- Dequeue multiple values
- Alternate between enqueue and dequeue

## Author: Joshua Huston

## Links and Resources

## Reflections and Comments


I created a PseudoQueue class that used two stacks, a temporary stack and a storage stack to mimic the functionality of a Queue. I created two functions, enqueue, and dequeue, which used built in Stack methods push and pop to move my Nodes to the appropriate stack in the correct order.


# Code Challenge 10 - Stack and Queue Implementation

This app creates a Stack and Queue data structures, and implements the following functions.

## Stack
- push
- pop
- peek
- isEmpty

## Queue

- enqueue
- dequeue
- peek
- isEmpty

## Author: Joshua Huston

## Links and Resources

https://docs.pytest.org/en/6.2.x/assert.html
https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html

## Reflections and Comments

I worked with Bionca Bond on the stack class functions.

Modularized the Node, Stack, and Queue classes, and separated Stack and Queue tests into their own files. Needs the python -m stack_queue.stack or stack_queue.queue command to run. I also learned how to use a pytest fixture to simplify some of my test creation.


