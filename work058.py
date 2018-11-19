#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:13:04 2018

@author: davidxiong
"""



class Stack():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
    def get(self):
        return self.items
    
    def reverse_stack(self):
       
        listt=[]
        while len(self.items)>0:
            listt.append(self.items[-1])
            self.items.remove(self.items[-1])
        return listt
    
    def parChecker(self,string):
        string = list(string)
        index = 0
        n = 0
        j = 0
        while index<len(string):
           
            if string[index] == "(":
                n+=1
            elif string[index] == ")":
                j+=1
            index +=1
        if n==j:
            return True
        else:
            return False
 
    def convert_binary(self,number):
        s = Stack()
        while number>0:
            s.push(number%2)
            number = number//2
        result = ""
        while not s.isEmpty():
            result = result + str(s.pop())
        return eval(result)
    
    def convert_everything(self,system,number):
        index = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        s = Stack()
        while number >0:
            s.push(index[number%system])
            number = number//system
        result = ""
        while not s.isEmpty():
            result+= s.pop()
        return result
    
    def every_system(self,system1,system2,number):
        """
        system 进制
        system1: the system of your input number
        system2: the system of what you want to get
        Number has to be in the type of string
        """
        s = Stack()
        temp = s.convert_decimal(system1,number)
        result = s.convert_everything(system2,temp)
        return result
    
    def convert_decimal(self,system,number):
        """
        number has to be in decimal
        """
        listt = []
        index = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        for i in range(len(number)):
            counter = index.index(number[i])
            listt.append(counter*(system**(len(number)-i-1)))
        summ = sum(listt)
        return summ
   
    def postfix_evaluation(self,s):
        listt = []
        tokenlist = s.split()
        symbol_list = ["+","-","*","/"]
        for i in tokenlist:
            if i in symbol_list:
                if str(i) == "+":
                    result = int(listt.pop())+int(listt.pop())
                    listt.append(result)
                elif str(i) == "-":
                    result = int(listt.pop())-int(listt.pop())
                    listt.append(result)
                elif str(i) == "*":
                    result = int(listt.pop())*int(listt.pop())
                    listt.append(result)
                elif str(i) == "/":
                    result = int(listt.pop())/int(listt.pop())
                    listt.append(result)
            else:
                listt.append(i)
        return listt.pop()

                    
        
            
      
s = Stack()

#print(s.isEmpty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.isEmpty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())
#print(s.get())
#s.push(5)
#print(s.isEmpty())
#print(s.get())
#print(s.reverse_stack())
#abc = "()"
#print(s.parChecker(abc))
#print(s.diff_parChecker(abc))
#print(s.convert_binary(10))
#print(s.convert_everything(16,100))
#print(s.every_system(16,2,"B7"))
#print(s.convert_decimal(2,"10101101110"))
print(s.postfix_evaluation('10 2 8 * + 3 -'))



    
    
        
