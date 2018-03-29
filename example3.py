user = "b2aca159-86a0-4afa-9b22-4b720ee1957f"
passwd = "vTSl6VKjZMPA"

#from watson import watson_run
from test2 import parse

cmd = [
"assign variable u with variable n plus three raised to the power variable s",
"assign variable v with three hundred ",
"function print four hundred and twenty",
"create a for loop of variable j till three million",
"create an if statement whre variable a greater than variable c and variable d or variable f not equal to nine",
"create a while loop where variable i less than equal to zero",
"function print variable i minus ten",
"assign variable i with variable i divided by two",
"done",
"done",
"create else",
"create if not of variable q",
"function print variable p mod variable p plus variable j into variable r",
"done",
"create else",
"pass",
"done",
"done",
"create a for loop with variable zz ranging form eleven to variable q",
"create if thirteen raiised to the power variable zz less than variable m",
"pass",
"done",
"done",
"done"

]
from time import sleep
for i in cmd:
    print(i)
    parse(i)
    sleep(1)
