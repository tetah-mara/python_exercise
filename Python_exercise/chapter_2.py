# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:52:19 2021

@author: ahmet
"""

def problem1():
    f = float(input())
    c = (f-32)/1.8
    return c

def problem2():
    c = float(input())
    f = c*1.8 + 32
    return f

def problem3():
    n = int(input())
    n = 2*n**2 - n
    return n

def problem4():
    n = int(input())
    n1 = 2
    n2 = 1
    Lucas =  [n1,n2]
    for i in range(100):
        n1,n2 = n2,n1+n2
        Lucas.append(n2)
    return Lucas[n]
                
def problem5():
     text = str(input()) [::-1]
     return text
def problem6():
    text = str(input())
    removed = """
    :"!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    """
    new = "                                           "
    correctness = str.maketrans(removed,new)
    text = text.translate(correctness)
    text_new = text.replace(" ","")
    return text_new

def problem7():
    x = int(input())
    y = ""
    if x > 0:
        if x < 4:
            return str(x)
        else:
            while x >= 4:
                y = str(x % 4) + y
                x = int(x/4)
                if x < 4:
                    break
            y = str(x % 4) + y
            return y
    elif x == 0:
        return str(x)
    else:
        x = x*-1
        if x < 4:
            return str(x)
        else:
            while x >= 4:
                y = str(x % 4) + y
                x = int(x/4)
                if x < 4:
                    break
            y = str(x % 4) + y
            y = "-" + y
            return y
        
         
openb = ["(","[","{"]
closeb = [")","]","}"]
def problem8():
    x = input()
    stack = []
    for i in x:
        if i in openb:
            stack.append(i)
        elif i in closeb:
            pos = closeb.index(i)
            if ((len(stack) > 0) and (openb[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
    
    
                   
def problem9():
    text = str(input())
    x = text.split()
    return len(x[-1])
            
def problem10():
    x = input()
    vertical = 0
    horizontal = 0
    for i in x:
        if "s" == i:
            vertical -= 1
        if "n" == i:
            vertical += 1
        if "w" == i:
            horizontal -= 1
        if "e" == i:
            horizontal += 1
    distance = (vertical**2 + horizontal**2)**0.5
    
    
    return float(distance)
                            
                        
    
        
       
            
            
        
            
        



    

    
        
        