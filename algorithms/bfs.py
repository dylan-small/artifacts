from collections import deque

class Node:
    def __init__(self, value : int, children = []):
        self.value = value
        self.children = children

def breadth_first_search(head : Node, n, debug=False):
    """
    Breadth first search on the head of a tree to find a node.
    Use for level traversals.

    :param head: The head of tree / subtree.
    :param target: The node value to search for.
    :return: True if the node exists, else False
    """
    queue = deque()
    queue.append(head)
    while len(queue) > 0:
        curr = queue.popleft()
        print(curr.value) if debug else None
        if curr.value == n:
            return True
        for child in curr.children:
            queue.append(child)
    return False
    

if __name__ == "__main__":
    
    leaf1 = Node(1)
    leaf2 = Node(2)
    leaf3 = Node(8)
    leaf4 = Node(3)

    mid1 = Node(4, [leaf1])
    mid2 = Node(7, [leaf2, leaf3, leaf4])

    head = Node(6, [mid1, mid2])
    
    print(breadth_first_search(head, 9, True))

    
    