class TreeNode:  # Ques 2: Implement Binary Tree
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def tree_to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.tree_to_tuple(self.left),  self.key, TreeNode.tree_to_tuple(self.right)

    def display_keys(self, space='\t\t', level=0):
        # print (node.key if node else None, level)
        indent = space * level

        # if node is empty
        if self is None:
            print(indent + '*')
            return

        # if node is a leaf
        if self.left is None and self.right is None:
            print(indent + str(self.key))
            return

        # if node has children
        TreeNode.display_keys(self.right, space, level + 1)
        print(indent + str(self.key))
        TreeNode.display_keys(self.left, space, level + 1)

    def traversal_in_order(self):
        if self is None:
            return []
        return TreeNode.traversal_in_order(self.left) + [self.key] + TreeNode.traversal_in_order(self.right)

    def traversal_pre_order(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traversal_pre_order(self.left) + TreeNode.traversal_pre_order(self.right)

    def traversal_post_order(self):
        if self is None:
            return []
        return TreeNode.traversal_post_order(self.left) + TreeNode.traversal_post_order(self.right) + [self.key]

    def tree_height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.tree_height(self.left), TreeNode.tree_height(self.right))

    def tree_size(self):
        if self is None:
            return 0
        return 1 + TreeNode.tree_size(self.left) + TreeNode.tree_size(self.right)

    def remove_none(self):
        return [x for x in self if x is not None]

    def is_bst(self):
        if self is None:
            return True, None, None
        is_bst_l, min_l, max_l = TreeNode.is_bst(self.left)
        is_bst_r, min_r, max_r = TreeNode.is_bst(self.right)
        is_bst_node = (is_bst_l and is_bst_r and
                       (max_l is None or self.key > max_l) and
                       (min_r is None or self.key < max_r))
        min_key = min(TreeNode.remove_none([min_l, self.key, min_r]))
        max_key = max(TreeNode.remove_none([max_l, self.key, max_r]))
#        print(f"\n Is this tree a BST? : {is_bst_node}\nMinium value: {min_key}\n Maximum value {max_key}")
        return is_bst_node, min_key, max_key

    def __str__(self):
        return f"Binary Tree: <{self.tree_to_tuple()}>"

    def __repr__(self):
        return f"Binary Tree: <{self.tree_to_tuple()}>"

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = TreeNode(data)
        return node


node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
tree = node0
node0.left = node1
node0.right = node2

# print(tree.left.key, tree.key, tree.right.key)
"""
tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
tree = TreeNode.parse_tuple(tree_tuple)
print(tree)
print("============")
TreeNode.display_keys(tree, ' ')
print("============")
print(f"Tree to tuple: {TreeNode.tree_to_tuple(tree)}")
print(f"\n Tree Traversals:")
print(f"\n1. In-Order  : {TreeNode.traversal_in_order(tree)}")  # Ques 3
print(f"2. Pre-Order : {TreeNode.traversal_pre_order(tree)}")  # Ques 4
print(f"3. Post-Order: {TreeNode.traversal_post_order(tree)}")  # Ques 5
print(f"\n Tree Height : {TreeNode.tree_height(tree)}")  # Ques 6
print(f"no. of nodes : {TreeNode.tree_size(tree)}")  # Ques 7
print(f"\nValidate if given tree is BST: {TreeNode.is_bst(tree)}\n\n")

tree2 = TreeNode.parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))
print(tree2)
print("============")
TreeNode.display_keys(tree2, ' ')
print("============")
print(f"Tree to tuple: {TreeNode.tree_to_tuple(tree2)}")
print(f"\n Tree Traversals:")
print(f"\n1. In-Order  : {TreeNode.traversal_in_order(tree2)}")  # Ques 3
print(f"2. Pre-Order : {TreeNode.traversal_pre_order(tree2)}")   # Ques 4
print(f"3. Post-Order: {TreeNode.traversal_post_order(tree2)}")  # Ques 5
print(f"\n Tree Height : {TreeNode.tree_height(tree2)}")         # Ques 6
print(f"no. of nodes : {TreeNode.tree_size(tree2)}")             # Ques 7
# Ques 8, 9, 10 -- Is given tree a BST, find min and max value
print(f"\nValidate if given tree is BST: {TreeNode.is_bst(tree2)}")
"""
"""
print(f"L1: {tree2.key}")
print(f"L2: {tree2.left.key} {tree2.right.key}")
print(f"L3: {tree2.left.left.key} {tree2.left.right.key} {tree2.right.left.key} {tree2.right.right.key}")
print(f"L4: {tree2.left.left.left.key} {tree2.left.left.right.key} 
{tree2.left.right.left.key} {tree2.left.right.right.key} 
{tree2.right.left.left.key} {tree2.right.left.right.key} 
{tree2.right.right.left.key} {tree2.right.right.right.key}")
"""
