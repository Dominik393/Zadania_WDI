class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.last = None

    def dodawanko(self,val):
        p = self
        while p.next is not None:
            p = p.next
        p.next = Node(val)
        p.next.last = p

    def printowanko(self):
        p = self
        while p is not None:
            print(p.val)
            p = p.next

def rebase(number, base):
    answ = 0
    power = 0
    while number > 0:
        answ += (number%base)*10**power
        power += 1
        number //= base
    return answ

def amount_of_digit(number, digit):
    answ = 0
    while number > 0:
        if number%10 == digit:
            answ += 1
        number //=10
    return answ

def funkcja(header):
    p = header
    while p is not None:
        if amount_of_digit(rebase(p.val,2),1) % 2 == 1:
            if p.last is None:
                p = p.next
                header = header.next
                p.last = None
            elif p.next is None:
                p = p.last
                p.next = None
            else:
                p.next.last, p.last.next = p.last, p.next
                p = p.next
        else:
            p = p.next
    return header


lista = Node(4)         #  100
lista.dodawanko(8)      # 1000
lista.dodawanko(10)     # 1010
lista.dodawanko(11)     # 1011
lista.dodawanko(17)     #10001
lista.dodawanko(19)     #10011
lista.printowanko()
print()
lista = funkcja(lista)