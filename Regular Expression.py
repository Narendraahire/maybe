#!/usr/bin/env python
# coding: utf-8

# # Regular Expression

# In[3]:


import re         # Here you import the regression


# In[4]:


x = """abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    any.thing123@gmail.com
    somthing123@gmail.com
    @gmail.com
    1234567890
    9167005980
    Mr. Someone
    Mr. Hello"""


# In[43]:


xr = re.findall(r'[\w|\.]?@gmail.com', x)   # Raw string. This string will give you the list containing all matches
                                            # before @gmail.com word only.
print(xr)


# In[44]:


y="Hi this is my email is,something@gmail.com"
yr = re.findall(r'[\w|\.]+@gmail.com', y)     
yr


# In[45]:


d = "qWeRty@_#1237"
dr = re.findall(r'[a-zA-Z0-5]', d)    # whatever you write inside [] bracket it will choose that words and print in string format
dr


# In[46]:


s=input("Enter the string: ")
sr=re.findall(r'[aeiou]', s)      # at this point you extracting the vowels from the entered string.
if len(sr)>0:
    print("Vowels are prent")
else:
    print("Vowels are not present")


# In[47]:


d = "qWeRty@_#1237"
dr = re.findall(r'[a-z][A-Z]', d)    # whatever you write inside [] bracket it will choose that words and print in string format
dr


# In[48]:


xr = re.findall(r'[\w|\.]?@gmail.com', x)   # zero or once occurence is getting printed as shown before @gmail.com.
print(xr)


# In[49]:


xr = re.findall(r'[\w|\.]{4}@gmail.com', x)   # Here exact specific number of characters are
                                              # getting printed here which is written in {} as shown before @gmail.com.
print(xr)


# In[53]:


xr = re.findall(r'[\w.]*@gmail.com', x)     # if you dont mention | \ can also get printed your information
print(xr)


# In[8]:


xr = re.findall(r'[\w|\.]{3,10}@gmail.com', x)
print(xr)


# In[ ]:





# In[ ]:




