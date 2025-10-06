class Stack:

    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def pushElement(self, element):
        if len(self.stack) >= self.max_size:
            print("Stack Overflow! Cannot push element:", element)
        else:
            self.stack.append(element)
            print(f"{element} is pushed onto the Stack")

    def popElement(self):
        if len(self.stack) == 0:
            print("Stack Underflow! Stack is empty, cannot pop.")
        else:
            removed = self.stack.pop()
            print(f"{removed} is popped from the Stack")

    def peekElement(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to peek.")
        else:
            print("Top Element of the Stack is:", self.stack[-1])

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
            return True
        else:
            print("Stack is not Empty")
            return False

    def isFull(self):
        if len(self.stack) == self.max_size:
            print("Stack is Full")
            return True
        else:
            print("Stack is not Full")
            return False

    def displayStack(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Current Stack Elements:", self.stack)


if __name__ == "__main__":

    print("----- Stack Data Structure Implementation -----\n")

    stack_obj = Stack(5)

    stack_obj.pushElement(10)
    stack_obj.pushElement(20)
    stack_obj.pushElement(30)

    stack_obj.displayStack()

    stack_obj.peekElement()

    stack_obj.popElement()

    stack_obj.isEmpty()
    stack_obj.isFull()

    stack_obj.displayStack()
