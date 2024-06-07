#!/usr/bin/python3
'''lockboxes module'''
from collections import deque


def canUnlockAll(boxes):
    '''returns true if all boxes can be unlocked'''
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
