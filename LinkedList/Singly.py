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

    # def traverse(){
    #     current = self.head
    #     while(current):
    #         print(current.val)
    #         current = current.next
    # }

    def pop(self):
        '''
        Description:
            removes tail and returns the value

        Arguments:
            None
        Return:
            tail: Node object
        '''
        if not self.head:
            return None

        current = self.head
        while(current.next):
            print(current.val)
            new_tail = current
            current = current.next
        
        self.tail = new_tail.val
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current


    def shift(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        if length == 0:
            return None 

            

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