class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1

        node = self.head
        for _ in range(index):
            node = node.next

        return node.val

    def getNode(self, index: int) -> ListNode:
        if index >= self.length:
            return None

        node = self.head
        for _ in range(index):
            node = node.next

        return node

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)

        if self.length == 0:
            self.head = newNode
            self.length += 1
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        if self.length == 0:
            self.head = newNode
            self.length += 1
            return

        lastNode = self.getNode(self.length-1)

        if lastNode:
            newNode.prev = lastNode
            lastNode.next = newNode
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == self.length:
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return

        newNode = ListNode(val)
        
        node = self.getNode(index-1)

        node.next.prev = newNode
        newNode.next = node.next

        newNode.prev = node
        node.next = newNode

        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        node = self.getNode(index)
        
        if node is None:
            return

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev

        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)