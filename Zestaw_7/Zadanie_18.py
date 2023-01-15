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


def funkcja(header):
    p = header
    q = header
    while p is not None:
        while q.next is not None:
            if p.val == q.next.val:
                q.next = q.next.next
            else:
                if q.next is None:
                    break
                q = q.next
        p = p.next
        q = p
    return header

lista = Node(10)
lista.dodawanko(15)
lista.dodawanko(10)
lista.dodawanko(10)
lista.dodawanko(30)
lista.dodawanko(10)
lista.printowanko()
lista = funkcja(lista)
print()
lista.printowanko()


