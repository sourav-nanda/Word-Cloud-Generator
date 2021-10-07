from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import st_helper as sth
import streamlit as st
from PIL import Image



st.markdown(sth.hide_header_footer(),unsafe_allow_html=True)
st.title('WORD CLOUD GENERATOR')
text=st.text_area('Enter your text here')
    
img_types=['jpeg','jpg','png','webp']
img_file=st.file_uploader('Upload your image',type=img_types)
st.markdown(sth.write_color_text('MediumSeaGreen','h7','Ensure that the image has white background color to get the wordcloud in your desired shape'),unsafe_allow_html=True)
size=st.slider('Adjust the resolution of the wordcloud',1,10)

def binary_detect(img):
    if len(img.shape)<3:
       wc=WordCloud(background_color='white',mask=mask,height=1920,width=1080)
       cloud=wc.generate(text)
       fig,ax=plt.subplots(figsize=[size,size])
       plt.imshow(cloud,cmap='viridis',interpolation='bilinear')
       plt.axis('off')
       plt.show()
       with col2:
            st.pyplot(fig)
    else:
         wc=WordCloud(background_color='white',mask=mask,height=1920,width=1080)
         img_col=ImageColorGenerator(mask)
         cloud=wc.generate(text)
         fig,ax=plt.subplots(figsize=[size,size])
         plt.imshow(wc.recolor(color_func=img_col),cmap='viridis',interpolation='bilinear')
         plt.axis('off')
         plt.show()
         with col2:
              st.pyplot(fig)


if img_file is not None:
     try:
          img=Image.open(img_file)
          mask=np.array(img)
          col1,col2=st.columns(2)
          col1.image(mask,width=350,)
          binary_detect(mask)
     except:
          st.subheader('Upload an Image')


st.sidebar.markdown(sth.credits(),unsafe_allow_html=True)

