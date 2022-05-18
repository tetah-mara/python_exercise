


my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtu.edu.tr"




def problem1(deste): # Deste içinde "K" olduğunda true dönmektedir.
    wanted = "K"
    for i in deste:
        if wanted in deste:
            return True
        else:
            return False
        
def problem2(a,b,c,d):  #girilen inputları listeye çevirip sort ile sıralayarak ilk index dönmektedir.
    liste = [a,b,c,d]
    liste.sort()
    return float(liste[0])

def problem3(x,y):
    if type(x) is float:
        if 0 < y < x < 1:
            if (1-y) <= y: # y 1'e yakındır.
                return 1
            else:
                return 0
        elif -1 < x < y < 0:
            if (-1-y) >= y: # y -1'e yakındır.
                return -1
            else:
                return 0
        elif x > y:
            if round(x) > x:
                x = round(x) - 1
                return x
            else:
                return round(x)
        else:
            if round(x) < x:
                x = round(x) + 1
                return x
            else:
                return round(x)
    else:
        return x

def problem4(radius,height,pi=3.1415):
    volume = (radius**2)*pi*height
    return volume

def problem5(radius,height,pi=3.1415): # girilen girdilerin type ları kontrol edilerek koşul aranmıştır.
    volume = -1
    if type(radius) == float or type(radius) == int:
        if type(height) == float or type(height) == int:
            if type(pi) == float or type(pi) == int:
                volume = (radius**2)*pi*height
        return volume
    else:
        return volume

def problem6(girdi):  
    for i in girdi:
        count = girdi.count(i)
        if count > 1:
            pass
        else:
            return i
        
def problem7(girdi):
    asc = sorted(girdi)
    ilk =list(girdi)
    if asc == ilk:
        return True
    else:
        return False
    
def problem8(girdi):
    if len(girdi) == len(set(girdi)):
        return True
    else:
        return False
    
def problem9(row,column):
    i = row
    j = column
    if i == 1 and j == 1:
        return 1
    elif i > 1 and j == 1:
        return 3
    elif i > 1 and j == i:
        return 2
    else:
        return problem9(i-1,j-1) + problem9(i-1,j)
    
def problem10(str1,str2):
    l1 = list(str1)
    l2 = list(str2)
    count = 0
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if i == j: 
                if l1[i] == l2[i]:
                    count += 1
                else:
                    pass
    return count



if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

    
