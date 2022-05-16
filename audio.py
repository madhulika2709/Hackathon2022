#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gtts import gTTS


# In[2]:


convert = gTTS(text='Sanja Kon', lang='en', slow=False)
# Saving the converted audio in mp3 which can be played
convert.save("audio.mp3")


# In[ ]:




