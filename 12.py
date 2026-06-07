mark={"english":95,"chemistry":98}
information={"ram":"balkishan"}
print(mark["chemistry"])
mark["physics"]=97
print(mark)
mark["physics"]=99
print(mark)
print("Functions")
print("Functions")
print("1. In-Built Functions")
print("2. Module Functions")
print("3. User-Defined Functions")
# 1.
# int()
# str()
# bool()
# 2.
import math
print(dir(math))
from math import sqrt
print(sqrt(4))
print(sqrt(16))
from math import *
# 3.
# def function_name(parameters):
#    // do something
def print_sum(first,second=4):
    print(first+second)
print_sum(1,2)
print_sum(1)