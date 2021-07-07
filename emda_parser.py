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
