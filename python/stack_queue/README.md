
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


