def is_prime(number):
    i=2
    while i < number**0.5 + 1:
        if number%i == 0:
            return False
        i+=1
    return True

def number_of_digits(number):
    digits = 0
    while number > 0:
        digits+=1
        number = number//10
    return digits

def prime_segments(number, array=0):
    array = [0 for x in range(number_of_digits(number))]

