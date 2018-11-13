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
        a = Stack()
        balanced = True
        index = 0
        while index< len(string) and balanced:
            symbol = string[index]
            if symbol == "(":
                a.push(symbol)
            else:
                if a.isEmpty():
                    balanced = False
                else:
                    a.pop()
            index+=1
        if balanced and a.isEmpty():
            return True
        else:
            return False
                
                
        
                     
        
            
        
            
        
        
    


    
s = Stack()

#print(s.isEmpty())
s.push(4)
s.push('dog')
#print(s.peek())
s.push(True)
#print(s.size())
#print(s.isEmpty())
s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())
#print(s.get())
#print(s.isEmpty())
#print(s.get())
print(s.reverse_stack())



    
    
        
