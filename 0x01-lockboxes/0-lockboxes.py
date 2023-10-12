#!/usr/bin/python3

def canUnlockAll(boxes):
    # Check if the boxes list is empty
    if not boxes:
        return False

    # Get the total number of boxes
    num_boxes = len(boxes)

    # Create a list to keep track of visited boxes
    visited = [False] * num_boxes

    # Mark the first box (box 0) as visited since it's initially unlocked
    visited[0] = True

    # Create a queue for breadth-first search, starting with box 0
    queue = [0]

    # Perform breadth-first search to explore reachable boxes
    while queue:
        current_box = queue.pop(0)

        # Iterate through keys in the current box
        for key in boxes[current_box]:
            # Check if the key is within the valid range of boxes and if the box hasn't been visited
            if key < num_boxes and not visited[key]:
                # Mark the box as visited and add it to the queue for further exploration
                visited[key] = True
                queue.append(key)

    # Check if all boxes have been visited; if so, return True, otherwise, return False
    return all(visited)

# Example usage
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # False

