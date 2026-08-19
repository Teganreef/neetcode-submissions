class ListNode:
    def __init__(self,val):
        self.val = val  
        self.next = None

class LinkedList:
    def __init__(self):
        dummy_node = ListNode(-1)
        self.head = dummy_node
        self.tail = dummy_node 

    

    def get(self, index: int) -> int:
        curr = self.head.next 
        for i in range(index):
            curr = curr.next 
            if curr is None:
                return -1

        if curr:
            return curr.val 
        else: 
            return -1 
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node
        

    def remove(self, index: int) -> bool:
        curr = self.head 

        for i in range(index):
            curr = curr.next
            if curr is None:
                return False
        
        if curr and curr.next: 
            curr.next = curr.next.next
            if curr.next is None: 
                self.tail = curr
            return True 
        return False
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next 
        while curr:
            res.append(curr.val)
            curr = curr.next 
        return res 
        
