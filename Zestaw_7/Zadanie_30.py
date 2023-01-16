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
    while p is not None:
        while q is not None:
            if bp.val < q.val < p.val:
                bq.next = q.next
                bp.next = q
                q.next = p
                q = bq.next
            else:
                bq = q
                q = q.next
        bp = p
        p = p.next
        bq = header2
        q = bq.next
        if p is None:
            bq = header2
            q = bq.next
            while q is not None:
                if bp.val < q.val:
                    bq.next = q.next
                    bp.next = q
                    q.next = p
                    q = bq.next
                    bq = bq.next
                else:
                    bq = q
                    q = q.next

    # bp = header1
    # p = bp.next
    # q = header2
    # bq = q.next
    # while q is not None:
    #     pass


lista = Node(2)
lista.dodawanko(3)
lista.dodawanko(5)
lista.dodawanko(7)
lista.dodawanko(11)

listka = Node(8)
listka.dodawanko(2)
listka.dodawanko(12)
listka.dodawanko(4)

f(lista,listka)
lista.printowanko()