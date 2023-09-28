#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# In[ ]:





# In[4]:


import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


# In[9]:


st.title("Investment Protfolio Dashboard")
assets = st.text_input("Provide your assests (comma-separated)","AAPL,MSFT,GOOGL")
start = st.date_input("Pick a starting date for your analysis",
                     value = pd.to_datetime('2022-06-01'))
data = yf.download(assets,start = start)['Adj Close']


# In[10]:


data


# In[11]:


ret_df = data.pct_change()


# In[12]:


cumul_ret = (ret_df + 1). cumprod() - 1
pf_cumul_ret = cumul_ret.mean(axis = 1)


# In[13]:


cumul_ret


# In[14]:


pf_cumul_ret


# In[15]:


benchmark = yf.download('^GSPC',start = start)['Adj Close']
bench_ret = benchmark.pct_change()
bench_dev = (bench_ret + 1).cumprod() - 1


# In[16]:


bench_dev


# In[18]:


W = (np.ones(len(ret_df.cov()))/len(ret_df.cov()))
pf_std = (W.dot(ret_df.cov()).dot(W)) ** (1/2)


# In[19]:


W


# In[20]:


ret_df.cov()


# In[21]:


st.subheader("Portfolio vs. Index Development")
tog = pd.concat([bench_dev,pf_cumul_ret],axis = 1)
tog.columns = ['S&P500 Performance','Portfolio Performance']


# In[22]:


tog


# In[24]:


st.line_chart(data = tog)


# In[25]:


st.subheader("Portfolio Risk:")
pf_std
st.subheader("Benchmark Risk:")
bench_risk = bench_ret.std()
bench_risk


# In[27]:


st.subheader("Portfolio composition:")
fig, ax = plt.subplots(facecolor = '#121212')
ax.pie(W,labels = data.columns, autopct = '%1.1f%%',textprops={'color': 'white'})
st.pyplot(fig)


# In[ ]:




