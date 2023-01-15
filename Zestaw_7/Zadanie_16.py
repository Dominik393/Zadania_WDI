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
    p = header
    parzyste = Node(None)
    nieparzyste = Node(None)
    while p is not None:
        if amount_of_digit(rebase(p.val,8),5) % 2 == 0 and amount_of_digit(rebase(p.val,8),5) != 0:
            parzyste.dodawanko(p.val)
        else:
            nieparzyste.dodawanko(p.val)
        p = p.next

    nieparzyste = nieparzyste.next
    while nieparzyste is not None:
        parzyste.dodawanko(nieparzyste.val)
        nieparzyste = nieparzyste.next
    return parzyste.next


print(rebase(100,8))
print(rebase(150,8))
print(rebase(166,8))
print(rebase(381,8))
print()

lista = Node(100)
lista.dodawanko(150)
lista.dodawanko(166)
lista.dodawanko(381)
lista.printowanko()
print()
odp = zadanie(lista)
odp.printowanko()