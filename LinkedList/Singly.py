class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, val):
        '''
        Description:
            Appends a user specified value to the end of the linked list.
            Increases length.

        Arguments:
            val: user specified value

        Return:
            linked list object
        '''
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return self




        pass

    def pop(self):
        '''
        Description:

        Arguments:

        Return:

        '''
        
        pass

    def shift(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

    def unshift(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

    def get(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

    def set(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

    def insert(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

    def unshift(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        pass

singly = SinglyLinkedList()
singly.push('Hi')