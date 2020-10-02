class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        #Move to the tail (the last Node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value) 
        return 

    def to_list(self):
        out_list = []

        if self.head is None:
            return
        
        node = self.head 
        while node:
            out_list.append(node.value)
            node = node.next 
        
        return out_list

    def prepend(self, value):
        '''Prepend a value to the beginning of the list''' 
        if self.head is None:
            self.head = Node(value)
            return
        
        new_head = Node(value)
        new_head.next = self.head 
        self.head = new_head 
    
    def search(self, value):
        ''' Search the linked list for a node with the request value and return the node'''
        if self.head is None:
            return None
         
        node = self.head 
        while node:
            if node.value == value:
                return node 
            node = node.next 
        raise ValueError("Value not found in the list") 
    
    def remove(self, value):
        '''Remove first occurrence of value'''
        if self.head is None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
        
        node = self.head 

        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return 
            node = node.next 
        
        raise ValueError("Value is not found in the list") 

    def insert(self, value, pos):
        if self.head is None:
            return None 
        
        if pos == 0:
            self.prepend(value)
            return
        
        index = 0
        node = self.head 
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node 
                return 
            index += 1
            node = node.next
        else: 
            self.append(value)
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value = node.next
    
    def __repr__(self):
        return str([v for v in self]) 
    
    def reverse(linked_list):
        '''
        Reverse Linked List
        Args: linked_list(obj): Linked List to be reversed
        Returns:
            obj: Reversed LL
        '''
        new_list = LinkedList()
        prev_node = None

        for value in linked_list:
            new_node = Node(value)
            new_node.next = prev_node.next
            prev_node = new_node
        new_list.head = prev_node 
        return new_list 
    
    def isCircular(linked_list):
        if linked_list.head is None:
            return None 
        
        slow = linked_list.head 
        fast = linked_list.head 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
            if slow == fast:
                return True 
        return False 
    
    def merge(list1, list2):
        merged = LinkedList(None)
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        list1_elt = list1.head
        list2_elt = list2.head
        while list1_elt is not None or list2_elt is not None:
            if list1_elt is None:
                merged.append(list2_elt)
                list2_elt = list2_elt.next 
            elif list2_elt is None:
                merged.append(list1_elt)
                list1_elt = list1_elt.next
            elif list1_elt.value <= list2_elt.value:
                merged.append(list1_elt)
                list1_elt = list1_elt.next 
            else:
                merged.append(list2_elt)
                lsit_2_elt = list2_elt.next 
        return merged

'''In a NESTED LinkedList object, each node will be simple LinkedList in itself'''
class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)
    
    '''Recursive function'''
    def _flatten(self, node):
        # A termination condition
        if node.next is None:
            return merge(node.value, None)
        # _flatten() is calling itself until a termination condition is met
        return merge(node.value, self._flatten(node.next))



class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head 
            return
        
        self.tail.next = DoubleNode(value)
        self.tail.next.previous = self.tail 
        self.tail = self.tail.next 
        return  

     




linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next 

