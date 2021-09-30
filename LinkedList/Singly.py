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
        new_tail = current
        
        while(current.next):
            # print(current.val)
            new_tail = current
            current = current.next
        
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current.val


    def shift(self):
        '''
        Description:

        Arguments:

        Return:
        
        '''

        if not self.head:
            return None

        old_head = self.head
        self.head = self.head.next
        self.length -= 1
        return old_head

            

    def unshift(self, val):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        new_head = Node(val)
        if not self.head:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head = new_head
        self.length += 1
        return self

    def get(self, i):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        if i < 0 or i > self.length:
            return None
        p = 0
        current = self.head

        while(p < i):
            current = current.next
            p += 1
        
        return current


    def set(self, i, val):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        found_node = self.get(i)
        if found_node:
            found_node.val = val
            return True
        return None

    def insert(self, index, val):
        '''
        Description:

        Arguments:

        Return:
        
        '''
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            new_node = self.unshift(val)
            return new_node == new_node
        elif index == self.length:
            new_node = self.push(val)
            return new_node == new_node
        else:
            new_node = Node(val)
            prev_node = self.get(i - 1)
            new_next = prev_node.next
            prev_node.next = new_node
            new_node.next = new_next
            return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == self.length - 1:
            return self.pop(index)
        
        if index == 0:
            return self.shift(index)
        removed = self.get(index)
        prev_node = self.get(index - 1)
        prev_node.next = removed.next
        self.length -= 1

        return removed

    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        prev = None
        next = None

        while(current.next):
            next = current.next
            current.next = prev
            prev = current
            current = next
            
        return self

singly = SinglyLinkedList()
singly.push('Hi')