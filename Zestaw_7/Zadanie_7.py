class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def dodawako(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def printowanko(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


def usun(header):
    p = header
    while p.next.next is not None:
        p = p.next
    p.next = None

lista = Node(4)
lista.dodawako(6)
lista.dodawako(7)
lista.dodawako(9)
lista.dodawako(11)
lista.dodawako(14)
lista.printowanko()
print()
usun(lista)
lista.printowanko()