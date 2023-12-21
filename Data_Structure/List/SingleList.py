class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Return boolean
    def is_empty(self):
        return self.head is None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def print(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(4)
    linked_list.append(5)
    linked_list.print()






