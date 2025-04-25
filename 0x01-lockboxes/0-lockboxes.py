#!/usr/bin/python3
"""
This module defines a function to check if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened starting from box 0."""
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set()       # Set of opened box indexes
    stack = [0]           # Start from box 0

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            # Add only new keys that are valid box numbers
            for key in boxes[current]:
                if isinstance(key, int) and 0 <= key < n and key not in visited:
                    stack.append(key)

    return len(visited) == n
