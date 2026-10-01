class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        elements = []

        while current.next is not None:
            elements.append(current.data)
            current = current.next
        current.next = new_node
    

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Invalid Index")

        if index == 0:
            self.prepend(data)
            return

        current = self.head

        for _ in range(index - 1):
            if current is None:
                raise IndexError("Invalid index")
            current = current.next

        if current is None:
            raise IndexError("Invalid index")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_first(self):
        if self.head is None:
            return 

        self.head = self.head.next

    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current != None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def length(self):
        count = 0
        
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False

ll = LinkedList()
ll.append('hello')
ll.append('world')
ll.append(10)
print(ll.search(10))
ll.display()
print(f"Length: {ll.length()}")