comment="""Basic operations like:
1. type conversions
2. mathematical operations     """
#hard-coded initialization

a,b,c=2,2.5,1j
print("\n[] Type of values","\na: ",a,type(a),"\nb: ",b,type(b),"\nc: ",c,type(c),"\n\n[] Conversion:")
x=float(a)
y=int(b)
z=complex(y)
print("Earlier:",a,b,c,"\nNow    :",x,y,z,"\n\n[] Operations:","\nAdd:",a+b,"\nSubtract:",a-b,"\nMultiply:",a*b,"\nDivide:",a/b,"\nModulus:",a%b,"\nExponential:",b**a,"\nFloor Division:",b//a)

#Testing iteration function for a list
chk=[2,3]
print("\n[] List:\n",chk)
it=iter(chk)
print(next(it),next(it))

i="Lets play, with string    "
j="for now"
print("\n\nUpper: ",i.upper(),"\nLower: ",i.lower(),"\n String Length: ",len(i),"\nStrip whitespaces at end: ",i.strip(),"\nReplace L wid G: ",i.replace("L","G"),"\nSplit wid comma: ",i.split(","),"\nConcatenate: ",i+j)

#assignment
word="programmer"
print("\n [1] String Length for ",word," : ",len(word),"\n [2] Print using escape characters: ","We are \"VIKINGS\" of the north","\n\n [3] Print list of numbers to loop through a list :")
list=[1,29,53,74,50,86]
for i in list:
    print(i)

#in-built functions
array=sorted([123,435,46,5,2,124,4,23,67,21]) # for strings, sort order numbers as strings 1st, then upper n then lower case
print("\n Sorted array: ",array)
hl=str(array[1]) + " " + str(array[-2])
print("\n Second lowest n greatest: ",hl)

#defined functions, naming convention, my_function() for functions, MyClass: for classes
def my_function(x,y):
    print("\nNew fn : ",x,"  ",y) #if + is used instead of comma, then integer value of y needs to be converted to str(y)
my_function("test",20)

#infinite args
def print_ppl(*ppl):
    for p in ppl:
        print("Welcome :", p)
print_ppl("a","b","c","d")

def add(a,b):
    return a+b
c=add(5,7)
d=add(6,8)
print("\n 1st add : ",c,"\n 2nd add : ",d)

"""Modules -- external library, that can b included to leverage re-usable code, alrdy written in tht library by some1
Ex: import re <-- re is regex library, alrdy included wid python n need be loaded """
import re
string="Testing FOR nOW"
new=re.sub('[A-Z]',"*",string)
print(new)