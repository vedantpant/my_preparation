class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "stack is empty"


stack = StackArray()
stack.push(1)
stack.push(10)
print(stack.peek())
print(stack.is_empty())
print(stack.pop())