#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");


# In[2]:


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE PRONOUNCIATION
         (EMPID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AUDIO_OUTPUT    BLOB);''')
print ("Table created successfully");

conn.close()


# import sqlite3
# 
# conn = sqlite3.connect('test.db')
# print ("Opened database successfully");
# 
# conn.execute("INSERT INTO PRONOUNCIATION (EMPID,NAME,AUDIO_OUTPUT) \
#       VALUES (67865, 'Test', '37e79f' )");
# 
# conn.commit()
# print ("Records created successfully");
# conn.close()

# In[4]:


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("INSERT INTO PRONOUNCIATION (EMPID,NAME,AUDIO_OUTPUT)       VALUES (45655546, 'Test', '37e79f' )");

conn.commit()
print ("Records created successfully");
conn.close()


# In[5]:


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

cursor = conn.execute("SELECT EMPID,NAME,AUDIO_OUTPUT from PRONOUNCIATION")
for row in cursor:
   print ("EMPID = ", row[0])
   print ("NAME = ", row[1])
   print ("AUDIO_OUTPUT = ", row[2])
  
print ("Operation done successfully");
conn.close()


# In[ ]:




