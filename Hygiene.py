#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In this file I'll clean the different files. 
#Then I'll evaluate the potential relations among the records.


# In[2]:


#import import_ipynb
import pandas as pd
pd.set_option('display.max_columns', None)

import numpy as np

import warnings
warnings.filterwarnings('ignore')

#Wenders level 4K graphics.
import pylab as plt
import seaborn as sns

#This make the graph possible
get_ipython().run_line_magic('matplotlib', 'inline')

#Functions
from src.funk import Funk 


# In[3]:


##A general overview has already been done on the raw csv files.
#I'll start by dropping update columns and language related data since there are only english spoken content. 


# In[4]:


#Loading data

actor = pd.read_csv('data/actor.csv', encoding= "ISO-8859-1")
category = pd.read_csv('data/category.csv', encoding= "ISO-8859-1")
film = pd.read_csv('data/film.csv', encoding= "ISO-8859-1")
inventory = pd.read_csv('data/inventory.csv', encoding= "ISO-8859-1")
old_HDD = pd.read_csv('data/old_HDD.csv', encoding= "ISO-8859-1")
rental = pd.read_csv('data/rental.csv', encoding= "ISO-8859-1")


# In[5]:


del actor['last_update']
del category['last_update']
del inventory['last_update']
del rental['last_update']


# In[6]:


film.drop(['language_id', 'original_language_id', 'last_update'], axis=1, inplace=True)


# In[7]:


#Dataframes were checked for null values, they seem clean.
#All the info in them seems useful, time to relate it and build a database.
#actor.shape 200,3
#category.shape 16,2
#film.shape 1000,10
#inventory.shape 1000,3
#old_HDD.shape 1000,5
#rental.shape 1000,6


# In[8]:


#From a quick overview and my assumption I can relate 2 general groups of info:

#Given_data, as in actor, category and film. This data is true regardless of the business, and won't change.
#Created__data as in inventory, old_HDD and rental. This is business history, and will fluctuate ahead.
#Probably as of now, film and inventory are matching, since both have 1K records. 
#The zip among those two could very well be the bridge for all data.

#Drawing time. 


# In[9]:


#Contrary of the initial thought, film cannot relate category and actor.

#inventory shows there are two stores, each with half the movies.
#inventory also shows there are 1000 dvds, but only 207 unique titles.

#rental shows that the staff counts 2 entities, each renting more or less half the volume.
#rental shows there are 485 customers, they have rented in a range 8 to 1, 75% of them have rented less than 3.

#oldHDD will just be merged with film and that will be the database core.


# In[10]:


actor['name'] = actor['first_name'] +' '+ actor['last_name']
old_HDD['name'] = old_HDD['first_name'] +' '+ old_HDD['last_name']
actor.drop(['first_name', 'last_name'], axis=1, inplace=True)
old_HDD.drop(['first_name', 'last_name'], axis=1, inplace=True)


# In[11]:


#film has 1000 unique id and title
#old_HDD has 614 unique title, 39 unique actor name
#from old_HDD, film is missing the category.
#old_HDD will be used to create the new table with film_id and actor_id

film2 = pd.merge(film, old_HDD, how="left", on=["title"])
film2.drop(['release_year_y', 'name'], axis=1, inplace=True)
film2 = film2.drop_duplicates()
old_HDD.drop(['release_year', 'category_id'], axis=1, inplace=True)


# In[12]:


tit_id = film[['film_id', 'title']]
act_id = actor[['actor_id', 'name']]

merg1 = pd.merge(old_HDD, tit_id, how="left", on=["title"])
merg2 = pd.merge(merg1, act_id, how="left", on=["name"])
merg2.drop(['title', 'name'], axis=1, inplace=True)
title_actor = merg2.drop_duplicates()

#614 unique title achieved, the one with more actors has 6, the less 1
#39 unique actors, the one on more titles is on 37, the less on 7
#title_actor['film_id'].value_counts()
#title_actor['actor_id'].value_counts()


# In[13]:


cinefilo = rental.customer_id.value_counts()
stats = cinefilo.describe()
stats['IQR'] = stats['75%'] - stats['25%']
#stats


# In[14]:


film2.info()


# In[15]:


#Data cleaning seams ready, the next file will construct the database.
#Exporting data


# In[16]:


category.to_csv('data/category_clean.csv', index=False)
actor.to_csv('data/actor_clean.csv', index=False)
rental.to_csv('data/rental_clean.csv', index=False)
inventory.to_csv('data/inventory_clean.csv', index=False)
film2.to_csv('data/film_clean.csv', index=False)
title_actor.to_csv('data/title_actor.csv', index=False)

