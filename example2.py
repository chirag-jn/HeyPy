user = "b2aca159-86a0-4afa-9b22-4b720ee1957f"
passwd = "vTSl6VKjZMPA"

#from watson import watson_run
from test2 import parse

cmd = [
"assign variable abc with variable xyz plus three mod seventeen",
"create a for loop of variable j from one to hundred",
"create an if statement whre variable a greater than variable c ",
"create a while loop where variable i greater than equals three",
"function print variable i raised to the power variable i",
"assign variable i with variable i minus one",
"done",
"done",
"create else",
"create if variable p less than variable r",
"function print variable p modulus variable r",
"done",
"create else",
"pass",
"done",
"done",
"done",

]
from time import sleep
for i in cmd:
    print(i)
    parse(i)
    sleep(1)
