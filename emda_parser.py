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
    
    def tostring(self, l=0):
        return self.text + ''.join(['\n'+('\t'*l)+c.tostring(l+1) for c in self.children])
    
    def find(self, name):
        return list(filter(lambda x: x.text == name, self.children))
    
    def __str__(self):
        return self.tostring()
    
    def __getattr__(self, name):
        nodes = self.find(name)
        if nodes:
            return nodes[0]
        else:
            return self.add(Block(name))
        
def getlinks(node):
    links = []
    for w in node.words:
        if '$' in w:
            links.append(w.split('$'))
    for c in node.children:
        links.extend(getlinks(c))
    return links
        
root = Block('')
levels = {0: root}
for line in lines:
    content = line.lstrip()
    if content:
        tabs = len(line) - len(content)
        lblock = Block(content)
        levels[tabs+1] = lblock
        levels[tabs].add(lblock)

# print(levels)
# JSON(json.dumps(root, default=vars))

root.Metadata.Links.add([Block(l[1]) for l in getlinks(root)])
print(root.Metadata.Links)
print(root)


# In[62]:


getlinks(root)


# In[43]:


print(root.markdown())


# In[48]:


_


# In[ ]:




