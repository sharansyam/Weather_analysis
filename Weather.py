#!/usr/bin/env python
# coding: utf-8

# In[8]:


#importing pandas

import pandas as pd


# In[10]:


data = pd.read_csv(r'C:\Users\shara\Downloads\1. Weather Data.csv')


# In[11]:


data


# # How to analyze DataFrames?

# ### .head()

# In[15]:


#show first N rows in the data
data.head()


# ### .shape

# In[20]:


#to get no of rows & columns
data.shape


# ### .index

# In[21]:


#to get index of dataframe
data.index


# ### .columns

# In[23]:


#shows the name of each column
data.columns


# ### .dtypes

# In[24]:


#shows the data type of each column
data.dtypes


# ### .unique()

# In[26]:


#used to get unique values from a single column
data['Weather'].unique()


# ### .nunique()

# In[28]:


#it shows the number of unique values in each column
data.nunique()


# ### .count()

# In[34]:


#it shows the total no of non- null values in each column
data.count()


# ### .value_counts()

# In[35]:


#In a column, it shows all the unique values with their count, it can be applied on a single column only
data['Weather'].value_counts()


# ### .info()

# In[36]:


#Provides the basic information about the dataframe
data.info()


# # 1)Find all the unique "Wind Speed" values in the data.

# In[37]:


data.head(2)


# In[41]:


data['Wind Speed_km/h'].nunique()


# In[42]:


data['Wind Speed_km/h'].unique()


# # 2)Find the number of times in which the "Weather is exactly clear"

# In[47]:


#value_counts()
data.Weather.value_counts()


# In[44]:


#filtering
data[data.Weather == 'Clear']


# In[45]:


#groupby()
data.groupby('Weather').get_group('Clear')


# # 3)Find the number of times when the 'wind speed was exactly 4km/hr'

# In[61]:


data[data['Wind Speed_km/h']== 4]


# # 4)Find out all the null values in the data

# In[62]:


data.isnull().sum()


# In[63]:


data.notnull().sum()


# # 5)Rename the coumn name "Weather" of the dataframe to "Weather Condition"

# In[64]:


data.rename(columns = {"Weather": "Weather Condition"}, inplace = True)


# In[65]:


data


# # 6)What is the mean visibility?

# In[66]:


data.Visibility_km.mean()


# # 7)What is the standard deviation of 'Pressure' in this data?

# In[67]:


data.Press_kPa.std()


# 

# # 8)What is the variance of 'Relative Humidity' in this data?

# In[70]:


data['Rel Hum_%'].var()


# # 9)Find all instances when 'Snow' was recorded

# In[76]:


#value_counts()
data['Weather Condition'].value_counts()


# In[78]:


#filtering
data[data["Weather Condition"] == "Snow"]


# In[82]:


#all values which contain snow
#str.contains()
data[data['Weather Condition'].str.contains('Snow')]


# # 10)Find all the instances in which 'Wind speed is above 24' and 'Visibility is 25'

# In[83]:


data.head(2)


# In[89]:


data[(data['Wind Speed_km/h']> 24) & (data['Visibility_km'] == 25)]


# # 11)What is the mean value of each column against each ' Weather Condition'?

# In[96]:


data.groupby('Weather Condition').mean()


# # 12)What is the minimum & maximum value of each column aganinst each 'Weather Condition'?

# In[97]:


data.groupby('Weather Condition').min()


# In[98]:


data.groupby('Weather Condition').max()


# # 13) Show all the records where Weather Condition is Fog

# In[100]:


data[data['Weather Condition'] == 'Fog']


# # 14) Find all the instances when ' Weather is Clear' or ' Visibility is above 40'

# In[105]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km']> 40)]


# # 15) Find all instances when:
# 
# ### A. 'Weather is Clear' and ' Relative Humidity is greater than 50'
# 
# ### or
# 
# ### B. 'Visibility is above 40'

# In[110]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)]


# In[ ]:




