try:
    from stack_queue.stack import Stack
    from stack_queue.node import Node

except:
    from stack import Stack
    from node import Node


def validate_brackets(str):
    # Create dictionary of values to compare
    brackets = {"{": "}", "[": "]", "(": ")"}
    S = Stack()

    # Iterate through all the characters in the string
    for i in range(0, len(str)):
        # Check if the character is in the bracket keys - if it is, push into a stack.
        if str[i] in brackets.keys():
            S.push(str[i])
        # If a character is in the bracket values, pop the first item off the stack
        elif str[i] in brackets.values():
            stack_item = S.pop()
            # Check if the stack item and the string character are the same
            if brackets[stack_item] == str[i]:
                continue
            else:
                return False
        # Catch any other characters and ignore them
        else:
            continue

    # Final check to catch instances of an extra value in the string.
    if S.isEmpty() == True:
        print("True")
        return True
    else:
        print("False")
        return False


if __name__ == "__main__":

    validate_brackets("(({{morgan}}))")
