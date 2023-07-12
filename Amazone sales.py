#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Admin\Downloads\Amazon Sale Report.csv", encoding='unicode escape')
df


# In[37]:


df.head()


# In[38]:


df.tail()


# In[43]:


df.info()


# In[45]:


df.describe( include='all')


# In[46]:


df.shape


# In[47]:


df.isnull().sum()/128976


# In[11]:


df


# In[15]:


df.isnull().sum()/128976


# In[28]:


df.shape


# In[48]:


df.isnull()


# In[49]:


df.isnull().sum()


# In[50]:


df.drop(['fulfilled-by','New','PendingS'],axis=1 , inplace=True)


# In[51]:


df.isnull().sum()


# In[52]:


df.dropna( inplace=True)


# In[53]:


df.shape


# In[56]:


df.isnull().sum()


# In[55]:


df.columns


# In[57]:


df.info()


# In[59]:


df['ship-postal-code']=df['ship-postal-code'].astype("int")


# In[60]:


df['ship-postal-code'].dtype


# In[74]:


df.rename(columns={'Qty':'Quantity'}, inplace=True)


# # Exploratory data analysis
# 

# In[72]:


ax=sns.countplot(x='Size', data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# # Groupby

# In[79]:


S_Quantity=df.groupby(['Size'], as_index= False)['Quantity'].sum().sort_values(by ='Quantity',ascending=False)


# In[80]:


sns.barplot(x='Size',y='Quantity', data=S_Quantity)


# In[82]:


sns.countplot(data=df, x='Courier Status', hue='Status')


# In[83]:


plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Courier Status', hue='Status')
plt.show()


# In[89]:


df['Category']=df['Category'].astype('str')
column_data=df['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data, bins=30, edgecolor='Black')
plt.xticks(rotation=90)
plt.show()


# 
# # #above graph show mostly customer buy t-shirt

# In[93]:


B2B_check=df['B2B'].value_counts()
plt.pie(B2B_check,labels=B2B_check, autopct='%1.1f%%')
plt.show()


# 
# # from above chart we can see mostly customers are retalers only 1 percent is B2B

# In[96]:


X_data=df['Category']
y_data=df['Size']
plt.scatter(X_data,y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter plot')
plt.show()


# In[ ]:





# In[116]:


plt.figure(figsize=(10,5))
top_10_states=df['ship-state'].value_counts().head(10)
sns.countplot(data=df[df['ship-state'].isin(top_10_states.index)], x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of state')
plt.xticks(rotation=45)
plt.show()


# # most of buyers from Maharastra state

# # Conclusion

# # this is basically define the buisness is depend on maharatsra customer and high demand of msize t-shirt
