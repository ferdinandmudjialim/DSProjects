# Ferdinand Mudjialim, Barrett Barnard
# Insert method reference
# https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# Delete method reference
# http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Trees/AVL-delete.html


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1


# AVL Helper Functions


def getHeight(node):
    if node is None:
        return 0
    else:
        return node.height


def rotateLeft(z):
    oldparent = z.parent

    y = z.right
    T2 = y.left

    # Update parents
    z.parent = y
    y.parent = oldparent
    if T2 is not None:
        T2.parent = z

    # Update oldparent's child
    if oldparent is None:
        pass
    elif z == oldparent.left:
        oldparent.left = y
    elif z == oldparent.right:
        oldparent.right = y

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(getHeight(z.left),
                       getHeight(z.right))
    y.height = 1 + max(getHeight(y.left),
                       getHeight(y.right))
    return y


def rotateRight(z):
    oldparent = z.parent

    y = z.left
    T3 = y.right

    # Update parents
    y.parent = oldparent
    z.parent = y
    if T3 is not None:
        T3.parent = z

    # Update oldparent's child
    if oldparent is None:
        pass
    elif z == oldparent.left:
        oldparent.left = y
    elif z == oldparent.right:
        oldparent.right = y

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(getHeight(z.left),
                       getHeight(z.right))
    y.height = 1 + max(getHeight(y.left),
                       getHeight(y.right))
    return y


def rebalance(z, balance, key):
    newroot = None
    # Left Left
    if balance < -1 and key < z.left.key:
        newroot = rotateRight(z)
    # Right Right
    elif balance > 1 and key > z.right.key:
        newroot = rotateLeft(z)
    # Left Right
    elif balance < -1 and key > z.left.key:
        z.left = rotateLeft(z.left)
        newroot = rotateRight(z)
    # Right Left
    elif balance > 1 and key < z.right.key:
        z.right = rotateRight(z.right)
        newroot = rotateLeft(z)
    return newroot


def insert(root, key):

    """
        Insert key into the AVL tree rooted at root.
        Return the root of the resulting tree.
    """

    # BST INSERT
    node = root
    if root is None:
        root = Node(key)
        return root
    else:
        while node:
            if key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = Node(key)
                    node.right.parent = node
                    node = node.right
                    break
            elif key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = Node(key)
                    node.left.parent = node
                    node = node.left
                    break

    # Update Heights of ancestors, check balance factor, determine pivot

    path = []  # consists of parent references (going up tree)

    # Update Heights of ancestors
    while node.parent:
        leftHeight = getHeight(node.parent.left)
        rightHeight = getHeight(node.parent.right)
        node.parent.height = 1 + max([leftHeight, rightHeight])
        path.append(node.parent)
        node = node.parent

    # Update Balance and determine pivot
    i = 0
    while i < len(path):
        balance = getHeight(path[i].right) - getHeight(path[i].left)  # R-heavy is 1, L-heavy is -1
        if abs(balance) > 1:  # pivot (z) found!
            z = path[i]
            root = rebalance(z, balance, key)
            break
        i += 1

    # Update Heights once more?
    i = 0
    while i < len(path):
        leftHeight = getHeight(path[i].left)
        rightHeight = getHeight(path[i].right)
        path[i].height = 1 + max([leftHeight, rightHeight])
        i += 1

    # Traverse up the tree to find real root
    while root.parent:
        root = root.parent

    return root


def delete(root, key):
    """
        Delete key from the AVL tree rooted at root.
        Return the root of the resulting tree.
    """

    # BST Search - Delete
    node = root
    while node:
        if node.key == key:
            break
        elif key < node.key:
            node = node.left
        elif key > node.key:
            node = node.right

    if node is None:
        raise Exception("Node", key, "not found!")

    if node.parent is None and node.left is None and node.right is None:  # Only node left in tree
        return None

    # 3 cases: node is leaf, node has 2 children, or node has 1 child.
    # First, determine if node is left child or right child of its parent
    leftChild = rightChild = False
    if node.parent is None:  # node is the root
        pass
    elif node.parent.left == node:
        leftChild = True
    elif node.parent.right == node:
        rightChild = True
    # 1st case: node is leaf -> just delete it
    if node.left is None and node.right is None:
        if leftChild:  # node is leftChild of its parent
            node.parent.left = None
        elif rightChild:
            node.parent.right = None
        node = node.parent
    # 2nd case: node has two children -> replace node w/ succ and delete succ
    # succ is node.right then all the way node.left
    elif node.left and node.right:
        succ = node.right
        while succ.left:
            succ = succ.left
        # Takes advantage of fact that succ cannot have a left child, otherwise recursion needed
        # to delete succ
        if succ.parent.key == node.key:
            node.right = succ.right
            if node.right:
                node.right.parent = node
        else:
            succ.parent.left = succ.right
            if succ.right is not None:
                succ.right.parent = succ.parent
        node.key = succ.key
        node = succ.parent  # testing...
    # 3rd case: node has one child, either right or left -> connect node's child and parent
    else:
        if node.parent is None:  # node has one child, no parent, so child replaces node as root
            if node.left:
                node.left.parent = None
                return node.left
            elif node.right:
                node.right.parent = None
                return node.right

        if node.left:  # node has left child
            if leftChild:  # node is left child of its parent
                node.parent.left = node.left
            elif rightChild:
                node.parent.right = node.left
            node.left.parent = node.parent
            node = node.parent  # testing...
        elif node.right:
            if leftChild:
                node.parent.left = node.right
            elif rightChild:
                node.parent.right = node.right
            node.right.parent = node.parent
            node = node.parent  # testing...
    # Traversing up from actionPos to update heights and check balances
    while node:
        leftHeight = getHeight(node.left)
        rightHeight = getHeight(node.right)
        node.height = 1 + max([leftHeight, rightHeight])
        balance = rightHeight - leftHeight  # R-heavy is 1, L-heavy is -1
        if abs(balance) > 1:  # pivot (z) found!
            z = node

            # Find y and x. If heights equal, prioritize left child
            y = x = None

            # y is taller child of z
            if getHeight(z.left) > getHeight(z.right):
                y = z.left
            elif getHeight(z.left) < getHeight(z.right):
                y = z.right
            else:
                y = z.left

            # x is taller child of y
            if getHeight(y.left) > getHeight(y.right):
                x = y.left
            elif getHeight(y.left) < getHeight(y.right):
                x = y.right
            else:
                x = y.left
            root = rebalance(z, balance, x.key)
        node = node.parent

    # Traverse up the tree to find real root
    while root.parent:
        root = root.parent

    return root


def pre_order_traversal(root, S):
    if root is None:
        return S
    S.append(root.key)
    S = pre_order_traversal(root.left, S)
    S = pre_order_traversal(root.right, S)
    return S


def deep_equals(l1, l2):
    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False
    return True


if __name__ == '__main__':
    root = None
    keys = [10, 20, 30, 9, 8, 40, 35, 36, 37]

    results = [
        [10],
        [10, 20],
        [20, 10, 30],
        [20, 10, 9, 30],
        [20, 9, 8, 10, 30],
        [20, 9, 8, 10, 30, 40],
        [20, 9, 8, 10, 35, 30, 40],
        [20, 9, 8, 10, 35, 30, 40, 36],
        [20, 9, 8, 10, 35, 30, 37, 36, 40]
    ]
    for i in range(len(keys)):
        root = insert(root, keys[i])
        rep = pre_order_traversal(root, S=[])
        if not deep_equals(rep, results[i]):
            print('expected: ' + str(rep) + ' to deeply equal: ' + str(
                results[i]))

    results = [
        [20, 9, 8, 35, 30, 37, 36, 40],
        [30, 9, 8, 36, 35, 37, 40],
        [35, 9, 8, 37, 36, 40],
        [35, 8, 37, 36, 40],
        [36, 35, 37, 40],
        [36, 35, 37],
        [36, 37],
        [37],
        []
    ]
    for i in range(len(keys)):
        root = delete(root, keys[i])
        rep = pre_order_traversal(root, S=[])
        if not deep_equals(rep, results[i]):
            print('expected: ' + str(rep) + ' to deeply equal: ' + str(
                results[i]))