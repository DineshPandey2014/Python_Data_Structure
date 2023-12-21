# class Stack:
#     def __init(self):
#         self.stack = []
#
#     # Push the element in the end
#     def push(self, data):
#         self.stack.append(data)
#
#     # Pop the element
#     def pop(self):
#         self.stack.pop()

class stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()

if __name__ == "__main__":
    stack1 = stack()
    stack1.push(4)
    stack1.push(5)
    stack1.push(6)
    stack1.push(7)
    print(len(stack1.stack))


