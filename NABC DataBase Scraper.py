#!/usr/bin/env python
# coding: utf-8

# In[35]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


# In[36]:


import os
import wget


# In[37]:


driver = webdriver.Firefox('/usr/local/bin')


# In[38]:


driver.get('https://cliffbarackman.com/forum/')


# In[39]:


username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="username"]')))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="password"]')))
username.clear()
password.clear()
username.send_keys()
password.send_keys()


# In[ ]:




