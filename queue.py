class Queue:
    """
    A simple implementation of the queue abstract data type
    :author: maxwell aladago 
    """

    def __init__(self):
        self._items = []

    def enqueue(self, data):
        """
        Add an item to the queu
        :param data: The data of the item
        :return:
        """
        self._items.append(data)

    def dequeue(self):
        """
        Remove the earliest added item in the queue
        :return: The removed item
        """
        if self.isEmpty():
            return
        return self._items.pop(0)

    def dequeue2(self):
        """
        Another implementation of the dequeue method
        :return:
        """
        if self.isEmpty():
            return

        x = self._items[0]
        self._items = self._items[1:]
        return x

    def top(self):
        """
        :return: The earliest added item in the queue
        """
        if self.isEmpty():
            return
        return self._items[0]

    def getSize(self):
        return len(self._items)

    def isEmpty(self):
        return len(self._items) == 0



if __name__ == "__main__":

    q = Queue()

    print("Adding 'Maxwell and Aladago........\n")
    q.enqueue("Maxwell")
    q.enqueue("Aladago")


    print("Removing the first added item....: ", q.dequeue())
    q.enqueue("Sara")
    q.enqueue("Solomon")
    print("Printing the item which has been in wait longest.....: ", q.top())
    print("The number of items currently in the queue are ", q.getSize())

