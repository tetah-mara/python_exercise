# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:42:22 2021

@author: ahmet
"""

# Write code that returns your name with a greeting as a string. The string should be: "Hi all, 
# This is your_name!". (Careful with punctuation marks.) Your function name should be 
# problem1.


def problem1():
    return "Hi all, This is ahmet_atar!"

# Write code that asks a name and returns the input as a string. The string should be: "Input was 
# input". Your function name should be problem2. (Hint: use input() function to grab user input 
# as a string and prepend "Input was " to the string and return it)


def problem2():
    input("Input was" )
    print(input)
    return

# Write code to accept two input numbers as integers, apply sum operation and return the result. 
#Your function name should be problem3. (Only integer numbers will be tested for correctness.)
          
def problem3():
    a = int(input("First Number:"))
    b = int(input("Second Number:"))
    return a+b 

# Write code to accept two input numbers as floats, apply subtract operation (first - second) and 
# return the result. Your function name should be problem4. (Both integer and float numbers will be 
# tested for correctness.)

def problem4():
    First = float(input("First Number:"))
    Second = float(input("Second Number:"))
    return First - Second

# Write code to accept two input numbers as integers, apply modulo operation and return the result. 
# Your function name should be problem5. (Only integer numbers will be tested for correctness.)

def problem5():
    X = int(input("First Number:"))
    Y = int(input("Second Number:"))
    return X % Y

# Write code that will calculate the volume of a cylinder. First it should 
# ask for the radius. Second, it should ask for the height. Then it should 
# calculate the volume and return the result. All inputs should be treated 
# as floats. pi should be taken as 3.141592. Your function name 
# should be problem6. (Both integer and float numbers will be tested for 
# correctness.)

def problem6():
    pi = 3.141592
    r = float(input("radius:"))
    h = float(input("height:"))
    return pi*r*r*h

# Write code that will calculate the perimeter of a square. Ask for 
# the length of a side. Then calculate the perimeter and return the 
# result as a string with additional wordings. The string should be 
# "The perimeter of the square is value." (Careful with 
# the dot at the end) All inputs should be treated as floats. Your 
#function name should be problem7. (Both integer and float 
# numbers will be tested for correctness.)

def problem7():
    a = float(input("The length of a side: " ))
    value = a*4
    return print("The perimeter of the square is {}".format(value))


