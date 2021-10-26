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
            print("Invalid index")
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
        newN = Node(val, next=None)
        for _ in range(index):

    def deleteAtIndex(self, index: int) -> None:
        pass


if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtHead(4)
    print(ll.get(0))
    print(ll.get(1))
