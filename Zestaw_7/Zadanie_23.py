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


def f(header):
    p = header
    q = header
    tmp = header
    cnt = 1
    while p is not None and q is not None:
        p = p.next
        q = q.next.next
        if p == q:
            tmp = p
            p = p.next
            while tmp != p:
                p = p.next
                cnt+=1
            return cnt


lista = Node(1)
lista.dodawanko(2)
lista.dodawanko(3)
lista.dodawanko(4)
lista.dodawanko(5)
lista.dodawanko(6)
lista.next.next.next.next.next.next = lista.next.next.next

print(f(lista))