class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def list_empty(self):
        return self.head is None

    def list_insert(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        self.print_list()

    def list_delete(self):
        if self.list_empty():
            print("List underflow")
            return None
        x = self.head.data
        self.head = self.head.next
        self.print_list()
        return x

    def print_list(self):
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
linked_list = SinglyLinkedList()

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to insert: "))
        linked_list.list_insert(item)
    elif choice == 2:
        item = linked_list.list_delete()
        if item is not None:
            print("Deleted item:", item)
    elif choice == 3:
        print("Final stack list:", stack.get_stack_list())
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
