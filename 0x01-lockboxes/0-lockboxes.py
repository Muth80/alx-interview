#!/usr/bin/python3
"""
This module contains the canUnlockAll function which determines if all
the boxes can be opened based on the keys each box contains.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Parameters:
    boxes (List[List[int]]): A list of lists, where each sublist represents the keys in a box.

    Returns:
    boolean: True if all boxes can be opened, False otherwise.
    """
    unlocked = [False] * len(boxes)  # Initialize all boxes to be locked
    unlocked[0] = True  # The first box is unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()  # To store any new keys found in this iteration
        for key in keys:
            if key < len(boxes) and not unlocked[key]:
                unlocked[key] = True  # Unlock the box with the current key
                new_keys.update(boxes[key])  # Add keys from the unlocked box
        keys = new_keys  # Update keys for the next iteration
    
    return all(unlocked)  # Check if all boxes are unlocked

# This is the test code that you provided.
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False
