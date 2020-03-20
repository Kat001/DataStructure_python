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
	
	while True:
		print("1.add node at last")
		print("2.delete node at last")
		print("3.seach node in the list")
		print("4.Show all data")
		print("--------------------")
		ch = int(input("Enter your choice:"))
		print("----------------------")

		if ch==1:
			data = input("Enter the data:")
			l_list.add_node_last(data)
		elif ch==2:
			l_list.delete_node_last()
		elif ch==3:
			data = input("Enter data to Search")
			l_list.serach_node(data)
		elif ch==4:
			l_list.Show_data()
		else:
			print("Wrong input")

