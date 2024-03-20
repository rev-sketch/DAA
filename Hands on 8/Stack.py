class Stack:
    def __init__(self, size):
        self.items = [None] * size
        self.top = 0
        self.size = size

    def stack_empty(self):
        return self.top == 0

    def push(self, x):
        if self.top == self.size:
            print("Stack overflow")
            return
        self.items[self.top] = x
        self.top += 1
        print("Stack:", self.get_stack_list())

    def pop(self):
        if self.stack_empty():
            print("Stack underflow")
            return None
        self.top -= 1
        print("Stack:", self.get_stack_list())
        return self.items[self.top]

    def get_stack_list(self):
        stack_list = ['_'] * self.size
        stack_list[:self.top] = self.items[:self.top]
        return stack_list


# Example usage
size = int(input("Enter the size of the stack: "))
stack = Stack(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to push: "))
        stack.push(item)
    elif choice == 2:
        item = stack.pop()
        if item is not None:
            print("Popped item:", item)
    elif choice == 3:
         print("Final stack list:", stack.get_stack_list())
         break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
