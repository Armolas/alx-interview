#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    opened = set()
    queue = deque([0])
    
    while queue:
        current = queue.popleft()
        if current not in opened:
            opened.add(current)
            for key in boxes[current]:
                if key < n and key not in opened:
                    queue.append(key)
    
    return len(opened) == n
