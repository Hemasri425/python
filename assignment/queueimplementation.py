class Queue:

    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueueElement(self, element):
        if len(self.queue) >= self.max_size:
            print("Queue Overflow! Cannot insert element:", element)
        else:
            self.queue.append(element)
            print(f"{element} is inserted into the Queue")

    def dequeueElement(self):
        if len(self.queue) == 0:
            print("Queue Underflow! Queue is empty, cannot remove.")
        else:
            removed = self.queue.pop(0)
            print(f"{removed} is removed from the Queue")

    def peekElement(self):
        if len(self.queue) == 0:
            print("Queue is empty, nothing to peek.")
        else:
            print("Front Element of the Queue is:", self.queue[0])

    def isEmpty(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
            return True
        else:
            print("Queue is not Empty")
            return False

    def isFull(self):
        if len(self.queue) == self.max_size:
            print("Queue is Full")
            return True
        else:
            print("Queue is not Full")
            return False

    def displayQueue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            print("Current Queue Elements:", self.queue)


if __name__ == "__main__":

    print("----- Queue Data Structure Implementation -----\n")

    queue_obj = Queue(5)

    queue_obj.enqueueElement(10)
    queue_obj.enqueueElement(20)
    queue_obj.enqueueElement(30)

    queue_obj.displayQueue()

    queue_obj.peekElement()

    queue_obj.dequeueElement()

    queue_obj.isEmpty()
    queue_obj.isFull()

    queue_obj.displayQueue()
