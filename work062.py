#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 09:47:00 2018

@author: davidxiong
"""

class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self,item):
        self.queue.insert(0,item)
        
    def front(self):
        return self.queue[0]
    
    def pop(self):
        return self.queue.remove(self.queue[0])
    
    def back(self):
        return self.queue[-1]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def get(self):
        return self.queue
    
a = Queue()
a.push(4)
a.push(3)
a.push(2)
a.push(1)
a.pop()
print(a.isEmpty())
print(a.back())
print(a.front())
print(a.get())

    
