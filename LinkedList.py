class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        iter = self.head
        if index < 0 or index > self.size-1:
            # print("Invalid index")
            return
        if index == 0:
            return iter.val
        count = 0
        while iter.next != None:
            if count == index:
                break
            print
            iter = iter.next
            count += 1
        # print(iter.val,"->")
        return iter.val

    def addAtHead(self, val: int) -> None:
        newN = Node(val, next=self.head)
        self.head = newN
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newN = Node(val, next=None)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = newN
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # newN = Node(val, next=None)
        if index < 0:
            index = 0
        if index > self.size:
            return
        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        self.size += 1
        newN = Node(val, next=curr.next)
        curr.next = newN

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        self.size -= 1
        for _ in range(index-1):
            curr = curr.next
        curr.next = curr.next.next


if __name__ == "__main__":
    ll = MyLinkedList()
    # ll.addAtHead(6)
    # ll.addAtHead(8)
    ll.addAtHead(12)
    # ll.addAtIndex(1, 10)
    # ll.addAtIndex(1, 11)
    ll.deleteAtIndex(1)
    print(ll.get(0))
    print(ll.get(1))
    # print(ll.get(2))
    # print(ll.get(3))
