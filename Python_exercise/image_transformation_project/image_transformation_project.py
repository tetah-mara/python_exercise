my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtu.edu.tr"


import random


def generate_random(row,column):
    def dict_gen():    
        R = random.randint(0,255)
        G = random.randint(0,255)
        B = random.randint(0,255)
        pixel = {"R":R,"G":G,"B":B}
        return pixel
    liste_1 = []
    for i in range(0,row*column):
        liste_1.append(dict_gen())
    x = len(liste_1)/float(column)
    y = []
    last = 0.0
    while last < len(liste_1):
        y.append(liste_1[int(last):int(last + x)])
        last += x
    return y
    

def is_valid(img):
     r = len(img)
     c = len(img[0])
     control = 0
     for i in range(0,r):
         k = 0
         m = img[i]
         while k < c:
             if 0 <= m[k]["R"] < 256 and 0 <= m[k]["G"] < 256 and 0 <= m[k]["B"] < 256:
                 k += 1
             else:
                 k += 1
                 control += 1
     if control == 0:
         return True
     else:
         return False
                 
             
def read_from_file(filename):
    a = open(filename)
    lines = [line.rstrip() for line in a]
    for i in range(0,len(lines)):
        lines[i] = lines[i] + "," 
    main = []
    for i in range(0,len(lines)):
        liste = list(lines[i].split(","))
        liste.pop()
        main.append(liste)
    img = []
    for i in range(0,len(main)):
        img_columns = []
        img.append(img_columns)
        for j in range(0,len(main[0])):
            k = main[i][j]
            R = int(k[0],16)*16 + int(k[1],16)
            G = int(k[2],16)*16 + int(k[3],16)
            B = int(k[4],16)*16 + int(k[5],16)
            pixel = {"R":R,"G":G,"B":B}
            img_columns.append(pixel)
    a.close()
    return img

def write_to_file(img,filename):
    image = []
    for i in range(0,len(img)):
        image_column = []
        image.append(image_column)
        for j in range(0,len(img[0])):
            hexString_1 = hex(int(img[i][j]["R"] / 16))
            hexString_1 = hexString_1.strip("0x")
            hexString_2 = hex(img[i][j]["R"]%16)
            hexString_2 = hexString_2.strip("0x")
            hexString_3 = hex(int(img[i][j]["G"] / 16))
            hexString_3 = hexString_3.strip("0x")
            hexString_4 = hex(img[i][j]["G"]%16)
            hexString_4 = hexString_4.strip("0x")
            hexString_5 = hex(int(img[i][j]["B"] / 16))
            hexString_5 = hexString_5.strip("0x")
            hexString_6 = hex(img[i][j]["B"]%16)
            hexString_6 = hexString_6.strip("0x")
            hexString = hexString_1 + hexString_2 + hexString_3 + hexString_4 + hexString_5 + hexString_6
            image_column.append(hexString)
    b = open(filename,"w")
    for i in range(0,len(image)):
        c = str(image[i])
        c = c + "\n"
        c = c.strip("[]")
        b.write(c)
    return

def clear(img):
    r = len(img)
    c = len(img[0])
    for i in range(0,r):
        k = 0
        m = img[i]
        while k < c:
            m[k] = {"R":0,"G":0,"B":0}
            k += 1
    return None

def set_value(img,value,string):
    if "r" or "g" or "b" in string:
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                if "r" in string:
                    m[k]["R"] = value
                else:
                    None
                if "g" in string:
                    m[k]["G"] = value
                else:
                    None
                if "b" in string:
                    m[k]["B"] = value
                else:
                    None
                k += 1
    else:
        None

def fix(img):
    r = len(img)
    c = len(img[0])
    for i in range(0,r):
        k = 0
        m = img[i]
        while k < c:
            if m[k]["R"] > 255:
                m[k]["R"] = 255
            elif m[k]["R"] < 0:
                m[k]["R"] = 0
            else:
                None
            if m[k]["G"] > 255:
                m[k]["G"] = 255
            elif m[k]["G"] < 0:
                m[k]["G"] = 0
            else:
                None
            if m[k]["B"] > 255:
                m[k]["B"] = 255
            elif m[k]["B"] < 0:
                m[k]["B"] = 0
            else:
                None
            k += 1

def enhance(img,value,channel = "rgb"):
    r = len(img)
    c = len(img[0])
    for i in range(0,r):
        k = 0
        m = img[i]
        while k < c:
            if "r" in channel:
                m[k]["R"] = value*m[k]["R"]
            else:
                None
            if "g" in channel:
                m[k]["G"] = m[k]["G"]*value
            else:
                None
            if "b" in channel:
                m[k]["B"] = m[k]["B"]*value
            else:
                None
            k += 1
            
def rotate90(img):
    new_img = []
    for i in range(len(img[0])):
        li = list(map(lambda x: x[i], img))
        li.reverse()
        new_img.append(li)
    return new_img

def rotate180(img):
    new_img2 = rotate90(img)
    neww_img2 = rotate90(new_img2)
    return neww_img2

def rotate270(img):
    new_img3 = rotate90(img)
    neww_img3 = rotate90(new_img3)
    newww_img3 = rotate90(neww_img3)
    return newww_img3

def mirror_x(img):
    r = len(img)
    for i in range(0,r):
            img[i] = img[i][::-1]
    return img

def mirror_y(img):
    img = img[::-1]
    return img

def convertInteger(img):
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                m[k]["R"] = int(m[k]["R"])
                m[k]["G"] = int(m[k]["G"])
                m[k]["B"] = int(m[k]["B"])
                k += 1

def grayscale(img,mode=1):
    def mode_1(img):
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                m[k]["R"] = int((m[k]["R"] + m[k]["G"]+ m[k]["B"])/3)
                m[k]["G"] = m[k]["R"] 
                m[k]["B"] = m[k]["R"] 
                k += 1 
    def mode_2(img):
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                m[k]["R"],m[k]["G"],m[k]["B"] = int(m[k]["R"]*0.299),int(m[k]["G"]*0.587),int(m[k]["B"]*0.114)
                k += 1  
    def mode_3(img):
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                m[k]["R"],m[k]["G"],m[k]["B"] = int(m[k]["R"]*0.2126),int(m[k]["G"]*0.7152),int(m[k]["B"]*0.0722)
                k += 1  
    def mode_4(img):
        r = len(img)
        c = len(img[0])
        for i in range(0,r):
            k = 0
            m = img[i]
            while k < c:
                m[k]["R"],m[k]["G"],m[k]["B"] = int(m[k]["R"]*0.2627),int(m[k]["G"]*0.6780),int(m[k]["B"]*0.0593)
                k += 1
    if mode == 1:
        img = mode_1(img)
    elif mode == 2:
        img = mode_2(img)
    elif mode == 3:
        img = mode_3(img)
    elif mode == 4:
        img = mode_4(img)
        
def get_freq(img,channel = "rgb",bin_size = 16):
    r = len(img)
    c = len(img[0])
    R_count = []
    G_count = []
    B_count = []
    h = 0
    while h < (256/bin_size):
        R_count.append(0)
        G_count.append(0)
        B_count.append(0)
        h += 1
    freq_list = list(range(0,257,bin_size))
    freq = {"bin_size":bin_size,"red":R_count,"green":G_count,"blue":B_count}
    for i in range(0,r):
       for j in range(0,c):
           b = freq_list[-1]/bin_size + 1
           k = 1
           while k < b:
               if freq_list[k-1] < img[i][j]["R"] < freq_list[k]:
                   R_count[k-1] += 1
               if freq_list[k-1] < img[i][j]["G"] < freq_list[k]:
                   G_count[k-1] += 1
               if freq_list[k-1] < img[i][j]["B"] < freq_list[k]:
                   B_count[k-1] += 1
               k += 1
    if not "r" in channel:
        freq.pop("red")
    else:
        None
    if not "g" in channel:
        freq.pop("green")
    else: 
        None
    if not "b" in channel: 
        freq.pop("blue")
    else:
        None
    return freq

def scale_down(img,N):
    r = len(img)
    c = len(img[0])
    if r*c % N*N == 0:
        return img
    elif r*c % N*N != 0:
        i = 1
        while r*c % N*N == 0:
            for j in range(0,r):
                img[j].append(img[j][c-i])
            img.append(img[r-i])
            i += 1
        return img
    pass
def scale_up(img,N):
    pass

def apply_window(img,window):
    pass
            
            
            
            















if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")   
            



            
              
        
        
        
        
        
    
    
    
    
    
    
    

    
    
