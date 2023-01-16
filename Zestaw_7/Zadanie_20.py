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

def f(header):
    p = header
    bq = p
    q = bq.next
    while p is not None:
        while q is not None:
            if overlap(p.val, q.val):
                p.val[0] = min(p.val[0], q.val[0])
                p.val[1] = max(p.val[1], q.val[1])
                bq.next = q.next
                bq = p
                q = bq.next
            else:
                bq = q
                q = q.next
        p = p.next



lista = Node([2,10])
lista.dodawanko([13,15])
lista.dodawanko([4,8])
lista.dodawanko([9,12])


listunia = Node([15,19])
listunia.dodawanko([20,21])
listunia.dodawanko([18,20])
listunia.dodawanko([5,6])
listunia.dodawanko([8,12])
listunia.dodawanko([13,14])

f(listunia)
listunia.printowanko()