from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value=None, left_child = None, right_child = None):
        self.value: Any = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self)->str:
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.left_child == None and self.right_child == None:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        newChild = BinaryNode(value)
        self.left_child=newChild

    def add_right_child(self, value: Any) -> None:
        newChild = BinaryNode(value)
        self.right_child=newChild

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if (self.left_child != None):
            self.left_child.traverse_in_order(visit)
        visit(self)
        if(self.right_child != None):
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if (self.left_child != None):
            self.left_child.traverse_post_order(visit)
        if(self.right_child != None):
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if (self.left_child != None):
            self.left_child.traverse_pre_order(visit)
        if(self.right_child != None):
            self.right_child.traverse_pre_order(visit)




class BinaryTree:
    root: BinaryNode

    def __init__(self, root = None):
        self.root: BinaryNode = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def printTree(node:BinaryNode, level=0):
    if node != None:
        printTree(node.left_child, level + 1)
        print(' ' * 2 * level + '->', node.value)
        printTree(node.right_child, level + 1)

n1 = BinaryNode(1)
n2 = BinaryNode(3)
n3 = BinaryNode(9,n1,n2)
n4 = BinaryNode(4)
n5 = BinaryNode(6)
n6 = BinaryNode(2,n4,n5)
n7 = BinaryNode(10,n3,n6)

tree = BinaryTree(n7)

printTree(n7)