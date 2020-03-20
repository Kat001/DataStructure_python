# Create a node class having two fields.......
class Node():
	"""Create a node"""
	def __init__(self, data = None):
		self.data = data
		self.next_pointer = None


# LinkList class to create a list
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

	# Search a specific node......
	def serach_node(self,d):
		n=0
		k=0
		if(self.head == None):
			print("List is Empty")
		else:
			current_node = self.head
			while current_node != None:
				n = n+1
				if(current_node.data == d):
					k = 1
					break
				else:
					k = 0
					current_node = current_node.next_pointer
		if k==1:
			print(f'present at index={n-1}')
		else:
			print("Not in list")



	# A Method to delete a node........ 
	def delete_node_last(self):
		if(self.head == None):
			print("List is Empty")
		else:
			current_node = self.head
			while current_node.next_pointer != None:
				second_last_node = current_node
				current_node = current_node.next_pointer
			if current_node.next_pointer == None:
				self.head = None
			else:
				second_last_node.next_pointer = None	

	# A method to diaplay the whole list
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
	
	while True:
		print("1.add node at last")
		print("2.delete node at last")
		print("3.seach node in the list")
		print("4.Show all data")
		print("--------------------")
		ch = int(input("Enter your choice:"))
		print("----------------------")

		if ch==1:
			print("------------------------")
			data = input("Enter the data:")
			l_list.add_node_last(data)
			print("--------------------")
			print("Node added Successfully")
			print("-----------------------")
			print()
		
		elif ch==2:
			print("-------------------")
			l_list.delete_node_last()
			print("Last node deleted Successfully")
			print("--------------------------------")
			print()

		elif ch==3:
			print("---------------------------")
			data = input("Enter data to Search")
			l_list.serach_node(data)
			print("-----------------------------")
			print()

		elif ch==4:
			print("------------------")
			l_list.Show_data()
			print()
			print("-------------------")
			print()

		else:
			print("--------------")
			print("Wrong input")
			print("-----------------")
			print()

