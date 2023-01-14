good_ones = []
def area_of_square(square):
    return (square[0] - square[1])**2

def same_area_squares(list, number_used=0, total_area=0):
    global good_ones
    if number_used == 13 and total_area == 2012:
        return True
    if number_used > 13 or total_area > 2012:
        return False


    return good_ones

def generate_number_as_n_squares(number, n = 13):
    if number == 0 and n == 0:
        return True
    if number <= 0 and n != 0:
        return False
    i=1
    while i*i < number:
        i+=1

    if i != 1:
        i-=1

    while i > 0:
        if generate_number_as_n_squares(number-i*i, n - 1):
            print(i)
            return True
        i-=1

    return False

squares = [(0,5,10,15), (3,10,7,14), (29,40,77,88),
           (0,1,0,1),(1,2,1,2),(0,1,1,2),(1,2,0,1),(-1,0,0,1),(-2,-1,0,1),(-1,0,1,2),(-2,-1,1,2),(0,1,-1,0),
           (0,3,10,13),(0,3,14,17),(0,7,20,27), (0,100,-5,95)]

#print(same_area_squares(squares))
generate_number_as_n_squares(91, 7)
