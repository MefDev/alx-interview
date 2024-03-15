#!/usr/bin/python3
"""Unlock all the boxes"""
from typing import List


def canUnlockAll(boxes: List[List[int]]):
    """Unlock all the boxes"""
    if (len(boxes) == 0):
        return False
    if (len(boxes) == 1):
        return True
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False
