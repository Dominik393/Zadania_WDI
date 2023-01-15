class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def dodawako(self, val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def printowanko(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next

def porzadkuj(header):
    p = header
    removed = None
    while p.next is not None:
        if p.val > p.next.val:
            removed = p.next
            if removed.next is not None:
                while removed.val > removed.next.val:
                    if removed.next is None:
                        break
                    removed = removed.next
            p.next = removed.next
            p = p.next
        else:
            p = p.next


lista = Node(200)       #Zostanie
lista.dodawako(202)     #Zostanie
lista.dodawako(202)     #Zostanie
lista.dodawako(200)     #Usunie
lista.dodawako(100)     #Usunie
lista.dodawako(140)     #Zostanie
lista.dodawako(150)     #Zostanie

porzadkuj(lista)
lista.printowanko()