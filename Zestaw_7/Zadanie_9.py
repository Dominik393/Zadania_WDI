class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def dodawanko(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def printowanko(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


def inkrementuj(header):
    p = header
    while p.next is not None:
        p = p.next
    p.val += 1

lista = Node(1)
lista.dodawanko(2)
lista.dodawanko(9)
lista.dodawanko(4)
inkrementuj(lista)
lista.printowanko()