#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd 
import matplotlib.pyplot as plt


# In[43]:


df = pd.read_excel(r'C:\Users\acamp\Downloads\IHME_USA_COUNTY_RESP_DISEASE_MORTALITY_1980_2014_NATIONAL_XLSX (1)\IHME_USA_COUNTY_RESP_DISEASE_MORTALITY_1980_2014_NATIONAL_Y2017M09D26.XLSX', sheet_name='Chronic respiratory diseases')


# In[44]:


df.columns = ['Location', 'FIPS', 'Mortality Rate, 1980', 'Mortality Rate, 1985', 'Mortality Rate, 1990', 'Mortality Rate, 1995', 'Mortality Rate, 2000', 'Mortality Rate, 2005', 'Mortality Rate, 2010', 'Mortality Rate, 2014', '% Change in Mortality Rate, 1980-2014']


# In[45]:


df = df.iloc[1: , :]


# In[46]:


df = df.dropna(subset=['FIPS'])


# In[47]:


df['FIPS'] = df['FIPS'].astype(int)


# In[48]:


df = df.loc[df['FIPS'] <= 56]


# In[49]:


df.head(10)


# In[19]:


years = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2014]


# In[90]:


plt.figure(figsize=(25,25))
for rowIndex, row in df.loc[ : , 'Location':'Mortality Rate, 2014'].iterrows():
    state = ''
    results = []
    for columnIndex, value in row.items():
        if columnIndex == df.columns[0]:
            state = value
        elif columnIndex != df.columns[1]:
            result = value
            result = float(result[:result.find('(')])
            results.append(result)
    plt.plot(years, results, label=state, marker='o') 
    
    
plt.legend()
plt.show()





