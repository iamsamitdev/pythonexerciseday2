#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("Hello Python Notebook")
print("สวัสดีครับ")
print(2**3)


# In[ ]:


def show_message(msg):
    print(msg)

show_message("Hi Jupyter")


# In[ ]:


# print(1+2)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'print')


# In[ ]:


help(print)
help(input)
help(numpy)


# In[6]:


from Car import *


# In[7]:


# รับข้อมูลจากผู้ใช้
c_color = input('Enter favorit color: ')
c_brand = input('Enter favorit brand: ')
c_seats = input('Enter car seats: ')
c_wheels = input('Enter car wheels: ')
c_speed = input('Enter car speed: ')
c_plateid = input('Enter car plateid: ')

print("------------------------")

# สร้าง Object Car
c1 = Car(c_color, c_brand, c_seats, c_wheels, c_speed, c_plateid)
c1.printData()

