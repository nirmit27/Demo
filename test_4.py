"""
Linked List
"""


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __str__(self):
        return f"Node<value={self.value}>"


class LL:
    def __init__(self, val):
        self.head = Node(val)

    def ins(self, val):
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = Node(val)  # type: ignore

    def fwd(self):
        if not self.head:
            print("<Empty List>")
            return

        temp = self.head
        while temp:
            print(f"{temp.value} -> ", end="")
            temp = temp.next

        print("NULL")

    def rev(self):
        curr, prev, next = self.head, None, None

        while curr:
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev


if __name__ == "__main__":
    ll = LL(1)

    for i in range(2, 6):
        ll.ins(i)

    ll.fwd()
    ll.rev()
    ll.fwd()
