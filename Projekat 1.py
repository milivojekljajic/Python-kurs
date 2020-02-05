#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  # import of pandas library

# In[2]:


from matplotlib import pyplot as plt  # import of matplotlib library

# In[3]:


import numpy as np  # import of numpy library

# In[4]:


df = pd.read_csv("/home/glooscap/Desktop/cbb19.csv")  # reading csv file from desktop

# In[5]:


df  # csv file

# In[6]:


# top five teams with most wons

df2 = df.sort_values(by="W", ascending=0)  # sorting values
df3 = df2[ :5 ]  # index for first five teams
df3[ [ "TEAM", "W" ] ]  # two colums

# In[7]:


# bar-chart for top five teams with most wons

x = df3[ "TEAM" ]
y = df3[ "W" ]
plt.bar(x, y)
plt.show()

# In[8]:


# top five teams with least played games

df6 = df.sort_values(by="G")
df7 = df6[ :5 ]
df7[ [ "TEAM", "G" ] ]

# In[9]:


# bar-chart for top five teams with least played games

x = df3[ "TEAM" ]
y = df3[ "G" ]
plt.bar(x, y)
plt.show()

# In[10]:


# first five teams with most wons and played games

df2 = df.sort_values(by="W", ascending=0)
df3 = df2[ :5 ]
df8 = df3[ [ "TEAM", "W", "G" ] ]  # three colums for teams, wons and played games

# In[11]:


df8

# In[12]:


# bar-chart for five teams with most wons and played games

x = df8[ "W" ]
y = df8[ "G" ]
l = df8[ "TEAM" ]

labels = l
won_games = x
played_games = y

x = np.arange(len(labels))  # the label locations
width = 0.32  # width of the labels

fig, ax = plt.subplots(figsize=(15, 8))  # size of the bar-chart
rects1 = ax.bar(x - width / 2, won_games, width, label='Wons')  # react for most wons
rects2 = ax.bar(x + width / 2, played_games, width, label='Games')  # react for most games

ax.set_ylabel('Scores')  # name of the y label
ax.set_title('Scores by wons')  # title for the bar-chart
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


# function for bar-chart
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

# plt.savefig('/home/glooscap/Desktop/five teams with most wons and played games.png')

plt.show()

# In[17]:


# 3 Points Shooting Percentage first five teams
df.sort_values(by="3P_O", ascending=0)
df3[ :5 ]
df4 = df3[ [ "TEAM", "3P_O" ] ]
df4
