#!/usr/bin/env python
# coding: utf-8

# In[68]:


import re

x = open("regex_sum_42.txt")
c = 0
g = 0
j = 0
num_list = []

for i in x:
    i = i.rstrip()
    if re.search("^Python+", i):
        print(i)
        

    a = re.findall(r"\d+", i)
    for b in a:
        c = c + int(b)
        num_list.append(int(b))
        

    d = re.findall(r"[aeiouAEIOU]+", i)
    for e in d:
        for f in e:
            g = g + 1
            
   
    h = re.findall("Python", i)
    for i in h:
        j = j + 1

print()
print("The sum of all numbers is", c)
print("The highest number is",max(num_list))
print("The total vowel count is", g)
print("Python word count is", j)

