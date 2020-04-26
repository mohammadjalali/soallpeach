import sys
from math import sqrt

file_name = sys.argv[1]

def is_prime(n:int) -> bool:

    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
<<<<<<< HEAD
    return True
=======
>>>>>>> 532d1abe1b5ab06b08f1604927e6d7a0e1262ea9

    return True
        

with open(file_name) as input_numbers:
    for line in input_numbers:
        number = int(line)
        print(1 if is_prime(number) else 0)
