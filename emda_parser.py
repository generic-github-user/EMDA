#!/usr/bin/env python
# coding: utf-8

# In[9]:


from IPython.display import JSON
import json


# In[18]:


# path = 'entities.edma'
# path = '../todo_july.txt'
path = './readme_source.txt'
with open(path, 'r') as file:
    content = file.read()
lines = content.splitlines()


# In[67]:


class Block:
    def __init__(self, text):
        self.text = text
        self.words = self.text.split()
        self.children = []

    def add(self, x):
        if type(x) in [list, tuple]:
            self.children.extend(x)
        else:
            self.children.append(x)
        return x
    
    def traverse(self, callback):
        return [callback(c) for c in self.children]
    
    def markdown(self, level=0):
        prefixes = ['# ', '## ', '', '- ', '', '', '']
        return self.text + '\n' + '\n'.join(prefixes[level]+c.markdown(level+1) for c in self.children)
    
#     def indent(self, n):
#         return ['\t'*n+c for c in self.children]
