#!/usr/bin/python3
#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """the method determines if all the boxes can be opened.
    """
    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    v = [False] * n
    v[0] = True
    stack = [0]

    while stack:
        cb = stack.pop()
        for key in boxes[cb]:
            if 0 <= key < n and not v[key]:
                v[key] = True
                stack.append(key)

    return all(v)
