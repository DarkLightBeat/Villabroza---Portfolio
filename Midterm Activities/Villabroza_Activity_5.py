#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

dataset = pd.read_csv('suicide.csv')

dataset.iloc[:,[0,1,2,3,6]]


# In[2]:


dataset.iloc[:,[0,1,2,3,4,6]][dataset.country.isin(['Philippines'])]


# In[4]:


dataset.iloc[:, [0, 1, 2, 3, 4, 6]][(dataset['country'] == 'Philippines') & (dataset['year'] == 2011)]


# In[5]:


x = dataset[(dataset.year == 2005)][['country', 'year', 'sex', 'age', 'suicides/100k pop']]
x[x['suicides/100k pop'] == max(x['suicides/100k pop'])]


# In[6]:


import numpy as np

x = dataset.groupby(by='year')[['suicides_no', 'suicides/100k pop']].agg(sum)

x.sort_values(by='suicides_no', ascending = [False])


# In[7]:


import numpy as np

x = dataset.groupby(by='sex')[['suicides_no', 'suicides/100k pop']].agg(sum)

x.sort_values(by='suicides_no', ascending = [False])


# In[8]:


import numpy as np

x = dataset.groupby(by='age')[['suicides_no', 'suicides/100k pop']].agg(sum)

x.sort_values(by='suicides_no', ascending = [False])


# In[9]:


import numpy as np

x = dataset.groupby(by=['country', 'year']) [['suicides_no']].agg(sum)

x.sort_values(by='suicides_no', ascending = [False])


# In[10]:


import numpy as np

total = dataset.groupby(['sex', 'year', 'age']).agg({'suicides_no':'sum'})
display(total)


# In[11]:


total = dataset.groupby(['sex', 'year', 'age']).agg({'suicides_no':'sum'}).sort_values(by='suicides_no', ascending=False).iloc[0]

print(total)


# In[ ]:
