
# coding: utf-8

# # Rising inequality but everyone is better of: Armenia edition

# #### This is my first project with Python. My goal is to explore the data, and answer the question if the wage gap among different industries is increasing in Armenia.
# 
# 
# The data is acquired from the Statistical Committee of Armenia. The industry sectors are previously translated English and AMD is converted to USD as of 8/3/2018 when USD=481AMD, done using Excel. The table shows the mean salaries for different industries of Armenia from 2009 to 2016. 

# ## Preparing the Data 
# 

# In[1]:


import pandas as pd


# In[2]:


get_ipython().system('ls ')


# In[3]:


get_ipython().system('head ./PS-eu-19.csv')
#Some exploration of the Data


# In[10]:


industries = pd.read_csv('./PS-eu-19.csv', sep='\t')
#Importing the csv file as a DataFrame


# In[21]:


industries.head()


# In[12]:


industries = industries.drop(['Unnamed: 10', 'Unnamed: 11', '2012*', '2013**', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21'],   axis=1)
#Dropping extra columns


# In[13]:


industries=industries.set_index('Unnamed: 0')
#Setting the indices to be the the names of industry column


# ## Exploring the data

# In[22]:


industries.describe()


# In[24]:


transpose=industries.transpose()
transpose.describe()


# ## Visualizing the data

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[16]:


industries.boxplot(figsize=(9,12))


# Here we can see that the mean salary overall is increasing when taken together over these years.

# In[36]:


means=transpose.mean()
vc=means.values
means=pd.Series.sort_values(means)
indices=means.index


# In[70]:


industries=industries.set_index(vc)
industries_sorted=industries.sort_index(ascending=True)
#sorting the table for further analysis


# In[64]:


industries_sorted=industries_sorted.set_index(indices)


# In[74]:


# Create a figure instance
fig = plt.figure(figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(1, 1, 1)


# Create the boxplotindex
bp = ax.boxplot(industries_sorted, labels= indices)

plt.xticks(rotation=90)


# This plot shows how the mean salaries differ depending on the sector, but it does not show if the difference has increased over these years or not.

# In[75]:


transpose=industries_sorted.transpose()
sd=transpose.std()


# In[69]:



sector = sd.index
# get the values 
var = sd.values

# create
plt.bar(sector, var, label=sector)
plt.xticks(rotation=90)
plt.show()


# The standard deviation of sectors gives us an idea how much there was an increase over these years in different sectors. The higher the standard deviation the higher is the increase.

# In[46]:


sd2=industries.std()
sd2

# get the years
years = sd2.index.values
years
# get the values 
variety= sd2.values

# create
plt.bar(years,variety)
plt.show()


# The standard deviation of years shows the variability among different sectors in different years. The higher the standard deviation, the more is the difference among sectors and the more is the inequality. 

# #### As a conclusion, there has clearly been an increase in salaries overall, but it is not equal in all sectors and the wage gap is increasing.
