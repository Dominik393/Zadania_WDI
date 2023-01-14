class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

    def dodawanko(self, val):
        p = self
        while p.next != None:
            p = p.next

        p.next = Node(val)

    def printowanko(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next


def iloczyn(z1, z2, z3):
    p = z1
    d = z2
    t = z3

    lista = Node(None)
    ostatnia = lista

    while p != None and d != None and t != None:
        if p.val <= d.val:
            if p.val <= t.val:
                nowy = Node(p.val)
                ostatnia.next = nowy
                ostatnia = nowy
                p = p.next
            else:
                nowy = Node(t.val)
                ostatnia.next = nowy
                ostatnia = nowy
                t = t.next
        else:
            if d.val <= t.val:
                nowy = Node(d.val)
                ostatnia.next = nowy
                ostatnia = nowy
                d = d.next
            else:
                nowy = Node(t.val)
                ostatnia.next = nowy
                ostatnia = nowy
                t = t.next

    if p is None:
        np = d
        nd = t
    elif d is None:
        np = p
        nd = t
    else:
        np = p
        nd = d

    while np.next != None and nd.next != None:
        if np.val <= nd.val:
            nowy = Node(np.val)
            ostatnia.next = nowy
            ostatnia = nowy
            np = np.next
        else:
            nowy = Node(nd.val)
            ostatnia.next = nowy
            ostatnia = nowy
            nd = nd.next

    if np is None:
        nnp = nd
    else:
        nnp = np

    while nnp is not None:
        nowy = Node(nnp.val)
        ostatnia.next = nowy
        ostatnia = nowy
        nnp = nnp.next


    return lista


listka = Node(1)
listka.dodawanko(3)
listka.dodawanko(7)
listka.dodawanko(11)
listka.dodawanko(14)

listeczka = Node(2)
listeczka.dodawanko(5)
listeczka.dodawanko(7)
listeczka.dodawanko(23)


lysta = Node(1)
lysta.dodawanko(3)
lysta.dodawanko(6)
lysta.dodawanko(66)

nowa = iloczyn(lysta, listka, listeczka)
nowa.printowanko()