#!/usr/bin/env python
# coding: utf-8

# In[19]:


mc=[0,1,4,4,0,2,5,0,3,6,1,4,6]
d=["Saturdy","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
def day(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    if 0<a<=31 and 0<b<=12 and 1500<c<2099:
        if 1500<c<1599:
            e=0
        elif 1600<c<1699:
            e=6
        elif 1700<c<1799:
            e=4
        elif 1800<c<1899:
            e=2
        elif 1900<c<1999:
            e=0
        elif 2000<c<2099:
            e=6
        k=a+int(mc[b])+(c%100)+((c%100)//4)+e
        k=k%7
        return d[k]    
        
        


# In[21]:


day(2,4,2002)


# In[ ]:




