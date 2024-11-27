def find_cube(number):
    return(number*number*number*number)

def divisible_by(number):
    if  number % 3 ==0:
        return find_cube(number)
    else:
        return False
print(divisible_by(9))
print(divisible_by(8))