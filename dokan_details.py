#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import pandas as pd
import numpy as np
from csv import DictWriter
a=input("enter your file name with full path :  ")
file_nm=''
for i in a:
    if (i=="\\"):
        file_nm=file_nm+'\\'
    file_nm=file_nm+i
print(file_nm)        
#check if exist file
if os.path.exists(file_nm):
 #   print("File exists")
    field_names=['date','m_name','item','weight','unit','price_per_unit','cost','paid','due']
    c='yes'
    in_date=input("enter todays date : ")
    while(c=='yes'):
        in_name=input("enter the name : ")
        in_item=input("enter the item name : ")
        in_weight=int(input("enter the weight of item : "))
        in_unit=input("enter the unit : ")
        in_pprice=int(input("enter per unit price : "))
        in_cost=in_pprice*in_weight
        in_paid=int(input("enter amount paid : "))

        in_due=(prev_due(file_nm,in_date,in_name,in_item)+in_cost)-int(in_paid)
        entry={'date':in_date,'m_name':in_name,'item':in_item,'weight':in_weight,'unit':in_unit,'price_per_unit':in_pprice,'cost':in_cost,'paid':in_paid,'due':in_due}
        
        c=input("do u want to enter more records (yes\no) : ")
        with open(file_nm,'a',newline='\n') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names)
            dictwriter_object.writerow(entry)
            f_object.close()

else:
#    print("File does not exist")
    df=pd.DataFrame(columns=['date','m_name','item','weight','unit','price_per_unit','cost','paid','due'])
    df.to_csv(file_nm,header=True,index=False)


# In[8]:


from datetime import datetime, timedelta

def previous_date(date_str, date_format="%Y-%m-%d"):
    # Convert string to date object
    date_obj = datetime.strptime(date_str, date_format)
    # Subtract one day
    previous_date = date_obj - timedelta(days=1)
    # Convert back to string
    return previous_date.strftime(date_format)


# In[4]:


def prev_due(f_name,in_date,in_name,in_item):
    data=pd.read_csv(f_name)
    k=data["due"][(data['date']==previous_date(in_date)) & (data['m_name']==in_name) & (data['item']==in_item)]
    if(len(k)==0):
        return(0)
    else:
        return(int(k.iloc[0]))


# In[ ]:





# # store profit

# In[ ]:


def total_profit(f_name,in_date):
    data=pd.read_csv(f_name)
    t_expence=data['cost'][data['date']==in_date].sum()
    t_income=int(input("enter total today's income : "))
    profit = t_income - t_expence
    t_due=data['due'][data['date']=='2025-07-16'].sum()


# In[ ]:





# In[ ]:





# # tests

# In[12]:


import os
import pandas as pd
import numpy as np
from csv import DictWriter
f_name="D:\\dokan_details.csv"
in_date='2025-07-14'
in_name='A'
in_item='milk'
data=pd.read_csv(f_name)
k=data["due"][(data['date']==previous_date(in_date)) & (data['m_name']==in_name) & (data['item']==in_item)]
if(len(k)==0):
    print(0)
else:
    print(int(k.iloc[0]))
data


# In[15]:


data['due'][data['date']=='2025-07-16'].sum()


# In[16]:


data['paid'][data['date']=='2025-07-16'].sum()


# In[ ]:




