#tasks-assign,create,function  {1,2,3}
task=0

stack=[]
variables=[]
operator={"plus":"+","minus":"-","into":"*","divide":"/","mod":"%","or":"or","and":"and","not":"!"}
blocks=["if","while","for"]

class token :
    
     def __init__(self,s,l):
         self.token = s
         self.req = l

while True:
    sent = cmd.lower().split(" ")
    #assign
    nextval=0
    nextassignee=0
    assignedflag=0
    
    #create
    subtask=0#1-for,2-if ,3-while
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
        elif i=="assign":
            task=1
        elif i=="create":
            task=2
        elif i=="function":
            task=3
            stack.aapend(token("print",[]))
        elif task==1:
            if i=="variable":
                nextassignee=1
            if nextassignee==1:
                nextassignee=0
                stack.append(token("var",i))
            elif i=="to":
                assignedflag=1
            if assignedflag==1:
                
                if nextval==1:
                    assigned+=i
                    nextval=0
                elif i in operator:
                    assigned+=operator[i]
                elif type(i)==int or type(i)==float:
                    assigned+=str(i)

                if i=="variable":
                    nextval=1
                if count==(len(sent)):
                    temp=stack[-1].req
                    stack[-1].req=[temp,assigned]
                    assigned=""
                    stack.append('[')
        elif task==2:
            
            if subtask==1:
                if nextvar==1 and i=="variable":
                    nextval=1
                    nextvar=0
                elif nextval==1:
                    nextval=0
                    stack[-1].req=[i]
                    st=1
                elif st==1 and (type(i)==int or type(i)==float ) :
                    stack[-1].req.append("i")
                    st=0
                    end=1
                elif st==1 and nextval==1 :
                    stack[-1].req.append(i)
                    st=0
                    end=1
                    nextval=0
                elif st==1 and (i=="variable" ) :
                    nextval=1
                elif end==1 and (type(i)==int or type(i)==float ) :
                    stack[-1].req.append("i")
                    end=0
                elif end==1 and nextval==1 :
                    stack[-1].req.append(i)
                    end=0
                    nextval=0
                    stack.append('[')
                elif end==1 and (i=="variable" ) :
                    nextval=1

            elif subtask==2:
                if nextvar==1 and i=="variable":
                    nextval=1
                    nextvar=0
                if nextval==1:
                    assigned+=i
                    nextval=0
                    nextvar=1
                elif i in operator:
                    assigned+=operator["i"]
                if count==(len(sent)):
                    stack[-1].req.append(assigned)
                    assigned=""
                    stack.append('[')

            elif subtask==3:
                if nextvar==1 and i=="variable":
                    nextval=1
                    nextvar=0
                if nextval==1:
                    assigned+=i
                    nextval=0
                    nextvar=1
                elif i in operator:
                    assigned+=operator["i"]
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
                    stack.append(token("if",[]))
                elif i=="while":
                    nextvar=1
                    subtask=3
                    stack.append(token("while",[]))
        elif task==3:
            if nextvar==1 and i=="variable":
                nextval=1
                nextvar=0
            if nextval==1:
                assigned+=i
                nextval=0
                nextvar=1
            elif i in operator:
                assigned+=operator["i"]
            if count==(len(sent)):
                stack[-1].req.append(assigned)
                assigned=""
    task=0
