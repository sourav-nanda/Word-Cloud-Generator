from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

st.markdown('<style>#MainMenu {Visibility:hidden;}footer {Visibility:hidden;} </style>', unsafe_allow_html=True)

st.title('WORD CLOUD GENERATOR')
st.subheader('Enter your text here')
text=st.text_area('')
    
img_types=['jpeg','jpg','png','webp']
img_file=st.file_uploader('Upload your image',type=img_types)
st.text('''Supported file types are jpeg,jpg,png,webp''')
st.write('Ensure that the image has white background color only to get the wordcloud in your desired shape')
if img_file:
   img=Image.open(img_file)
   size=st.slider('Adjust the resolution of the wordcloud',1,10)
   col1,col2=st.beta_columns(2)
   col1.image(img,width=350,height=350)
   mask=np.array(img)
   wc=WordCloud(background_color='white',mask=mask,height=1920,width=1080)
   img_col=ImageColorGenerator(mask)
   cloud=wc.generate(text)
    
     
fig,ax=plt.subplots(figsize=[size,size])
plt.imshow(wc.recolor(color_func=img_col),cmap='viridis',interpolation='bilinear')
plt.axis('off')
plt.show()
with col2:
    st.pyplot(fig)

st.subheader('Connect with me')
st.write('<link rel="stylesheet" type="text/css" href="https://cdn.rawgit.com/vaakash/socializer/80391a50/css/socializer.min.css"><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">',unsafe_allow_html=True)
st.write('<div class="socializer a sr-32px sr-opacity sr-bg-none sr-pad"><span class="sr-facebook"><a href="https://www.facebook.com/sourav.nanda.528" target="_blank" title="Facebook"><i class="fa fa-facebook"></i></a></span><span class="sr-instagram"><a href="https://instagram.com/_sourav_nanda_/?hl=en" target="_blank" title="Instagram"><i class="fa fa-instagram"></i></a></span><span class="sr-linkedin"><a href="https://www.linkedin.com/in/sourav-nanda-31ab841aa/" target="_blank" title="LinkedIn"><i class="fa fa-linkedin"></i></a></span><span class="sr-github"><a href="https://github.com/sourav-nanda" target="_blank" title="Github"><i class="fa fa-github"></div>',unsafe_allow_html=True)
