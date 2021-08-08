'''
A function in python is a piece of code which runs when it is referenced.
it is used to utilize the code in more than one place in a program.in-built functions, user defined function
print(),input()

def add(x,y):
 return x+y
x=3
y=4
z=add(x,y)
print("z=",z)

def sub(x,y):
 return x-y
x=3
y=4
print(sub(x,y))

def mul(x,y):
 return x*y
x=3
y=4
print(mul(x,y))

#Lambda Function: It is an anonymous function or a function havind no name.
#It is a small and restricted function having no more than one line.

#lambda p1,p2:expression

adder = lambda x,y:x+y

print(adder(1,2))

import math
euclidian_distance=lambda x,y:math.sqrt(x**2)+(y**2)
print(euclidian_distance(3,4))


#map()--> it is used to apply a particular operation to every element in a sequence.
even_list=[2,4,6,8,10]
squared_even_list=map(lambda x:x*x,even_list)

print(list(squared_even_list))
'''
#temperature conversion from c to F using lambda function
temperature_in_c=[39,2,36,5,37,3,38,37,8]
temperature_in_F-map(lambda x:((x * 9/5) + 32), temperature_in_c)
                    
print(list(temperature_in_F))
