from users import *
from tree_ops import TreeNode
from bst_ops import *


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = BSTNode.find_value(self.root, key)
        if not node:
            self.root = BSTNode.insert(self.root, key, value)
            self.root = BSTNode.balance_bst(self.root)
        else:
            BSTNode.update(self.root, key, value)

    def __getitem__(self, key):
        node = BSTNode.find_value(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in BSTNode.list_all(self.root))

    def __len__(self):
        return TreeNode.tree_height(self.root)

    def display(self):
        return TreeNode.display_keys(self.root)

"""
print(users)
treemap = TreeMap()
treemap.display()
treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh
treemap.display()
treemap['jadhesh']
len(treemap)
treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal
treemap.display()
for key, value in treemap:
    print(key, value)
list(treemap)
treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
treemap['aakash']
"""


