class Queue:
    def __init__(self, size):
        self.items = [None] * size
        self.head = 0
        self.tail = 0
        self.length = size

    def enqueue(self, x):
        if (self.tail + 1) % self.length == self.head:
            print("Queue overflow")
            return
        self.items[self.tail] = x
        self.tail = (self.tail + 1) % self.length
        print("Queue:", self.get_queue_list())

    def dequeue(self):
        if self.head == self.tail:
            print("Queue underflow")
            return None
        x = self.items[self.head]
        self.head = (self.head + 1) % self.length
        print("Queue:", self.get_queue_list())
        return x

    def get_queue_list(self):
        queue_list = ['_'] * self.length
        if self.tail >= self.head:
            queue_list[self.head:self.tail] = self.items[self.head:self.tail]
        else:
            queue_list[self.head:] = self.items[self.head:]
            queue_list[:self.tail] = self.items[:self.tail]
        return queue_list


# Example usage
size = int(input("Enter the size of the queue: "))
queue = Queue(size)

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter the element to enqueue: "))
        queue.enqueue(item)
    elif choice == 2:
        item = queue.dequeue()
        if item is not None:
            print("Dequeued item:", item)
    elif choice == 3:
        print("Final queue list:", queue.get_queue_list())
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
