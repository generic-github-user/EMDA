#!/usr/bin/env python
# coding: utf-8

# In[108]:


from IPython.display import JSON
import json
from pyvis.network import Network
import pathlib
import datetime


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
    
    def visualize(self, path='./graph-visualization.html'):
        self.vis = Network(notebook=True, width=800, height=800)
        rel_text = [[' '.join(a.text.split()[:3]) for a in b] for b in self.relations()]
#         print(rel_text)
        for x, y in rel_text:
            for w in [x, y]:
                self.vis.add_node(w)
            self.vis.add_edge(x, y)
        return self.vis.show(path)
    
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


# In[140]:


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
                
    def save(self, file_path):
        with open(file_path, 'w') as savefile:
            savefile.write(str(self.root))
        
    def backup(self):
        backup_dir = 'eparse_backups'
        pathlib.Path(f'./{backup_dir}').mkdir(parents=True, exist_ok=True)
        timestamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        backup_path = f'./{backup_dir}/backup_{timestamp}.emda'
        self.save(backup_path)
        return backup_path
                
maindoc = Doc(path)

# print(levels)
# JSON(json.dumps(root, default=vars))

urls = []

for l in getlinks(maindoc.root):
    if l[1] == 'wiki':
        b = f'https://en.wikipedia.org/wiki/{l[0].replace(" ", "_")}'
    else:
        b = l[1]
    urls.append(Block(b))

maindoc.root.Metadata.Links.add(urls)
# maindoc.backup()

# print(root.Metadata.Links)
# print(root)


# In[137]:





# In[105]:


maindoc.root.visualize()


# In[62]:


getlinks(root)


# In[142]:


print(maindoc.root.markdown())


# In[48]:


_


# In[ ]:




