from wordcloud import WordCloud
import warnings
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

warnings='ignore'
def gen():
    st.title('WORD CLOUD GENERATOR')
    st.subheader('Enter your text here')
    text=st.text_area('')
    
    img_types=['jpeg','jpg','png','webp']
    img_file=st.file_uploader('Upload your image',type=img_types)
    st.write('supported file types:','jpeg','jpg','png','webp')

    img=plt.imread(img_file)
    mask=np.array(img)
    size=st.slider('Adjust the size of the wordcloud',value=(1,10,value=(5,14))
    fig=plt.figure(figsize=(size,size))
    wc=WordCloud(background_color='white',mask=mask)
    
    return wc.generate(text)

plt.imshow(gen(),cmap='viridis',interpolation='bilinear')
plt.axis('off')
plt.show()

st.pyplot()
