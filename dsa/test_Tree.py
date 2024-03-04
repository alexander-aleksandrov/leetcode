from Tree import Node, Tree

def test_treeSum():
    # Create a tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, Node(6, None, None), Node(7, None, None)))
    tree = Tree(root)
    assert tree.treeSum(root) == 28

def test_treeMax():
    # Create a tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, Node(6, None, None), Node(7, None, None)))
    tree = Tree(root)
    assert tree.treeMax(root) == 7

def test_treeHeight():
    # Create a tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    #  / \
    # 8   9
    root = Node(1, Node(2, Node(4, Node(8, None, None), Node(9, None, None)), Node(5, None, None)), Node(3, Node(6, None, None), Node(7, None, None)))
    tree = Tree(root)
    assert tree.treeHeight(root) == 4

def test_exists():
    # Create a tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    root = Node(1, Node(2, Node(4, None, None), Node(5, None, None)), Node(3, Node(6, None, None), Node(7, None, None)))
    tree = Tree(root)
    assert tree.exists(root, 5) == True
    assert tree.exists(root, 8) == False
    
    

    