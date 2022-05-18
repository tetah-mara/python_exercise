my_name = "Ahmet Atar"
my_id = "161024045"
my_email = "ahmet.atar2016@gtueduTr"

def problem0():
    '''Doctests
    >>> A = problem0()
    >>> ainst = A(3)
    >>> ainst.get_value()
    3
    >>> A = problem0()
    >>> ainst = A(1)
    >>> ainst.get_value()
    1
    >>> A = problem0()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    
    >>> ainst.set_value(5)
    >>> ainst.get_value()
    5
    '''

    # p0 class is defined inside the function
    # if name is given in the problem, use that name as the class name.
    # If name is NOT given in the problem, pick a name yourself.
    # For example, you can just use p# structure.
    class p0:

        # These are class members. Make sure your indentation is correct.
        def __init__(self, x):
            self.a = x

        def get_value(self):
            return self.a

        def set_value(self, x):
            self.a = x

    # Make sure to always return the class
    # Otherwise we will not see it (i.e. NoneType),
    # and your problem will be marked 0.
    return p0

def problem1():
        class p1:
            def __init__(self,x):
                self.y = x
            def get_value(self):
                if type(self.y) is int:
                    return self.y
                else:
                    return 0
            def set_value(self,x):
                if type(x) is int:
                    self.y = x
                else:
                    pass
        return p1

def problem2():
    class p1:
        def __init__(self,x,y):
            self.a = x
            self.b = y
        def get_area(self):
            return self.a*self.b
        def get_perimeter(self):
            return 2*(self.a + self.b)
    return p1

def problem3():
    class Grades:
        def __init__(self):
            self.default = 0
            self.g = [self.default]
        def add_grade(self,x):
            if self.default in self.g:
                self.g.remove(self.default)
                self.g.append(x)
            elif not self.default in self.g:
                self.g.append(x)
        def remove_grade(self,x):
            if x in self.g:
                self.remove(x)
            else:
                pass
        def get_min(self):
            return min(self.g)
        def get_max(self):
            return max(self.g)
        def get_mean(self):
            return sum(self.g)/len(self.g)
        def get_median(self):
            b = self.g
            c = sorted(b)
            if len(c) % 2 == 1:
                return c[int(len(c)/2)]
            elif len(c) % 2 == 0:
                return (c[int(len(c)/2)-1] + c[int(len(c)/2)])/2
    return Grades
        
def problem4():
    class Movie:
        def __init__(self,movie_name,director,year,rating = 0.0,length = 0):
            self.movie_name = movie_name
            self.director = director
            self.year = year
            if 0.0 < rating < 10.0:
                if type(rating) is float:
                    self.rating = rating
            else:
                pass
            if 0 < length < 500:
                if type(rating) is int:
                    self.length = length
            else:
                pass
        def get_movie_name(self):
            return self.movie_name
        def get_director(self):
            return self.director
        def get_year(self):
            return self.year
        def get_rating(self,x):
            return self.rating
        def get_length(self,x):
            return self.length
    return Movie

def problem5():
    class MovieCatalog:
        def __init__(self,filename):
            file = open(filename)
            self.ml = []
            for i in file:
                k = i.split(",")
                k[2] = int(k[2])
                k[3] = float(k[3])
                k[4] = float(k[4])
                self.m.append(k)
            self.A = problem4()
        def add_movie(self,movie_name,director,year,rating = 0,length = 0):
            self.movie_name = movie_name
            self.director = director
            self.year = year
            self.rating = rating
            self.length = length
            movie_list = [self.movie_name,self.director,self.year,self.rating,self.length]
            if not movie_list in self.ml:
                self.ml.append(movie_list)
        def checklist(self):
            return self.movie_list
    return MovieCatalog

def problem6():
    class Node:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z
        def get_node(self):
            return (self.x,self.y,self.z)
        def get_distance(self):
            distance = ((self.x**2) + (self.y**2) + (self.z**2))**0.5
            return distance
        def __add__(self,new):
            new_x = self.x + new.x
            new_y = self.y + new.y
            new_z = self.z + new.z
            return Node(new_x,new_y,new_z)
        def __str__(self):
            return "<" + str(self.x) + " , " + str(self.y) + " , " + str(self.z) + ">"
        def __gt__(self,new):
            if Node.get_distance(new.x,new.y,new.z) > Node.get_distance(self.x,self.y,self.z):
                return True
            else:
                return False
        def __ge__(self,new):
            if Node.get_distance(new.x,new.y,new.z) == Node.get_distance(self.x,self.y,self.z):
                return True
            else:
                return False
        def __lt__(self,new):
            if Node.get_distance(new.x,new.y,new.z) < Node.get_distance(self.x,self.y,self.z):
                return True
            else:
                return False
        def __le__(self,new):
            if Node.get_distance(self.x,self.y,self.z) <= Node.get_distance(new.x,new.y,new.z):
                return True
            else:
                return False
        def __eq__(self,new):
            if Node(self.x,self.y,self.z) == Node(new.x,new.y,new.z):
                return True
            else:
                return False
    return Node

def problem7():
    class NodeCloud:
        def _init__(self,n):
            self.n = problem6()
            self.n1 = self.n(n)
        pass
def problem8():
    class Encoder:
        def __init__(self,x):
            if x.isalnum() == True:
                self.x = x
            else:
                pass
        def __str__(self):
            return self.x
        def morse(self):
            MORSE_CODE_DICT = { 'A':'.-','a':'.-', 'B':'-...','b':'-...',
                    'C':'-.-.', 'c':'-.-.', 'D':'-..', 'd':'-..', 'E':'.', 'e':'.',
                    'F':'..-.', 'f':'..-.', 'G':'--.', 'g':'--.', 'H':'....', 'h':'....',
                    'I':'..', 'i':'..', 'J':'.---', 'j':'.---', 'K':'-.-', 'k':'-.-',
                    'L':'.-..', 'l':'.-..', 'M':'--', 'm':'--', 'N':'-.', 'n':'-.',
                    'O':'---', 'o':'---', 'P':'.--.', 'p':'.--.', 'Q':'--.-', 'q':'--.-',
                    'R':'.-.', 'r':'.-.', 'S':'...', 's':'...', 'T':'-', 't':'-',
                    'U':'..-', 'u':'..-', 'V':'...-', 'v':'...-', 'W':'.--', 'w':'.--',
                    'X':'-..-', 'x':'-..-', 'Y':'-.--', 'y':'-.--', 'Z':'--..', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
            morse_text = ""
            for letter in self.x:
                if letter != " ":
                    morse_text += MORSE_CODE_DICT[letter] + " "
                else:
                    morse_text += " "
            return morse_text
        def binary(self):
            SEVEN_BIT_ASCII_DICT = { 'A':'1000001','a':'1100001', 'B':'1000010','b':'1100010',
                    'C':'1000011', 'c':'1100011', 'D':'1000100', 'd':'1100100', 'E':'1000101', 'e':'1100101',
                    'F':'1000110', 'f':'1100110', 'G':'1000111', 'g':'1100111', 'H':'1001000', 'h':'1101000',
                    'I':'1001001', 'i':'1101001', 'J':'1001010', 'j':'1101010', 'K':'1001011', 'k':'1101011',
                    'L':'1001100', 'l':'1101100', 'M':'1001101', 'm':'1101101', 'N':'1001110', 'n':'1101110',
                    'O':'1001111', 'o':'1101111', 'P':'1010000', 'p':'1110000', 'Q':'1010001', 'q':'1110001',
                    'R':'1010010', 'r':'1110010', 'S':'1010011', 's':'1110011', 'T':'1010100', 't':'1110100',
                    'U':'1010101', 'u':'1110101', 'V':'1010110', 'v':'1110110', 'W':'1010111', 'w':'1110111',
                    'X':'1011000', 'x':'1111000', 'Y':'1011001', 'y':'1111001', 'Z':'1011010', 'z':'1111010',
                    '1':'0110001', '2':'0110010', '3':'0110011',
                    '4':'0110100', '5':'0110101', '6':'0110110',
                    '7':'0110111', '8':'0111000', '9':'0111001',
                    '0':'0110000'}
            text = ""
            for letter in self.x:
                if letter != " ":
                    text += SEVEN_BIT_ASCII_DICT[letter] + ""
                else:
                    text += " "
            return text
        def hex(self):
            HEX_CODE_DICT = { 'A':'41','a':'61', 'B':'42','b':'62',
                    'C':'43', 'c':'63', 'D':'44', 'd':'64', 'E':'45', 'e':'65',
                    'F':'46', 'f':'66', 'G':'47', 'g':'67', 'H':'48', 'h':'68',
                    'I':'49', 'i':'69', 'J':'4A', 'j':'6A', 'K':'4B', 'k':'6B',
                    'L':'4C', 'l':'6C', 'M':'4D', 'm':'6D', 'N':'4E', 'n':'6E',
                    'O':'4F', 'o':'6F', 'P':'50', 'p':'70', 'Q':'51', 'q':'71',
                    'R':'52', 'r':'72', 'S':'53', 's':'73', 'T':'54', 't':'74',
                    'U':'55', 'u':'75', 'V':'56', 'v':'76', 'W':'57', 'w':'77',
                    'X':'58', 'x':'78', 'Y':'59', 'y':'79', 'Z':'5A', 'z':'7A',
                    '1':'31', '2':'32', '3':'33',
                    '4':'34', '5':'35', '6':'36',
                    '7':'37', '8':'38', '9':'39',
                    '0':'30'}
            hex_text = ""
            for letter in self.x:
                if letter != " ":
                    hex_text += HEX_CODE_DICT[letter] + ""
                else:
                    hex_text += " "
            return hex_text
    return Encoder
        
                   
            
        
            
            
            
        
            
            
            
            
        
        
    
        
        
            
            
            
            
            
                    




















if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.") 

    # You can do checks like this. We will do this way.
    A = problem0()
    # A is the class name, and it is not the instance.
    # We now create an intance using A
    ainst = A(4)
    # Now that we have the instance, we can call the methods.
    assert 4 == ainst.get_value()
    ainst.set_value(5)
    assert 5 == ainst.get_value()

    # alternatively, you can set up doctests and run those
    # autocheck with doctest
    import doctest
    doctest.testmod()

    print("Completed all doctests.")

