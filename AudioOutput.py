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


worker = soundex.Soundex()


# In[5]:


worker.soundex("Sanja Kon")


# In[6]:


get_ipython().system('pip install C:\\Users\\Karthik\\Downloads\\PyAudio-0.2.11-cp39-cp39-win_amd64.whl')


# In[ ]:





# In[ ]:





# In[8]:


import speech_recognition as sr


# In[7]:


get_ipython().system('pip install SpeechRecognition')


# In[12]:


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


# In[13]:


get_ipython().system('pip install gTTS')


# In[14]:


from gtts import gTTS


# In[15]:


# Choosing language as english
convert = gTTS(text='Sanja Kon', lang='en', slow=False)
# Saving the converted audio in mp3 which can be played
convert.save("audio.mp3")


# In[ ]:




