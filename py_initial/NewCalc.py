import re
print("Calculator","\nType 'quit' to exit")

run=True
previous=0

def operation():
    global run
    global previous
    equation=""
    if previous==0:
        equation=input("\nEnter problem to be solved:")
    else:
        equation=input(str(previous))

    if equation == 'quit':
        print("\nBye, have a nice time ahead")
        run = False
    else:
        equation=re.sub('[a-zA-Z,.:()" "]','',equation)

    if previous == 0:
        previous=eval(equation)
    else:
        previous=eval(str(previous)+equation)

while run:
    operation()




