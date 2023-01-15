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

    def print_in_base(self,base):
        p = self
        while p is not None:
            print(rebase(p.val,base))
            p = p.next

def rebase(number, system = 2):
    answ = 0
    power = 0
    while number > 0:
        answ += (number%system)*10**power
        number//=system
        power+=1
    return answ

def amount_of_digits(number, digit):
    answ = 0
    while number>0:
        if number%10 == digit:
            answ+=1
        number//=10
    return answ

def deletion(header):
    p = header
    if header.next is not None:
        while amount_of_digits(rebase(header.val,3),1) > amount_of_digits(rebase(header.val,3),2):
            header = header.next
        p = header
    while p.next is not None:
        if amount_of_digits(rebase(p.next.val,3),1) > amount_of_digits(rebase(p.next.val,3),2):
            p.next = p.next.next
        p = p.next
        if p is None:
            break

    return header


lista = Node(99)        #10200
lista.dodawanko(15)     #120
lista.dodawanko(20)     #202
lista.dodawanko(22)     #211
lista.dodawanko(29)     #1002
lista.dodawanko(97)     #10121
lista.print_in_base(3)
print()

lista = deletion(lista)
lista.printowanko()
