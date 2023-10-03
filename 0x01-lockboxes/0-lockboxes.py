#!/usr/bin/python3

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False
    # Sets the first box to unlocked
    unlocked = {0}
    # Start with the keys in the first box
    stack = boxes[0]
    while stack:
        key = stack.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            stack += boxes[key]
    # Checks if all boxes have been unlocked
    if len(unlocked) == len(boxes):
        return True
    return False
