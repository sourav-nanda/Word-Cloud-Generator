from wordcloud import WordCloud,ImageColorGenerator
import warnings
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

warnings='ignore'
def gen():
    global size
    global wc
    global img_col
    st.title('WORD CLOUD GENERATOR')
    st.subheader('Enter your text here')
    text=st.text_area('')
    
    img_types=['jpeg','jpg','png','webp']
    img_file=st.file_uploader('Upload your image',type=img_types)
    st.write('Supported file types are ','jpeg,','jpg,','png,','webp')
    if img_file is not None:
        img=Image.open(img_file)
        mask=np.array(img)
        size=st.slider('Adjust the resolution of the wordcloud',1,10)
    
    
    wc=WordCloud(background_color='white',mask=mask,height=1920,width=1080)
    
    img_col=ImageColorGenerator(mask)
    
    return wc.generate(text)
gen()
fig=plt.figure(figsize=[size,size])
plt.imshow(wc.recolor(color_func=img_col),cmap='viridis',interpolation='bilinear')
plt.axis('off')
plt.show()

st.pyplot()
