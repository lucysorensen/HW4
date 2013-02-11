"""
Homework 4
Lucy Sorensen
February 12, 2013
"""

class LinkedList(object):
  
	def __init__(self, value):
		self.nullnode = Node(None)
		self.nullnode.next = self.nullnode
		self.head = Node(value, self.nullnode)
		self.nullnode.prev = self.head
		self.tail = self.head
		self.length = 1
	
	def length(self):
		return self.length
	
	def addNode(self, new_value):
		new_node = Node(new_value, self.nullnode)
		new_node.prev = self.tail
		if self.head == None:
			self.head = new_node
		if self.tail != None:
			self.tail.next = new_node
		self.tail = new_node
		self.length += 1
				
#I am assuming that the "after_node" is an index of the node which you add after	
	def addNodeAfter(self, new_value, after_node):		
		insert_node = Node(new_value)
		if after_node == self.length-1:
			addNode(new_value)
		else:
			i = 0
			active_node = self.head
			while i < after_node:
				active_node = active_node.next
				i += 1
			insert_node.prev = active_node
			insert_node.next = active_node.next
			active_node.next.prev = insert_node
			active_node.next = insert_node
			self.length += 1
		
	def addNodeBefore(self, new_value, before_node):
		insert_node = Node(new_value)
		if before_node == 0:
			rejected = self.head
			rejected.next = self.head.next
			insert_node.next = rejected
			rejected.prev = insert_node
			self.head = insert_node	
		else:
			i = 0
			active_node = self.head
			while i < before_node:
				active_node = active_node.next
				i += 1
			insert_node.next = active_node
			insert_node.prev = active_node.prev
			active_node.prev.next = insert_node
			active_node.prev = insert_node
			self.length += 1
	
	def removeNode(self, node_to_remove):
		if node_to_remove == 0:
			self.head = self.head.next
			self.head.prev = None
		elif node_to_remove == self.length - 1:
			self.tail = self.tail.prev
			self.tail.next = self.nullnode
		else:
			i = 0
			active_node = self.head
			while i < node_to_remove:
				active_node = active_node.next
				i += 1
			active_node.prev.next = active_node.next
			active_node.next.prev = active_node.prev
			active_node.next = None
			active_node.prev = None
			active_node.value = None
		self.length -= 1
		
	def removeNodesbyValue(self, value):
		i = 0
		active_node = self.head
		while i < self.length:
			if active_node.value == value:
				active_node = active_node.next
				self.removeNode(int(i))				
				i += 1
			else:
				active_node = active_node.next
				i += 1
	
	def reverse(self):
		previous = self.nullnode
		current = self.head
		next = self.head.next
		while next.value != None:
			current.next = previous
			current.prev = next
			previous = current
			current = next
			next = next.next
		self.head = current
		self.head.next = previous
		
	def __str__(self):
		return str(self.Print())
			
	def Print(self):
		active_node = self.head
		while active_node.value != None:
			print str(active_node.value)
			active_node = active_node.next
					
class Node(object):
	
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next
		self.prev = None
	
	def __str__(self):
		return str(self.value)
