class StackListImplementation:
    """
    This class is a basic implementation of the operations supported by
    The stack abstract data type. Items are removed in reverse to the order in which
    they were inserted
    """
    def __init__(self):
        self._items = []

    def pop(self):
        """
        Remove and the latest inserted itemin the stack
        :return: The removed item
        """
        if self.isEmpty():
            return
        return self._items.pop(len(self._items) -1)

    def top(self):
        """
        :return: Th last inserted item in the stack
        """
        if self.isEmpty():
            return
        return self._items[len(self._items) -1]

    def push(self, data):
        """
        Add a new item to the stack
        :param data: The item to add to the stack
        :return:
        """
        self._items.append(data)

    def getSize(self):
        return len(self._items)

    def isEmpty(self):
        return len(self._items) == 0


## Linked List Implementation
class StackLinkedListImplementation:
    """
    Implementation of a stack using a singly linked list
    :author: Maxwell Aladago
    """
    def __init__(self):
        self._head = None
        self._size = 0

    class _Node:
        """
        An inner class modeling the node property of a node in the stack
        """
        def __init__(self, data):
            self._data = data
            self._next = None

    def push(self, data):
        """
        Add a new item to the stack
        :param data: the value of the item
        :return: None
        """
        if not self._head:
            self._head = self._Node(data)
        else:
            new_node = self._Node(data)
            new_node._next = self._head
            self._head = new_node
        self._size += 1

    def pop(self):
        """
        remove the last added item
        :return: the removed item
        """
        if not self._head:
            return

        pop_node = self._head
        self._head = self._head._next
        self._size -= 1
        return  pop_node._data

    def top(self):
        """
        :return: The last added item
        """
        return self._head

    def isEmpty(self):
        return self._head == None

    def size(self):
        return self._size


if __name__ == "__main__":

    print("Testing stack methods in the list implementation")
    list_stack = StackListImplementation()

    print("\nAdding items in the order 10, 12, 8, 18, 2")
    list_stack.push(10)
    list_stack.push(12)
    list_stack.push( 8)
    list_stack.push(18)
    list_stack.push(2)
    print("Done adding !!!")
    print("\nRemoving items....: should be in the order 2, 18, 8, 12, 10")
    while not list_stack.isEmpty():
        print(list_stack.pop())


    print("\nTesting stack methods in the singly linked list implementation")
    list_stack = StackLinkedListImplementation()
    print("\nAdding items in the order 10, 12, 8, 18, 2")
    list_stack.push(10)
    list_stack.push(12)
    list_stack.push(8)
    list_stack.push(18)
    list_stack.push(2)
    print("Done adding !!!")

    print("\nRemoving items....: should be in the order 2, 18, 8, 12, 10")
    while not list_stack.isEmpty():
        print(list_stack.pop())

