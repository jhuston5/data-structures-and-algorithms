
# Code Challenge 12 - Validate Brackets

This app creates a validate brackets function that takes in a string of various bracket characters ({[]}) and determines if the brackets in the string are balanced.

## Validate Brackets

### Function:

- Created a dictionary of the bracket pairs
- Iterated through the string, checking if it was a key or a value.
- If it was a key, stored the char in a stack
- If it was a value, popped the most recent stack value and checked if they were the same.
- Continued through the whole string; if able to iterate through the whole thing do a final check to see if there is an empty stack
- Return true or false.

### Tests:

- Passing a correct string returns True
- Passing an incorrect string returns False
- Passing a string with characters other than brackets ignores those characters

## Author: Joshua Huston

## Links and Resources

![Whiteboard](/python/img/code-challenge-13.png)

## Reflections and Comments

This was a cool code challenge - thanks to hints from Roger and a member of our class, Wenhao, I felt like I was able to visualize and frame this problem very well. I'm sure there are more efficient ways to solve this problem, but I feel that I was able to come up with a solid solution that meets the parameters of the problem. All tests passing. I was very happy with how I methodically worked through this problem.


# Code Challenge 12 - Animal Shelter

This app creates an Animal Shelter class that uses a queue and a stack to determine what kinds of animals are taken out of the shelter.

## AnimalShelter

Functions:

- Enqueue: push in new "dog" or "cat" objects into the class
- Dequeue: traverse the queue to find a preferred animal, pushing animals that are not preferred onto a stack. After the preferred animal has been returned, pop the animals on the stack back to the front of the queue.

Tests:

- Enqueue into an empty queue
- Enqueue multiple animals
- Dequeue a single animal
- Dequeue an animal and ensure the queue is returned correctly

## Author: Joshua Huston

## Links and Resources

![Whiteboard](/python/img/code-challenge-12.png)

## Reflections and Comments

I created an Animal Shelter class that uses a queue and a stack to determine what kinds of animals are taken out of the shelter. To return a preferred animal, we traverse the queue to find a preferred animal, pushing animals that are not preferred onto a stack. After the preferred animal has been returned, pop the animals on the stack back to the front of the queue.



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


