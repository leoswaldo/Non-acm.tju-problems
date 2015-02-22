#!/python3/bin/python3


## Class: Node
#  Decription: structure of nodes of binary tree
class Node():

    def __init__(self, data):
        self.data = data
        self.left_son = None
        self.right_son = None


## Function: list_tree
#  Description: list the tree from the left to right son (inorder)
#  Parameters: current_node
#      currernt_node: the scanned node
def list_tree(current_node):

    # review the left son and if it has something go in there
    if(current_node.left_son):
        list_tree(current_node.left_son)

    # print the current node
    print(current_node.data)

    # review the right son and if it has something go in there
    if(current_node.right_son):
        list_tree(current_node.right_son)


if(__name__ == "__main__"):

    # Create nodes of tree
    root = Node(10)
    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(8)
    node4 = Node(7)
    node5 = Node(9)

    # Assign nodes to tree
    root.left_son = node1
    node1.left_son = node2
    node1.right_son = node3
    node3.left_son = node4
    node3.right_son = node5

    # call function to print the tree
    list_tree(root)