# 1. Create a function.
# Name: get_random_fruit
# Inputs: none
# Output: String
# Description: returns a random fruit name as a string.
# See Exercise 01.
# Choose from at least 5 fruit.

import random


def get_random_fruit():
    match random.randint(0, 4):
        case 0:
            return "Apple"
        case 1:
            return "Banana"
        case 2:
            return "Pineapple"
        case 3:
            return "Pear"
        case 4:
            return "Mango"



if __name__ == "__main__":
    
    print(get_random_fruit())
    print(get_random_fruit())
    print(get_random_fruit())
    print(get_random_fruit())    
    pass
