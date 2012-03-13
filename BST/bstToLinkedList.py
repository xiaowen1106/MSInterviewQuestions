#!/usr/bin/python

#Questions: convert a Binary Search Tree to a Double Linked List, without using extra data structure

class BSTNode:
	def __init__(self,val):
		self.left = None
		self.right = None
		self.p = None
		self.key = val


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


linked_list = None
last = None

def convertToList(x):
	global last;
	global linked_list;
	if x!=None:
		convertToList(x.left)
		if last == None:
			linked_list = x
			last = x
		else:
			last.left = x
			x.p = last
			last = x
		print last.key
		convertToList(x.right)

def printList(l):
	while l != None:
		print l.key
		l = l.left


T = BSTNode(10)
tree_insert(T,BSTNode(4))
tree_insert(T,BSTNode(6))
tree_insert(T,BSTNode(8))
tree_insert(T,BSTNode(12))
tree_insert(T,BSTNode(14))
tree_insert(T,BSTNode(16))

convertToList(T)
printList(linked_list)
