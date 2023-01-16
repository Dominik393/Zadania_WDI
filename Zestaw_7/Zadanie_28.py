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
    bp = header1
    p = bp.next
    bq = header2
    q = bq.next
    flaga = False
    while p is not None:
        while q is not None:
            if q.val == p.val:
                flaga = True
                bq.next = q.next
                q = bq.next
            else:
                bq = q
                q = bq.next
        if flaga:
            bp.next = p.next
            p = bp.next
            flaga = False
            bq = header2
            q = bq.next
        else:
            bp = p
            p = p.next
            bq = header2
            q = bq.next

    p = header1
    warp = Node(None)
    warp.next = p
    q = header2
    warq = Node(None)
    warq.next = q
    bq = warq
    flaga = False
    while q is not None:
        if p.val == q.val:
            flaga = True
            bq.next = q.next
            q = bq.next
        else:
            bq = q
            q = q.next
    if flaga:
        warp.next = p.next
    return warp.next






lista = Node(1)
lista.dodawanko(2)
lista.dodawanko(3)
lista.dodawanko(4)
lista.dodawanko(5)
lista.dodawanko(6)
lista.dodawanko(7)
lista.dodawanko(8)

listka = Node(4)
listka.dodawanko(10)
listka.dodawanko(7)
listka.dodawanko(4)
listka.dodawanko(1)

f(lista, listka)

lista.printowanko()
