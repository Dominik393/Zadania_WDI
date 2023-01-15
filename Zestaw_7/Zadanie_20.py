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

def overlap(p1, p2):
    return (p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[1]
            or p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[1])

def funkcja(header):
    p = header
    bq = p
    q = bq.next
    flag = False
    while True:
        while q is not None:
            if overlap(p.val, q.val):
                p.val[0] = min(p.val[0], q.val[0])
                p.val[1] = max(p.val[1], q.val[1])
                bq.next = q.next
                q = q.next
                flag = True
            else:
                bq = q
                q = q.next
        if not flag and p.next is None:
            return header
        elif p.next is not None:
            p = p.next
            bq = p
            q = bq.next
        else:
            return header



lista = Node([2,10])
lista.dodawanko([4,8])
lista.dodawanko([9,12])
lista.dodawanko([13,15])
lista.printowanko()
print()

funkcja(lista)
lista.printowanko()