class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def search(self, key):
        print(f"\nat {self.data}..")
        if key < self.data:
            if self.left is None:
                return str(key) + " not found"
            return self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return str(key) + " not found"
            return self.right.search(key)
        else:
            print("\n" + str(self.data) + " is found")

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_print()

    def preorder_print(self):
        print(self.data, end=' ')
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()

    def postorder_print(self):
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print(self.data, end=' ')

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_print()

"""
    def make_list(self):
        if self is None:
            return
        else:
            d[self.data] = []
            self.left.make_list()
            if self.left:
                d[self.data].append(self.left.data)
            elif self.right:
                d[self.data].append(self.right.data)
            self.right.make_list()
        return d
"""

if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print("In-order Traversal : ")
    root.inorder_print()
    print("\n\nPre-order Traversal : ")
    root.preorder_print()
    print("\n\nPost-order Traversal : ")
    root.postorder_print()
    print(root.search(20))

"""
    d = {}
    aList = root.make_list()
    print("\n\nAdjacency List:")
    for i in aList:
        print(f"{i}:{d['i']}")
"""