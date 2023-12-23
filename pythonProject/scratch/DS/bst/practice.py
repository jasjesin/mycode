class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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
        if key < self.data:
            if self.left is None:
                return F"{str(key)} not found"
            else:
                self.left.search(key)
        elif key > self.data:
            if self.right is None:
                return F"{str(key)} not found"
            else:
                self.right.search(key)
        else:
            return f"{str(self.data)} is found"

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.data, end=' ')
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        print(self.data, end=' ')


if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)

    print("In-order Traversal : ")
    root.inorder_traversal()
    print("\n\nPre-order Traversal : ")
    root.preorder_traversal()
    print("\n\nPost-order Traversal : ")
    root.postorder_traversal()
    print(root.search(42))
