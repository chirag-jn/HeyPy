from parser_for_numbers import parse_nums
from parser_for_booleanOps import parse_bool
#tasks-assign,create,function  {1,2,3}
task=0

stack=[]
variables=[]
operator={"plus":"+","minus":"-","into":"*","power":"**","multiplied":"*","divided":"/","divide":"/","mod":"%","modulus":"%","or":"or","and":"and","not":"!","gt":">","lt":"<","gte":">=","lte":"<=","eq":"==","ne":"!="}
blocks=["if","while","for","else","elif"]

class token :
	
	 def __init__(self,s,l):
		 self.token = s
		 self.req = l

def program():
	prg = ""
	tab = 0 # to keep track of tabs (rep as "t")
	# import os
	# os.rename('finalcode.py', 'temp.txt')
	with open('finalcode.py', 'w') as t:
		# with open('finalcode.txt')
		for i in stack :
			if i == "[":
				tab+=1
			elif i == "]":
				tab-=1
			elif i == "pass":
				prg=prg+'\t'*tab+i+"\n"
			elif i.token == "for":
				if len(i.req)==3:
					prg=prg+'\t'*tab + "for "+str(i.req[0])+" in range("+str(i.req[1])+","+str(i.req[2])+"):\n"
				elif len(i.req)==2:
					prg=prg+'\t'*tab + "for "+str(i.req[0])+" in range("+str(i.req[1])+"):\n"
			elif i.token == "if":
				prg=prg+'\t'*tab+ "if " +str(i.req[0])+" :\n"
			elif i.token == "else":
				prg=prg+'\t'*tab+ "else" +" :\n"
			elif i.token == "while":
				prg=prg+'\t'*tab+ "while " +str(i.req[0])+" :\n"
			elif i.token == "var":
				prg=prg+'\t'*tab +str(i.req[0])+" = "+str(i.req[1])+"\n"
			elif i.token == "print":
				prg=prg+'\t'*tab +"print( "+str(i.req[0])+")\n"
		# print(prg)
		t.write(prg)
		t.close()
	# os.rename('temp.txt', 'finalcode.py')

cmd = ["assign variable b with 6",
"assign variable a with 5",
"create for loop of variable i from 1 to 2",
"create if variable b gt variable a",
"assign variable a with variable a plus variable b",
"done",
"create else",
"assign variable a with variable a minus variable b",
"done",
"create while variable a gt variable b",
"function variable a",
"assign variable a with variable a minus 1",
"done",
"done"
]
# ind=0
# while ind<14:
def parse(cmd):
	cmd = parse_nums(cmd)
	cmd = parse_bool(cmd)
	#print("parsed " + cmd)
	task = 0
	sent = cmd.lower().split(" ")
	#assign
	nextval=0
	nextassignee=0
	assignedflag=0
	
	#create
	subtask=0#1-for,2-if ,3-while,4-else,5-elif
	nextvar=0
	nextval=0
	st=0
	end=0
	#function

	assigned=""
	count=0
	for i in sent:
		count+=1
		if i=="done":
			stack.append(']')
		elif i=="pass":
			stack.append('pass')
		elif i=="assign":
			task=1
		elif i=="create":
			task=2
		elif i=="function":
			task=3
			stack.append(token("print",[]))
			nextvar=1
		elif task==1:
			if nextassignee==1:
				nextassignee=0
				stack.append(token("var",i))
			elif i=="with":
				assignedflag=1

			if i=="variable" and assignedflag==0:
				nextassignee=1
			
			if assignedflag==1:
				
				if nextval==1:
					assigned+=i
					nextval=0
				elif i in operator:
					assigned+=operator[i]
				elif i.isdigit() :
					assigned+=str(i)

				if i=="variable":
					nextval=1
				if count==(len(sent)):
					temp=stack[-1].req
					stack[-1].req=[temp,assigned]
					assigned=""
					assignedflag=0
					#stack.append('[')
		elif task==2:
			
			if subtask==1:
				if nextvar==1 and i=="variable":
					nextval=1
					nextvar=0
				elif st==1 and nextval==1 :
					stack[-1].req.append(i)
					st=0
					end=1
					nextval=0
				elif end==1 and nextval==1 :
					stack[-1].req.append(i)
					end=0
					nextval=0
					#stack.append('[')
				elif nextval==1:
					nextval=0
					stack[-1].req=[i]
					st=1
				elif st==1 and (i.isdigit() ) :
					stack[-1].req.append(str(i))
					st=0
					end=1

				elif end==1 and (i.isdigit() ) :
					stack[-1].req.append(str(i))
					end=0
					#stack.append('[')
				elif st==1 and i=="variable" :
					nextval=1
				
				elif end==1 and (i=="variable" ) :
					nextval=1

				if count==(len(sent)):
					stack.append('[')

			elif subtask==2:
				if nextval==1:
					assigned+=i
					nextval=0
					nextvar=1
				elif i in operator:
					assigned+=operator[i]
				elif i.isdigit():
					assigned+=str(i)
				if nextvar==1 and i=="variable":
					nextval=1
					nextvar=0
				if count==(len(sent)):
					stack[-1].req.append(assigned)
					assigned=""
					stack.append('[')

			elif subtask==3:
				if nextval==1:
					assigned= assigned + i + " "
					nextval=0
					nextvar=1
				elif i in operator:
					assigned= assigned + operator[i] + " "
				elif i.isdigit():
					assigned= assigned + str(i) + " "
				if nextvar==1 and i=="variable":
					nextval=1
					nextvar=0
				if count==(len(sent)):
					stack[-1].req.append(assigned)
					assigned=""
					stack.append('[')

			elif i in blocks:
				stack.append(token(i,[]))
				if i=="for":
					nextvar=1
					subtask=1
				elif i=="if":
					nextvar=1
					subtask=2
					#stack.append(token("if",[]))
				elif i=="while":
					nextvar=1
					subtask=3
					#stack.append(token("while",[]))
				elif i=="else":
					nextvar=1
					subtask=4
					#stack[-1].req.append(i)
					stack.append('[')

		elif task==3:
			if nextvar==1 and i=="variable":
				nextval=1
				nextvar=0
			elif nextval==1:
				assigned+=i
				nextval=0
				nextvar=1
			elif i in operator:
				assigned+=operator[i]
			elif i.isdigit() :
				 assigned+=str(i)
			if count==(len(sent)):
				stack[-1].req.append(assigned)
				assigned=""
	task=0
	# if ind==(len(cmd)-1):
	# 	for i in stack:
	# 		if i == "[" or i=="]":
	# 			print (i)
	# 		else:
	# 			print (i.token,i.req)
	# ind+=1
	program()