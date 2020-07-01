#C:\Users\Saroj\AppData\Roaming\Python\Python37\Scripts
from wordcloud import WordCloud
import warnings
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

warnings='ignore'

st.title('WORD CLOUD GENERATOR')

st.subheader('Enter some text')
text=st.text_area('')

#st.subheader('Enter the Path/URL of the image mask')
#path=st.text_area('.')

img=Image.open(r'F:\8k wallpapers\104765.jpg')
mask=np.array(img)
fig=plt.figure(figsize=(8,8))
wc=WordCloud(background_color='white',mask=mask)
wc.generate(text)

plt.imshow(wc,cmap='viridis',interpolation='nearest')
plt.axis('off')
plt.show()

st.pyplot()
