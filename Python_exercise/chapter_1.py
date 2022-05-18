# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:52:41 2021

@author: ahmet
"""

def problem1():
    my_names = "ahmet"
    return my_names[0]

    
    
def problem2():
    my_names = "ahmet"
    n = int(input())
    if 0 < n < 5:
        print(my_names[n])
    elif  n == 0:
        print(my_names[0])
    else:
        print(my_names[n % 5])    
    return my_names[n]

def problem3():
    my_names = "ahmet"
    x = int(input("Index1:"))
    y = int(input("Index2:"))
    if (0 < x < 5 and 0 < y < 5) and x < y:
        return my_names[x-1:y]
    elif (0 < x < 5 and 0 < y < 5) and y < x:
        return my_names[y-1:x]
    elif (x > 5 or y > 5) and x % 5 < y % 5:
        x = x % 5
        y = y % 5     
        return my_names[x-1:y]
    elif (x > 5 or y > 5) and y % 5 < x % 5:
        x = x % 5
        y = y % 5
        return my_names[y-1:x]
    else:
        x = x % 5
        y = y % 5
        if x > y:
            return my_names[y-1:x]
        else:
            return my_names[y-1:x]
        
def problem4():
    vowels = "aeiouAEIOU"
    text = input()
    counter = 0
    for letter in text:
        if letter in vowels:
            counter += 1
    print(counter)
        
def problem5():
    your_id = input("Your ID: ")
    s = 0
    for x in str(your_id):
        s += int(x)
    return s
        
        
def problem6():
    x = int(input())
    f = 1
    for k in range(x):
        f = f * (k+1)
    return f      

def problem7():
    x = int(input())
    if (x % 3 != 0) or (x % 7 != 0):
        return False
    else:
        return True
    
def problem8():
    x = int(input())
    y = x % 3 
    z = x % 7
    if y == 0 and z != 0:
        return 1
    elif (y != 0) and z == 0:
        return 2
    elif (y == 0) and (z == 0):
        return 3
    else:
        return "geçersiz input seçimi"
    
def problem9():
    x = int(input())
    if x > 1:
        for k in range(2,x):
            if (x % k == 0):
                return False
                break
        else:
            return True
    else:
        return False
        
def problem10():
    z = float(input())
    if(z == 0):
        return 0;
    x = z/2.0;
    y = x + 1;
    while(x != y):
        n = z/ x;
        y = x;
        x = (x + n)/2;

    return x;
        
            
        
        
         
