class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0