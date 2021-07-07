#!/usr/bin/env python
# coding: utf-8

# In[61]:


from IPython.display import JSON
import json
from pyvis.network import Network


# In[103]:


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
    
#     def collect(self):
#         collected = Block('')
#         collected.add(self.traverse(lambda a: a))
#         collected = []
#         for c in self.children:
#             print(c.collect())
#             collected.extend([[d.text, c] for a, d in c.collect()])
#         return collected
    
    def markdown(self, level=0):
        prefixes = ['# ', '## ', '', '- ', '', '', '']
        return self.text + '\n' + '\n'.join(prefixes[level]+c.markdown(level+1) for c in self.children)
    
#     def indent(self, n):
#         return ['\t'*n+c for c in self.children]
    
    def tostring(self, l=0):
        return self.text + ''.join(['\n'+('\t'*l)+c.tostring(l+1) for c in self.children])
    
    def find(self, name):
        return list(filter(lambda x: x.text == name, self.children))
    
    def relations(self):
        rlist = []
        for c in self.children:
#             print(c.relations())
            rlist.append([self, c])
#             rlist.extend([[c, t] for t, r in c.relations()])
            rlist.extend(c.relations())
        return rlist
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


# In[104]:


# path = 'entities.edma'
# path = '../todo_july.txt'
path = './readme_source.txt'
class Doc:
    def __init__(self, source):
        self.source = source
        with open(self.source, 'r') as source_file:
            self.content = source_file.read()
        self.lines = self.content.splitlines()
        
        self.root = Block('')
        self.levels = {0: self.root}
        for line in self.lines:
            content = line.lstrip()
            if content:
                tabs = len(line) - len(content)
                lblock = Block(content)
                self.levels[tabs+1] = lblock
                self.levels[tabs].add(lblock)
                
maindoc = Doc(path)

# print(levels)
# JSON(json.dumps(root, default=vars))

maindoc.root.Metadata.Links.add([Block(l[1]) for l in getlinks(maindoc.root)])
# print(root.Metadata.Links)
# print(root)


# In[62]:


getlinks(root)


# In[43]:


print(root.markdown())


# In[48]:


_


# In[ ]:




