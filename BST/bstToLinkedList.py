#!/usr/bin/python

#Questions: convert a Binary Search Tree to a Double Linked List, without using extra data structure

class BSTNode:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.p = None
		self.key = val

#insert element in a BST
def tree_insert(T,z):
	y = None
	x = T
	while x != None:
		y = x
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.p = y

	if y == None:
		T = z # Tree T is empty
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z

#init linked_list and the last element of list to null
linked_list = None
last = None

#after conversion, we use node.left as the pointer to its next node, and node.p as the pointer to its parent node
def connectToList(x):
	global last;
	global linked_list;
	if last == None:
		linked_list = x
		last = x
	else:
		last.left = x
		x.p = last
		last = x

def inorder_tree_walk(x):
	if x != None:
		inorder_tree_walk(x.left)
		connectToList(x)
		inorder_tree_walk(x.right)

def printList(l):
	while l != None:
		print l.key
		l = l.left

#test
T = BSTNode(10)
tree_insert(T,BSTNode(4))
tree_insert(T,BSTNode(6))
tree_insert(T,BSTNode(8))
tree_insert(T,BSTNode(12))
tree_insert(T,BSTNode(14))
tree_insert(T,BSTNode(16))

inorder_tree_walk(T)
printList(linked_list)
