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

def f(header, headerp, headernp):
    lp = headerp
    lnp = headernp
    wart = Node(None)
    p = header
    wart.next = p
    bp = wart
    cnt = 0
    while p is not None:
        if p.val>0 and p.val%2 == 0:
            lp.next = p
            bp.next = p.next
            p.next = None
            p = bp.next
            lp = lp.next
        elif p.val<0 and p.val%2 == 1:
            lnp.next = p
            bp.next = p.next
            p.next = None
            p = bp.next
            lnp = lnp.next
        else:
            bp = p
            p = p.next
            cnt += 1

    return headerp, headernp, cnt


lista = Node(2)
lista.dodawanko(6)
lista.dodawanko(7)
lista.dodawanko(-1)
lista.dodawanko(-3)
lista.dodawanko(12)

p = Node(None)
np = Node(None)

print(f(lista, p, np))
p.printowanko()
print()
np.printowanko()

