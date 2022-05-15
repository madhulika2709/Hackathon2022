#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pycountry


# In[2]:


import pycountry

input_countries = ['France']
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2
codes = [countries.get(country,'Unknow Code') for country in input_countries]
print(codes)


# In[3]:


get_ipython().system('pip install goslate')


# In[4]:


import goslate

text = "good night"

gs = goslate.Goslate()
outp=gs.translate(text,'FR')
print(outp)


# In[ ]:




