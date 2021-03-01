# Python program to demonstrate delete operation
# in binary search tree

# A Binary Tree Node

import time
import random
start=time.time()
end=time.time()
print("time (sec): ",end-start)

class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# A utility function to do inorder traversal of BST
def inorder(root):
	if root is not None:
		inorder(root.left)
		print(root.key)
		inorder(root.right)


# A utility function to insert a
# new node with given key in BST
def insert(node, key):

	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# return the (unchanged) node pointer
	return node

# Given a non-empty binary 
# search tree, return the node
# with minum key value 
# found in that tree. Note that the
# entire tree does not need to be searched


def minValueNode(node):
	current = node

	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left

	return current

# Given a binary search tree and a key, this function
# delete the key and returns the new root


def deleteNode(root, key):

	# Base Case
	if root is None:
		return root

	# If the key to be deleted 
	# is smaller than the root's
	# key then it lies in left subtree
	if key < root.key:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete 
	# is greater than the root's key
	# then it lies in right subtree
	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# If key is same as root's key, then this is the node
	# to be deleted
	else:

		# Node with only one child or no child
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Node with two children: 
		# Get the inorder successor
		# (smallest in the right subtree)
		temp = minValueNode(root.right)

		# Copy the inorder successor's 
		# content to this node
		root.key = temp.key

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.key)

	return root

def findval(root, lkpval):
    if lkpval < root.key:
        if root.left is None:
            return str(lkpval)+" Not Found"
        return findval(root.left, lkpval)
    elif lkpval > root.key:
        if root.right is None:
            return str(lkpval)+" Not Found"
        return findval(root.right, lkpval)
    else:
        return str(root.key) + ' is found'
        
# Print the tree
def PrintTree(root):
    print("print tree")
    if root.left:
        PrintTree(root.left)
    print( root.key)
    if root.right:
        PrintTree(root.right)

# Driver code
""" Let us create following BST
			50
		/	 \
		30	 70
		/ \ / \
	20 40 60 80 """


def display(root):
        lines, *_ = display_aux(root)
        for line in lines:
            print(line)

def display_aux(root):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if root.right is None and root.left is None:
        line = '%s' % root.key
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if root.right is None:
        lines, n, p, x = display_aux(root.left)
        s = '%s' % root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if root.left is None:
        lines, n, p, x = display_aux(root.right)
        s = '%s' % root.key
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = display_aux(root.left)
    right, m, q, y = display_aux(root.right)
    s = '%s' % root.key
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2




def main():
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    
    print(findval(root, 80))
    print(findval(root, 10))
    
    print("Inorder traversal of the given tree")
    inorder(root)
    # PrintTree(root)
    
    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    display(root)
    # This code is contributed by Nikhil Kumar Singh(nickzuck_007)
    
    
    # create a list of 10000 numbers
    lst = [random.randint(1,1000000) for i in range(1000000)]
    # each number is a random number between 1 and 10000 random.randint(1,10000)
    
    # in other loop for in 1 to 10000, check to see if i is in the list
    start1 = time.time()
    for i in range(1,1000001):
        for l in lst:
            if i == l:
                break
    end1 = time.time()
    print("time (sec): ", end1-start1)
    
    
    
    root = None
    for i in range(1000000):
        root = insert(root, random.randint(1,100000))
        
    start = time.time()
    for i in range(1000000):
        findval(root, i)
    end = time.time()
    
    print("time (sec): ",end-start)
    
    
   
            
        
    
    
main()