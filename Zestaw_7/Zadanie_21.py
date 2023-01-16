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
    bp = header
    p = header
    bq = header
    q = bq.next
    il_gig = 1
    pgigant = header
    qgigant = header
    dlugosc = 1
    max_len = -1
    while p is not None:
        if q is None:
            break
        elif q.val > bq.val:
            dlugosc += 1
            if dlugosc > max_len:
                pgigant = bp
                qgigant = q
                max_len = dlugosc
                il_gig = 1
            elif dlugosc == max_len:
                il_gig +=1
            bq = q
            q = q.next
        else:
            bp = bq
            p = q
            bq = p
            q = bq.next
            dlugosc = 1
    if il_gig == 1:
        if pgigant == header:
            return qgigant.next
        else:
            pgigant.next = qgigant.next
    return header




lista = Node(10)
lista.dodawanko(11)
lista.dodawanko(12)
lista.dodawanko(13)
lista.dodawanko(14)
lista.dodawanko(15)
lista.dodawanko(11)
lista.dodawanko(12)
lista.dodawanko(13)
lista.dodawanko(9)
lista.dodawanko(100)

lista = funkcja(lista)
lista.printowanko()