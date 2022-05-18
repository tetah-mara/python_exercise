

my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtu.edu.tr"


def problem1(a,n):
    b = set(a)
    output = []
    for i in b:
        x = a.count(i)
        if x == n:
            output.append(i)
    return output

def problem2(dictionary):
    a = list(dictionary.values())
    c = sorted(a)
    b = len(a)
    if b % 2 == 0:
        median = (c[int(b/2)] + c[int(b/2) - 1])/2
        return median
    else:
        median =  a[int(b/2)]
        return median
    
def problem3(filename):
    output = []
    a = open(filename,"r")
    for i in a:
        j = i.split(",")
        dic = {"name":j[0],"credit":j[1],"term":j[2],"grade":j[3]}
        dic["grade"] = dic["grade"].replace("\n","")
        if dic["grade"] == "":
            dic["grade"] = "NA"
        else:
            None
        output.append(dic)
    a.close()
    return output

def problem4(not_listesi,t):
    s = len(not_listesi)
    not_baremi = {"AA":4.0,"BA":3.5,"BB":3.0,"CB":2.5,"CC":2.0,"DC":1.5,"DD":1.0,"FF":0.0,"NA":"NA"}
    avr = []
    kredi_toplami = 0
    for i in range(0,s):
        k = not_listesi[i]
        if k["term"] == t:
            if k["grade"] != "NA":
                weighted_sum = not_baremi[k["grade"]]*k["credit"]
                avr.append(weighted_sum)
                kredi_toplami = kredi_toplami + k["credit"]
            else:
                None
        else:
            None
    if kredi_toplami == 0:
        return 0
    else:
        GPA = sum(avr)/kredi_toplami
        return GPA          

    
    
def ffunc(n):
        a = range(0,n+1)
        b = a.count(1)
        return b
    
def problem5(ffunc,n):
    a = range(0,n+1)
    b = a.count(1)
    c = ffunc(n)
    if b == c:
        return True
    else:
        return False
    
def problem6(string):
    l = len (string)
    for i in range(pow(2,l-1)):
        k = i
        x = 0
        print(string[x], end = "")
        x += 1
        for j in range(len(string)-1):
            if(k & 1):
                print(" ",end = "")
            k = k >> 1
            print(string[x], end = "")
            x += 1
def problem7(str1,str2):
    pass
            
def problem8(matris,sub_matris):
    def sub_mat_find(matris):
        r = len(matris)
        c = len(matris[0])
        count = 0
        x = 0
        sub_matrix_list = []
        while x < r:
            y = x+1
            while y <= r:
                a = 0
                while a < c:
                    b = a+1
                    while b <= c:
                        sm = []
                        for i in matris[x:y]:
                            sm.append(i[a:b])
                        sub_matrix_list.append(sm)
                        count += 1
                        b += 1
                    a += 1
                y += 1
            x += 1
        return sub_matrix_list
    sub_mat = sub_mat_find(matris)
    
    if sub_matris in sub_mat:
        return True
    else:
        return False
    
    
    
            
def problem9(words):
    h = len(words)
    k = list(words)
    binary_list = []
    string = ""
    for i in k:
        x = words.count(i)
        for j in words:
            if j == i:
                k.remove(i)
        if x != 1:
            string = string + i + str(x)
        else:
            string = string + i
            binary_list.append((i,x))
    s = len(string)
    ratio = (100- (100*s/h))
    return string,int(ratio)

def problem10(liste):
    m = max(liste)
    n = min(liste)
    checklist = range(n,m+1)
    counter = len(liste)
    a = 0
    list_up = m + 1
    for i in checklist:
        if i in liste:
            a += 1
            if a == counter:
                return list_up
        else:
            return i
    
            
            
            
            
    
        


    
    
    



if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
