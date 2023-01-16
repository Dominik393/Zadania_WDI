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


def f(header1, header2):
    p = header1
    tmpp = header1
    q = header2
    #   Czy q jest w p
    while p is not None:
        while q is not None:
            if p.val == q.val:
                tmpp = p
            while tmpp.val == q.val:
                tmpp = tmpp.next
                q = q.next
                if q is None:
                    return True
            q = q.next
        p = p.next
        q = header2
    return False



lista = Node(1)
lista.dodawanko(2)
lista.dodawanko(3)
lista.dodawanko(4)
lista.dodawanko(5)
lista.dodawanko(6)
lista.dodawanko(7)

listka = Node(5)
listka.dodawanko(6)
listka.dodawanko(7)

print(f(lista,listka))
