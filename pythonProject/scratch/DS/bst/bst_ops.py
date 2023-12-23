from users import *
from tree_ops import TreeNode


class BSTNode():
    def __init__(self, key, value=0):
        self.key = key
        self.value = value
        self.left = self.right = self.parent = None

    def insert(self, key, value):
        if self is None:
            self = BSTNode(key, value)
        elif key < self.key:
            self.left = BSTNode.insert(self.left, key, value)
            self.left.parent = self
        elif key > self.key:
            self.right = BSTNode.insert(self.right, key, value)
            self.right.parent = self
        return self

    def find_value(self, key):
        if self.key is None:
            return None
        if key == self.key:
            print(f"User {self.key} is present with value\n{self.value}")
            return self.key
        if key < self.key:
            BSTNode.find_value(self.left, key)
        if key > self.key:
            BSTNode.find_value(self.right, key)

    def update(self, key, value):
        target = BSTNode.find_value(self, key)
        if target is not None:
            target.value = value

    def list_all(self):
        if self is None:
            return []
        return BSTNode.list_all(self.left) + [self.key, self.value] + BSTNode.list_all(self.right)

    def is_balanced(self):
        if self is None:
            return True, 0
        balanced_l, height_l = BSTNode.is_balanced(self.left)
        balanced_r, height_r = BSTNode.is_balanced(self.right)
        balanced = balanced_r and balanced_l and abs(balanced_r - balanced_l) <= 1
        height = 1 + max(height_r, height_l)
        return balanced, height

    def create_balanced_tree(self, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(self) - 1
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        key, value = self[mid]
        root = BSTNode(key, value)
        root.parent = parent
        root.left = BSTNode.create_balanced_tree(self, lo, mid-1, root)
        root.right = BSTNode.create_balanced_tree(self, mid+1, hi, root)
        return root

    def balance_bst(self):
        return BSTNode.create_balanced_tree(print(BSTNode.list_all(self)))


tree = BSTNode(jas.username, jas)
tree.left = BSTNode(biraj.username, biraj)
tree.right = BSTNode(sonaksh.username, sonaksh)
TreeNode.display_keys(tree)

tree1 = BSTNode.insert(None, jas.username, jas)
BSTNode.insert(tree1, biraj.username, biraj)
BSTNode.insert(tree1, sonaksh.username, sonaksh)
BSTNode.insert(tree1, aakash.username, aakash)
BSTNode.insert(tree1, hemanth.username, hemanth)
BSTNode.insert(tree1, siddhant.username, siddhant)
BSTNode.insert(tree1, vishal.username, siddhant)
TreeNode.display_keys(tree1)

# Ques 14 : Check if tree is balanced
print(f"\nIs this tree balanced? Whats the height?\n {BSTNode.is_balanced(tree1)}")

data = [(user.username, user) for user in users]

print(f"\n\nUser Data:\n{data}")
print(len(data))

"""
print("\nDisplay Tree:\n=========================")
TreeNode.display_keys(tree1)
print("=========================")
print(f"\nHeight of the tree: {TreeNode.tree_height(tree1)}\n")

# Ques 11: Insert & Find key n its value
BSTNode.find_value(tree1, 'jasjesin')

# Ques 12 is to find & update value, completed, not invoking at the moment

# Ques 13: List all content
print(f"\nList all user details:\n{BSTNode.list_all(tree1)}")

# Ques 14 : Check if tree is balanced
print(f"\nIs this tree balanced? Whats the height?\n {BSTNode.is_balanced(tree1)}")
"""
data = [(user.username, user) for user in users]
"""
print(f"\n\nUser Data:\n{data}")
print(len(data))

# skewed / unbalanced tree from sorted list
tree2 = None
for username, user in data:
    tree2 = BSTNode.insert(tree2, username, user)

print("\nDisplay Tree2:\n=========================")
TreeNode.display_keys(tree2)
print("=========================")

# Ques 15 : Create balanced tree, from sorted list
tree3 = BSTNode.create_balanced_tree(data)

print("\nDisplay Tree3:\n=========================")
TreeNode.display_keys(tree3)
print("=========================")

# Ques 16 : Balance an unbalanced tree
"""
"""
tree4 = BSTNode.balance_bst(tree2)
print("\nDisplay Tree4 :\n=========================")
TreeNode.display_keys(tree2)
print("=========================")
"""