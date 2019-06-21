#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # decisiontree classifier only


# In[13]:


#here smooth is for apple and bumpy is for orange
# this is for apple and orange
features=[[100,"0"],[120,"0"],[130,"1"],[150,"1"]]
## here 0 means smooth and 1 means bumpy


# In[14]:


#now answers accordingly
label=["apple","apple","orange","orange"]


# In[15]:


# calling decisiontree classifier
clf=DecisionTreeClassifier()


# In[16]:



# now time for training data
trained=clf.fit(features,label)


# In[22]:


trained.predict([[123,1]])



# In[ ]:




