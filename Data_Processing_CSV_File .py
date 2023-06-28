#!/usr/bin/env python
# coding: utf-8

# # Importing Pandas

# In[22]:


import pandas as pd


# # Opening a Local CSV Files

# In[23]:


df=pd.read_csv('aug_train.csv')
df


# # Opening a csv file from an URL

# In[24]:


import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)



# # Sep Parameter

# In[25]:


pd.read_csv('movie_titles_metadata.tsv',sep='\t')


# In[26]:


pd.read_csv('movie_titles_metadata.tsv',sep='\t',names=['Sno','Name','Release_Year','Rating','Votes','Genres'])


# # Index_Col Parameter

# In[27]:


pd.read_csv('aug_train.csv',index_col='enrollee_id')


# # Header Parameter

# In[28]:


pd.read_csv('test.csv',header=1)


# # use_cols parameter

# In[29]:


pd.read_csv('aug_train.csv',usecols=['enrollee_id','gender','education_level'])


# # Squeeze Parameters

# In[30]:


pd.read_csv('aug_train.csv',usecols=['enrollee_id'],squeeze=True)


# # Skiprows/nrows Parameter 

# In[31]:


pd.read_csv('aug_train.csv',skiprows=[0,2])


# In[32]:


pd.read_csv('aug_train.csv',nrows=100)


# # Encoding Parameter

# In[33]:


pd.read_csv('zomato.csv',encoding='latin-1')


# # Skip Bad Lines

# In[15]:


pd.read_csv('BX-Books.csv',sep=';',encoding='latin-1',error_bad_lines=False)


# # Dtypes Parameter

# In[16]:


pd.read_csv('aug_train.csv').info()


# In[18]:


pd.read_csv('aug_train.csv',dtype={'target':int})


# # Handling Dates

# In[39]:


pd.read_csv('IPL Matches 2008-2020.csv',parse_dates=['date'])


# # Convertors

# In[41]:


pd.read_csv('IPL Matches 2008-2020.csv')


# In[42]:


def rename(name):
    if name=='Royal Challengers Bangalore':
        return "RCB"
    else:
        return name


# In[43]:


rename("Royal Challengers Bangalore	")


# In[46]:


pd.read_csv('IPL Matches 2008-2020.csv',converters={'team1':rename})


# # na_values parameters

# In[47]:


pd.read_csv('aug_train.csv',na_values=['Male'])


# # Loading a huge dataset in chunks

# In[53]:


dfs=pd.read_csv('aug_train.csv',chunksize=5000)


# In[54]:


for chunks in dfs:
    print(chunk.shape)


# In[ ]:




