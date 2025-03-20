class Node:
    def __init__(self, value : int, children = []):
        self.value = value
        self.children = children

def depth_first_search(head : Node, n, debug=False):
    """
    Depth first search on the head of a tree to find a node.
    Use for deep traversals.

    :param head: The head of tree / subtree.
    :param target: The node value to search for.
    :return: True if the node exists, else False
    """
    stack = []
    stack.append(head)
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.value) if debug else None
        if curr.value == n:
            return True
        for child in curr.children:
            stack.append(child)
    return False
    

if __name__ == "__main__":
    
    leaf1 = Node(1)
    leaf2 = Node(2)
    leaf3 = Node(8)
    leaf4 = Node(3)

    mid1 = Node(4, [leaf1])
    mid2 = Node(7, [leaf2, leaf3, leaf4])

    head = Node(6, [mid1, mid2])
    
    print(depth_first_search(head, 9, True))

    
    