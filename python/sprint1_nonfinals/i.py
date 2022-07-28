"""Степень 4х"""

import math

def is_power_of_four(number: int) -> bool:
    i = math.sqrt(number)
    if i - int(i) == 0:
        return True
    return False
    
print(is_power_of_four(int(input())))
