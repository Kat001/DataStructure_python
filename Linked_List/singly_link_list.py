class Node():
	"""Create a node"""
	def __init__(self, data = None):
		self.data = data
		self.next_pointer = None

class Link_List:
	""" Creating List class to manage node"""
	def __init__(self):
		self. head = None


	def add_node_last(self,data):
		new_node = Node(data)
		if(self.head == None):
			self.head = new_node
			
		else:
			current_node = self.head
			while current_node.next_pointer != None:
				current_node = current_node.next_pointer
			
			current_node.next_pointer = new_node

	def delete_node_last(self):
		if(self.head == None):
			print("List is Empty")
		else:
			current_node = self.head
			while current_node.next_pointer != None:
				second_last_node = current_node
				current_node = current_node.next_pointer
			second_last_node.next_pointer = None	

	def Show_data(self):
		if self.head == None:
			print("List is empty")
		else:
			current_node = self.head
			while current_node != None:
				print(f'{current_node.data}-->', end=" ")
				current_node = current_node.next_pointer
				




if __name__ == '__main__':
	l_list = Link_List() 
	print("list created")
	l_list.add_node_last(10)
	l_list.add_node_last(20)
	l_list.add_node_last(30)
	l_list.add_node_last(40)
	l_list.add_node_last(50)
	
	print("data addded succesfulyy")

	l_list.Show_data()
	print()

	l_list.delete_node_last()
	l_list.delete_node_last()

	l_list.Show_data()
	


