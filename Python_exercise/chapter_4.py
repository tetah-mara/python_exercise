

my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtu.edu.tr"


def problem1(liste,x):
    a = len(liste)
    if x < 0 or x > a:
        return None
    else:
        return len(liste)
    
def problem2(liste,x):
    a = len(liste)
    if a < x:
        return liste
    elif a == x or a >= x:
        liste.remove(a)
        return liste
 
def problem3(liste,x):
    if x == True:
        liste.sort()
        return liste
    elif x == False:
        liste.sort()
        liste.reverse()
        return liste

def problem4(l1,l2):
    count = 0
    for i in l1:
        if i in l2:
            count += 1
    return count      

def problem5(l1,l2):
    weighted_list = []
    for i in range(0,len(l1)):
        n = l1[i]*l2[i]
        weighted_list.append(n)
    x = sum(weighted_list) / sum(l2)
    return x

def problem6(m1):
    def hesap(matrix):
        k = m1[0][0]*m1[1][1] - m1[1][0]*m1[0][1]
        return k
    def hesap_3(matris):
         matris.pop(0)
         a = matris[0]
         b = matris[1]
         a.pop(0)
         b.pop(0)
         matris = [a] + [b]
         z = hesap(matris)
         return z
    if len(m1) == 1:
        return float(m1[0])
    elif len(m1) == 2:
        if len(m1[0]) == len(m1[1]):
            k = hesap(m1)
            return float(k)
    elif len(m1) == 3:
        if len(m1[0]) == len(m1[1]) == len(m1[2]):
            c = hesap_3(m1)
            return c
    elif len(m1) == 4:
        if len(m1[0]) == len(m1[1]) == len(m1[2]) == len(m1[3]):
            m1.pop(0)
            a = m1[0]
            b = m1[1]
            c = m1[2]
            a.pop(0)
            b.pop(0)
            c.pop(0)
            m1 = [a] + [b] + [c]
            l = hesap_3(m1)
            return l
           
            
def problem7(accounts,source,lira,kurus):
    if 0 <= source <= (len(accounts) -1) :
        transfer = lira + kurus/100
        accounts[source] = float(accounts[source])
        if transfer <= accounts[source]:
            accounts[source] = accounts[source] - transfer
            accounts[source] = round(accounts[source],2)
            if int(accounts[source]) == accounts[source]:
                accounts[source] = f"{accounts[source]:.1f}"
            else:
                accounts[source] = f"{accounts[source]:.2f}"
                accounts[source] = str(accounts[source])
            return accounts
        else:
            accounts[source] = f"{accounts[source]:.2f}"
            accounts[source] = str(accounts[source])
            return accounts
    elif source >= len(accounts):
        return accounts
    else:
        return accounts
    
def problem8(accounts,source,destination,lira,kurus,fee = False):
    if 0 <= destination <= (len(accounts) - 1):
        if 0 <= source <= (len(accounts) - 1):
            transfer = lira + kurus/100
            accounts[source] = float(accounts[source])
            accounts[destination] = float(accounts[destination])
            if source == destination:
                accounts[source] = str(accounts[source])
                accounts[destination] = str(accounts[destination])
                return accounts
            else:
                if fee == True:
                    if transfer <= 10:
                        fee = 0.1
                    else:
                        fee = transfer/100
                        fee = round(fee,1)
                if transfer <= accounts[source]:
                    accounts[source] = accounts[source] - transfer - fee
                    accounts[destination] = accounts[destination] + transfer
                    accounts[source] = round(accounts[source],2)
                    if int(accounts[source]) == accounts[source]:
                        accounts[source] = f"{accounts[source]:.1f}"
                    else:
                        accounts[source] = f"{accounts[source]:.2f}"
                        accounts[source] = str(accounts[source])
                    accounts[destination] = round(accounts[destination],2)
                    if int(accounts[destination]) == (accounts[destination]):
                        accounts[destination] = f"{accounts[destination]:.1f}"
                    else:
                        accounts[destination] = f"{accounts[destination]:.2f}"
                        accounts[destination] = str(accounts[destination])
                    return accounts
                else:
                    accounts[source] = f"{accounts[source]:.2f}"
                    accounts[source] = str(accounts[source])
                    accounts[destination] = f"{accounts[destination]:.2f}"
                    accounts[destination] = str(accounts[destination])
                    return accounts
        else:
            return accounts
    elif source >= len(accounts):
        return accounts
    else:
        return accounts
    
def problem9(x):
    pass


            
            
def problem10(liste):
  seen = set()
  seen_add = seen.add
  seen_twice = set(x for x in liste if x in seen or seen_add(x))
  k = list(seen_twice)
  if k != []:
      return str(k[0])
  else:
      return None

       
                
        
    
    
        
      
    

    

        
 
    
        
        

    
    
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        



if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
