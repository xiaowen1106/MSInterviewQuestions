#!/usr/bin/python

#Questions: Define a Stack structure. Requirement: time efficiency for push(), pop() and min() are all O(1)

class Node():
	def __init__(self,val):
		self.next = None
		self.key = val


# implement the Stack using a linked list. Maintain a stack to store all the minimum elements
class Stack():
	def __init__(self):
		self.min = []
		self.head = None

	#insert first
	def push(self,value):
		newElement = Node(value)
		if self.head == None:
			self.head = newElement
		else:
			newElement.next = self.head
			self.head = newElement

		# update min stack
		if len(self.min) == 0 or self.min[0].key > newElement.key:
			self.min.insert(0,newElement)

	#delete first
	def pop(self):
		if self.head == None:
			return None
		else:
			toReturn = self.head
			self.head = self.head.next

		if toReturn.key <= self.min[0].key:
			self.min.pop(0)
		return toReturn.key

	#get minimum element 
	def getMin(self):
		if len(self.min) == 0:
			return "empty list"
		else:
			return self.min[0].key

#Test
s = Stack()

s.push(2)
s.push(6)
s.push(4)
s.push(1)
s.push(5)

print s.getMin()

s.pop()
s.pop()

print s.getMin()