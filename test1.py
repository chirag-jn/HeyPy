'''
Stuff-if,for,while,assign,do,done,condition

Requirements:
*for - variable                                              , in
           |                                                          |
            ---->  placeholder                                ----> range/sequence
*if - boolean expression 
                |
                ----> condition(s)[1 / 2] , operator-> 0/1
                                |
                                -----> boolean expression
                                                |
                                                ----> ....
*while - boolean expression
                |
                ----> condition(s)[1 / 2] , operator-> 0/1
                                |
                                -----> boolean expression
                                                |
                                                ----> ....
*variable - assignment expression
                    |
                    ----> operand            - operator -               operand
                            |                                                       |
                            --->assignment expression                 ---->assignment expression
                                |                                                           |
                                ---> ....                                                   --->.....

*Operators - [+,-,*,/,%,**,and,or,==,!]
*Basic Operands - [True,False,Number,*String,**Variable]
                    *Strings for later
                    *Variable if already defined
*High level Operands - [assignment expression,boolean epression]

Note : Use STOP to terminate a certain lvl
    
'''
class render :
    stack =[]
    
    def program(self):
        prg = ""
        tabs = 0 # to keep track of tabs (rep as "t")
        for i in render.stack :
            if i.token == "do":
                tab+=1
            elif i.token == "done":
                tab-=1
            elif i.token == "for":
                prg=prg+'\t'*tab + "for "+str(i.req[0])+" in range("+str(i.req[1][0])+","+str(i.req[1][1])+"):\n"
            elif i.token == "if":
                prg=prg+'\t'*tab +str(i.req)+" :"
                '''
                if len(i.req)==1:
                    prg=prg+'\t'*tab + "if "+str(i.req[0])+" :\n"
                else:
                    prg=prg+'\t'*tab + "if "+str(i.req[0])+" "+str(i.req[1])+" "+str(i.req[2])+" :\n"
                '''
            elif i.token == "while":
                prg=prg+'\t'*tab +str(i.req)+" :"
            elif i.token == "variable":
                prg=prg+'\t'*tab +str(i.req)+" :"
                
                
class token :
    cmd = {"for":[placeholder,span],"if":[x_boo],"while":[x_boo],"variable":[x_ass]}
     def __init__(self,s,l):
         self.token = s
         self.req = l





s = ""


















