# Traverse the linked list
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next != None:
#             curr = curr.next
#         curr.next = new_node

#     def display(self):
#         curr = self.head

#         while curr != None:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.display()

# 2. Count the nodes
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def count(self):
#         count = 0
#         curr = self.head

#         while curr is not None:
#             count += 1
#             curr = curr.next

#         return count

#     def display(self):
#         curr = self.head

#         while curr != None:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.display()
#     print(f"Length of ll: {ll.count()}")


# 3. Search for a value
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def search(self, data):
#         curr = self.head

#         while curr:
#             if curr.data == data:
#                 return True
#             curr = curr.next
#         return False

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     print(ll.search(20))
    

# 4. Sum of all nodes
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def Sum(self):
#         Sum = 0
#         curr = self.head

#         while curr is not None:
#             Sum += curr.data
#             curr = curr.next
#         return Sum

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     print(f"Total Sum of linked list: {ll.Sum()}")


# 5. Maximum value in a linked list
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def maxVal(self):
#         if self.head is None:
#             return None
        
#         Max = self.head.data
#         curr = self.head.next

#         while curr:
#             if curr.data > Max:
#                 Max = curr.data
#             curr = curr.next

#         return Max

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(20)
#     ll.append(40)
#     print(f"Maximum value in linked list: {ll.maxVal()}")


# 6. Minimum value in a linked list
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def minVal(self):
#         if self.head is None:
#             return None
        
#         Min = self.head.data
#         curr = self.head.next

#         while curr:
#             if curr.data < Min:
#                 Min = curr.data
#             curr = curr.next

#         return Min

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(20)
#     ll.append(40)
#     print(f"Minimum value in linked list: {ll.minVal()}")


# 7. Get the value of the last node
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def lastValue(self):
#         if self.head is None:
#             return None

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         return curr.data

#     def display(self):
#         curr = self.head

#         while curr != None:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(20)
#     ll.append(40)
#     ll.display()
#     print(f"Last value in linked list: {ll.lastValue()}")


# 8. Insert a node at the beginning
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def insertAtBeginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     # 9. Delete the first node
#     def deleteFirst(self):
#         if self.head is None:
#             return 
        
#         self.head = self.head.next

#     # 10. Delete the last node
#     def deleteLast(self):
#         if self.head is None:
#             return

#         if self.head.next is None:
#             self.head = None
#             return 
        
#         curr = self.head
#         while curr is not None:
#             if curr.next.next is None:
#                 curr.next = None
#             curr = curr.next

#     # 11. Delete a node by value
#     def deleteVal(self, data):
#         if self.head is None:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return

#         curr = self.head
#         while curr.next is not None:
#             if curr.next.data == data:
#                 curr.next = curr.next.next
#                 return
#             curr = curr.next


#     def display(self):
#         curr = self.head

#         while curr != None:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(20)
#     ll.append(40)
#     ll.display()
#     ll.deleteVal(10)
#     ll.display()


# # 13. Count occurences of a value
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return 0

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def occurences(self, data):
#         if self.head is None:
#             return
        
#         count = 0
#         curr = self.head

#         while curr is not None:
#             if curr.data == data:
#                 count += 1
#             curr = curr.next
#         print(f"Total occurrences of {data}: {count}")

#     def display(self):
#         if self.head is None:
#             return

#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(10)
#     ll.append(20)
#     ll.append(40)
#     ll.append(10)
#     ll.display()
#     ll.occurences(10)


# # 14. Find the second-last node
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return 0

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def sndLast(self):
#         if self.head is None or self.head.next is None:
#             return 0

#         curr = self.head
#         while curr.next.next:
#             curr = curr.next
#         print(f"Second last node in linked list: {curr.data}")
#         return
            

#     def display(self):
#         if self.head is None:
#             return

#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(50)
#     ll.append(20)
#     ll.append(40)
#     ll.display()
#     ll.sndLast()
    

# 15. Check whether the list is sorted
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return 0

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new_node

#     def if_sorted(self):
#         if self.head is None:
#             return 0

#         prev = self.head
#         curr = self.head.next

#         while curr is not None:
#             if curr.data < prev.data:
#                 return False
#             prev = prev.next
#             curr = curr.next
#         return True

#     def display(self):
#         if self.head is None:
#             return True

#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(40)
#     ll.display()
#     print(ll.if_sorted())


# 16. Reverse a linked list
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def printReverse(self):
#         stack = []
#         curr = self.head

#         while curr:
#             stack.append(curr.data)
#             curr = curr.next

#         while stack:
#             print(stack.pop())
        

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.printReverse()


# 17. Remove Duplicates from Sorted List
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def duplicates(self):
#         if self.head is None:
#             return 0

#         prev = self.head
#         curr = self.head.next

#         while curr:
#             if prev.data == curr.data:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#             curr = curr.next
        
            
#     def display(self):
#         if self.head is None:
#             return 

#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.display()
#     ll.duplicates()
#     ll.display()


# 18. Middle of a linked list
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next= next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def middle(self):
#         if self.head is None:
#             return 0

#         fast = self.head
#         slow = self.head

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         return slow.data

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(10)
#     ll.append(20)
#     ll.append(30)
#     ll.append(40)
#     ll.append(50)
#     print(ll.middle())


# 19. Palindrome Linked List
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return

#         curr = self.head
#         while curr.next is not None:
#             curr = curr.next
#         curr.next = new_node

#     def isPalindrome(self):
#         if self.head is None:
#             return True

#         stack = []
#         curr = self.head

#         while curr is not None:
#             stack.append(curr.data)
#             curr = curr.next

#         curr = self.head
#         while curr is not None:
#             if curr.data != stack.pop():
#                 return False
#             curr = curr.next
#         return True

# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.append(2)
#     ll.append(1)
#     print(ll.isPalindrome())


