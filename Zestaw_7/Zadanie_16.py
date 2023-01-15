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


def rebase(number, base):
    answ = 0
    power = 0
    while number > 0:
        answ += (number%base)*10**power
        power +=1
        number //=base
    return  answ

def amount_of_digit(number, digit):
    answ = 0
    while number > 0:
        if number%10 == digit:
            answ += 1
        number //=10
    return answ

def zadanie(header):
    bp = header
    p = header.next
    wart = Node(None)
    wart.next = header
    while p is not None:
        if amount_of_digit(rebase(p.val,8),5) % 2 == 0 and amount_of_digit(rebase(p.val,8),5) != 0:
            bp.next = p.next
            p.next = wart.next
            wart.next = p
            p = bp.next
        else:
            bp = p
            p = p.next
    return wart.next


lista = Node(109)       #155
lista.dodawanko(150)    #226
lista.dodawanko(333)    #515
lista.dodawanko(166)    #246
lista.dodawanko(381)    #575
lista.printowanko()
print()
odp = zadanie(lista)
odp.printowanko()