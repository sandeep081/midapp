import streamlit as st
import numpy as np
import cv2

st.set_option('deprecation.showfileUploaderEncoding',False)
html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">

   <center><p style="font-size:25px;color:white;margin-top:10px;"Color Palette </p></center> 
   </div>
   </div>
   </div>
   """

st.markdown(html_temp,unsafe_allow_html=True)
st.header("Color Palette ")

file=st.file_uploader("Please upload image",type=("jpg","png","jpeg"))
R=0
G=st.slider('G',min_value=0,max_value=255,step=1)
B=0

def change_color(image):
  image[:]=[R,G,B]
  st.image(image,use_column_width=True)
  return 0
if file is None:
  st.text("Please upload an image")

else:
  file_bytes=np.asarray(bytearray(file.read()),dtype=np.uint8)
  image=cv2.imdecode(file_bytes,1)
  st.image(file,caption='Uploaded Image',use_column_width=True)

if st.button("Change Color"):
  result=change_color(image)

if st.button("About"):
  st.subheader("Developed by Prashant Jain")
  st.subheader("PGI")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Color Palette</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
