class Heap:
    """
    This class is a simple implementation of a binary heap using a list
    All supported operations of the heap interface have been implemented
    :author: Maxwell Aladago
    """
    def __init__(self):
        self._items = []

    def min(self):
        """        
        :return: the data of the minimum value
        """
        return self._items[0]

    def remove_min(self):
        """   
        Removes the minimum value
        :return: the min value
        """
        ln = len(self._items)
        if ln == 0:
            return
        # the last item is removed without percolating down
        if ln == 1:
            return self._items.pop(0)
        
        x = self._items[0]
        self._items[0] = self._items.pop(len(self._items) - 1)
        self._percolate_down(0)
        return x

    def insert(self, data):
        """
        Adds a new item to the data
        :param data: the priority of the item
        :return: 
        """
        self._items.append(data)
        self._percolate_up(len(self._items) - 1)

    def _percolate_down(self, index):
        """
        Percolate moves items downwards until the heap order is maintained. 
        The heap order is said to be maintained if a node is smaller than both of it's children
        :param index: the current index of the node being percolated.
        :return: an none to break the percoalation  
        """
        ln = len(self._items)
        if ln > 0 and index >= ln:
            return
        
        curItem = self._items[index]
        leftChildIndex, rightChildIndex = (2 * index) + 1, (2 * index) + 2
        if ln > leftChildIndex and ln > rightChildIndex:
            if self._items[leftChildIndex] < self._items[rightChildIndex]:
                if curItem > self._items[leftChildIndex]:
                    self._swap(index, leftChildIndex)
                    self._percolate_down(leftChildIndex)
            elif curItem > self._items[rightChildIndex]:
                self._swap(index, rightChildIndex)
                self._percolate_down(rightChildIndex)
            else:
                return
        elif ln > leftChildIndex and curItem > self._items[leftChildIndex]:
            self._swap(index, leftChildIndex)
            self._percolate_down(leftChildIndex)
        else:
            return

    def _swap(self, index1, index2):
        """
        a utility method to swap two items in the list
        :param index1: 
        :param index2: 
        :return: 
        """
        tempt = self._items[index1]
        self._items[index1] = self._items[index2]
        self._items[index2] = tempt

    def _percolate_up(self, index):
        if len(self._items) == 0 or index == 0 or index >= len(self._items):
            return
        
        curItem = self._items[index]
        parentIndex = (index - 1) // 2
        parent = self._items[parentIndex]

        if curItem < parent:
            self._swap(index, parentIndex)
            self._percolate_up(parentIndex)
        else:
            return

    def isEmpty(self):
        """        
        :return: True if there are no items in the heap
        """
        return len(self._items) < 1

    def size(self):
        """        
        :return: The number of items in the heap
        """
        return len(self._items)


## some test methods
hex = Heap()

hex.insert(10)
hex.insert(5)
hex.insert(6)
hex.insert(7)
hex.insert(2)
hex.insert(21)
hex.insert(1)
hex.insert(16)

while not hex.isEmpty():
    print("The currentMin is: " , hex.remove_min())
