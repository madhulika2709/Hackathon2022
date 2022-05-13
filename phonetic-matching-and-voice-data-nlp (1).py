#!/usr/bin/env python
# coding: utf-8

# In[1]:




import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[2]:


get_ipython().system('pip install soundex')


# In[3]:


import soundex


# In[4]:


# Running the soundex function
worker = soundex.Soundex()


# **We see that we get the same output for words that are similar to natural but have a typo/are misspelt. This is so because the pronounciation is very similar to the root correct word**

# In[5]:


worker.soundex("Sanja Kon")


# In[6]:


worker.soundex("nataral")


# In[7]:


worker.soundex("nutural")


# In[8]:


worker.soundex("language")


# In[9]:


worker.soundex("processing")


# In[10]:


get_ipython().system('apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg --yes')


# In[13]:


get_ipython().system('pip install C:\\Users\\Karthik\\Downloads\\PyAudio-0.2.11-cp39-cp39-win_amd64.whl')


# In[15]:


get_ipython().system('pip install SpeechRecognition')


# In[15]:


import speech_recognition as sr


# In[20]:


# Run this on your local machine with a mic available
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please say something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, phrase_time_limit=4)
    print("Time over, thanks")
    
try:
    print("I think you said: "+r.recognize_google(audio))
except:
    pass


# <h2>Converting text to speech</h2>

# In[2]:


get_ipython().system('pip install gTTS')


# In[3]:


from gtts import gTTS


# In[5]:


# Choosing language as english
convert = gTTS(text='Sanja Kon', lang='en', slow=False)
# Saving the converted audio in mp3 which can be played
convert.save("audio.mp3")


# In[6]:


pip install pycountry


# In[9]:


import pycountry

input_countries = ['France']
countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_2
codes = [countries.get(country,'Unknow Code') for country in input_countries]
print(codes)


# In[10]:


get_ipython().system('pip install goslate')


# In[12]:


import goslate

text = "good night"

gs = goslate.Goslate()
outp=gs.translate(text,'FR')
print(outp)


# In[4]:


import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");


# In[7]:


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE PRONOUNCIATION
         (EMPID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AUDIO_OUTPUT    BLOB);''')
print ("Table created successfully");

conn.close()


# In[8]:


import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully");

conn.execute("INSERT INTO PRONOUNCIATION (EMPID,NAME,AUDIO_OUTPUT)       VALUES (1472877, 'Madhulika', '37e79f' )");

conn.commit()
print ("Records created successfully");
conn.close()


# In[10]:


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




