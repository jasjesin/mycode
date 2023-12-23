#program to type in coding for assignments

"""
fn=input("\nFirst Name: ")
ln=input("\nLast Name: ")
print("\n Reverse Order : ",ln,fn)
"""

"""
n1=int(input("\n1st Number: "))
n2=int(input("\n2nd Number: "))
print("\n Sum Total : ",n1+n2)
"""

"""
chickens=int(input("\nEnter count of chickens : "))
cows=int(input("\nEnter count of cows : "))
pigs=int(input("\nEnter count of pigs : "))
print("Total count of legs:",2*chickens+4*cows+4*pigs)
"""

"""
n1=int(input("\n1st Number: "))
n2=int(input("\n2nd Number: "))
n3=int(input("\n3rd Number: "))
if (n1 == n2) and (n2 == n3):
    print("\n3 times sum :",3*(n1+n2+n3))
else:
    print("\nsum total :", (n1 + n2 + n3))
"""

"""
x=int(input("\nEnter number: "))
if x >= 90:
    print("\nGrade A")
elif x >= 80:
    print("\nGrade B")
elif x >= 70:
    print("\nGrade C")
elif x >= 60:
    print("\nGrade D")
else:
    print("\nGrade F")
"""

"""
x=int(input("\nEnter year: "))
if x%4 == 0 or x%400 == 0:
    print("\n",x," is a leap year")
else:
    print("\n",x," is not a leap year")
"""
"""
i=2
while i<22:
    print(i)
    i = i + 2
"""

"""
for i in range(2,22,2):
    print(i)
"""

"""
n=int(input("\nEnter number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("\nSum of all the numbers: ",sum)
"""

"""
list=[3, 5, 9, 3, 2, 9, 10]
for i in list:
    print(i)
"""

"""
tuple=("one", "two", "three", "four", "five")
for i in tuple:
    print(len(i))
"""

"""
def calculation(a,b,sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b

print(calculation(3,5,"+"))
print(calculation(3,8,"-"))
"""

"""
def showEmployee(name,sal):
    print("\nEmployee ",name," salary is: ",sal)

showEmployee("Sam",9000)
"""

"""
def outerFn(a,b):
    def innerFn(a,b):
        return a+b
    print("\nTotal : ",8+innerFn(a,b))

outerFn(5,10)
"""

"""
str=input("\nEnter a word : ")
str1=str[::-1]
if str == str1:
    print("\n",str," is a palindrome.")
else:
    print("\n",str," is not a palindrome.")
"""

"""
#strings related functions
a="apple" ;b="ball" ;c='cat'
print(a,b,c,sep = " : ")
print(a,b,c,end = " !! \n\n")

day="good Morning"
nite="good night"
print(day.capitalize())   # init cap

print(str(20**50))        # addition of numbers in string
print(nite.count("o"))    # searches for specified string n counts total
"""

#mess="""\\PLZ #@CLEANUP-- #@THIS MESSY #@DOCSTRING
#WHICH --CAN HAVE\\MULTIPLE LINES\\
#OF STRING--"""
#print(mess.replace("\\"," ").replace("#@","").replace("--","").replace("\n","").lower()) # kind of sed cmd replacement work

#print(nite[6:])           # starts printing from 6th index location onwards

# len starts from 1, index starts from 0
"""
print(day.endswith("}"))    # checks last character n returns value as true or false
print(day.endswith("g"))    # checks last character n returns value as true or false
print(day.find("n"))        # finds 1st index location of specified character
print(day[0::2])            # starts from specified location n skips by specified no. (2 here)
print(day[::-2])            # starts from specified location n skips by specified no. in reverse, from right to left (2 here)
print(nite.split())         # splits multiple words into a list, can be considered like a cut in bash
print(nite.split()[1])      # splits multiple words into a list, can be considered like a cut in bash
print(len(mess.split()))    # splits multiple words into a list n counts length
print(mess.split()[3:10:2]) # splits multiple words into a list n then picks from start n end location, with skip number (2 here)


# replacement characters, like %s or %d were read earlier. This one is format that replaces curly braces wid provided key values
name="Jas"
grade="B+"
str="This {} got {} grade"
print(str.format(name,grade))

# with lists
animals=["dog","cat","rabbit","bird"]
msg="I saw {}, {} and {} near my home"
print(msg.format(*animals))

# math operations
a=5
b=3
print("%d * %d = %.3f" % (a,b,(a/b)))

# lists
print(range(10))               # defines range from 0 to specified nu,ber
print(list(range(11)))         # defines list
print(list(range(0,20,2)))     # defines list of no.s starting frm 0 n skip by 2

# nested lists
nest=[[1,2,3],[4,5,6]]
print(nest[0])
new=[list(range(5)),list(range(5,10))]
print(nest+new)

num=[34, 76, 12, 5]
print(num)
num.sort()
print(num)
num.reverse()                 # this maybe needed to sort in reverse, for top scores for tht coding challenge
print(num)

animals.append(num)
print(animals)
animals[4].insert(4,["hey!"])
print(animals)
print(animals[4][4][0])       # 3 nested lists, located element inside 3rd nested list

#tuples -- support count n index only

"""

""" dictionaries -- contains keys n key-value pairs, separated by colons
called as dict, can contain
    strings, numbers, tuples, lists, set, series, dataframes, nested dictionaries

list   --> []
tuples --> ()
dict   --> {}
"""

"""
d1= {'A' : 10, 'B' : 20}
d1["C"]=30
print(d1)
toys={'car' : "$10.95", "robot" : "25.65"}
d1.update(toys)                               # method to concatenate or append 2 dictionaries
print(d1)
d1.pop("car")
print(d1)

l1=list(d1.values())                          # converts dictionary into list for indexing; .keys() provides keys, .values() provides values
print(l1)

# nested dictionary
maze = {"k1": d1,
        "k2": [1,2,3],
        "k3": ('tuple!',[1,2,['a','b','catch me!']])}
print(maze)
print(maze["k3"][1][2][2])

complex= {
    "3683640322031616":
        {
            "id":"6f9c741d-e2e9-5062-9c23-bf4210f92e23","data":"Gi du nakab ded peniktuv ihcurtew eh suw uw matow tira uraehomi fe mar wuseoc ibokikkez itoputo. Febcuna neda okkein god cinhitkop topfup wimizo uneni favosca jolef der dacmar. Wa utucori fogarsib zodokuwa ogoje ikpopaj jeh ce baclatki pisbera verolide lomhozes uco fipsi oj im fil. Eske ecwu epohehes heti tik fip gokfawma ote zabwam go ig ba micati. Ele hufet ohibu jeele juhvav udih nobew mohheihi bahher pol jiw jevvi watobci jit imolenob."
        },
    "2580811517788160":
        {
            "id":"d9ed1874-8d9f-5049-9382-8834f7a45e82","data":"Pafwefowo vihbek luhih igo coziculo zurva pocad bur ca wokut mivdeso bam ta giwacedu danos. Ret ba saev bikihi wuc uf hahusago zolkewago mishe kutzi buejedu ziw evatap ocmo nakgup roj evlabigo. Gid co umase tegbi ekaehajan rajodti no wugfueku omukeza coeruv iwfo le. Re ce pehen mioc etevod akwega pufbac boridsi vil zas kirif biuza fowzer. Foszo nevo pezjo sit sihno mehfiw lif dadoala lahutge wa ud owojef."
        }
          }

l2=list(complex.keys())
l3=list(complex.values())
print(complex)
print("\nl2:",l2)
print("\nl3:",l3)
l4=[]
print("\n\n Testing to pick values from complex dict")
for i in l3[0][1] 
"""

""""
# append vs extend -- append adds a list as is, wid square brackets, extend avoids adding square brackets
a=['1','2','3']
b=['abc']
a.append(b)
print("\n Append: ",a)
a.extend(b)
print("\n Extend: ",a)
"""

"""
# zip -- helps perform math operations between lists, wid integer values, for strings, it concatenates, gives error for str n int operation
a=[1,2,3,'4','Jas ']
b=[4,5,6,'7','Singh']
c=[i+j for i,j in zip(a,b)]
print("\nSum Total:",c)
"""

"""
# multiplication for 2 lists
a=[1,2,3]
b=2*a
print("\n b:",b)
c=[2*i for i in a]
print("\n c:",c)
"""

"""
# Convert Lists into Dictionary
key=['name','age','grade']
values=['Jas',38,'B']
d={}
for i,j in zip(key,values):
    d.update({i:j})

print("\nDictionary: ",d)

e=list(d.keys())
f=list(d.values())
print("\nList e: ",e)
print("\nList f: ",f)
"""

nested_dict= {
    "3683640322031616":
        {
            "id":"6f9c741d-e2e9-5062-9c23-bf4210f92e23",
            "data":"Gi du nakab ded peniktuv ihcurtew eh suw uw matow tira uraehomi fe mar wuseoc ibokikkez itoputo. Febcuna neda okkein god cinhitkop topfup wimizo uneni favosca jolef der dacmar. Wa utucori fogarsib zodokuwa ogoje ikpopaj jeh ce baclatki pisbera verolide lomhozes uco fipsi oj im fil. Eske ecwu epohehes heti tik fip gokfawma ote zabwam go ig ba micati. Ele hufet ohibu jeele juhvav udih nobew mohheihi bahher pol jiw jevvi watobci jit imolenob."
        },
    "2580811517788160":
        {
            "id":"d9ed1874-8d9f-5049-9382-8834f7a45e82",
            "data":"Pafwefowo vihbek luhih igo coziculo zurva pocad bur ca wokut mivdeso bam ta giwacedu danos. Ret ba saev bikihi wuc uf hahusago zolkewago mishe kutzi buejedu ziw evatap ocmo nakgup roj evlabigo. Gid co umase tegbi ekaehajan rajodti no wugfueku omukeza coeruv iwfo le. Re ce pehen mioc etevod akwega pufbac boridsi vil zas kirif biuza fowzer. Foszo nevo pezjo sit sihno mehfiw lif dadoala lahutge wa ud owojef."
        }
          }

print("\n What type of variable is complex? ",type(nested_dict))
print("\n Original data in data file: ",nested_dict)

x=list(nested_dict.keys())
y=str(list(nested_dict.values())).replace('{','').replace('}','').replace(',','\n')
print("\n What type of variable is y? ",type(y))

print("\nList x: ",x)
print("\nList y: ",y)


def extract_dicts(data):
    dicts = []  # create a list to store the dictionaries we find

    # if the data is a dictionary, add it to our list
    if isinstance(data, dict):
        dicts.append(data)

    # if the data is a list or tuple, traverse its elements
    if isinstance(data, (list, tuple)):
        for item in data:
            # call our function recursively on each element
            dicts.extend(extract_dicts(item))

    return dicts

my_dicts = extract_dicts(nested_dict)

print("\n Original data in data file: ",nested_dict)

print("\n\nIs this what we need? : ",my_dicts)

print("\n\nWhat type is this? : ",type(my_dicts))
