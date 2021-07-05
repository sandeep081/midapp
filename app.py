import numpy as np
import pandas as pd
import cv2 as cv
import matplotlib.pyplot as plt
import streamlit as st
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
Transformation = st.selectbox('How would you like to be contacted?',   ("Translation","Scaling","Shearing","Reflection","Rotation"))

def change_color(image):

  st.image(image,use_column_width=True)
  return 0

if file is None:
  st.text("Please upload an image")

else:
  file_bytes=np.asarray(bytearray(file.read()),dtype=np.uint8)
  image=cv.imdecode(file_bytes,1)
  st.image(file,caption='Uploaded Image',use_column_width=True)
  if Transformation == "Scaling":
    print(image.shape)

    plt.axis('off')
    plt.imshow(image)
    plt.show()
    rows, cols, dim = image.shape

    M = np.float32([[2, 0, 0],
                    [0, 2, 0],
                    [0, 0, 1]])
    image = cv.warpPerspective(image, M, (cols * 2, rows * 2))

  if Transformation == "Shearing":
    plt.axis('off')
    plt.imshow(image)
    plt.show()
    rows, cols, dim = image.shape
    M1 = np.float32([[1, 0.5, 0],
                     [0.5, 1, 0],
                     [0, 0, 1]])

    image = cv.warpPerspective(image, M1, (int(cols * 1.5), int(rows * 1.5)))
    # sheared_imgy = cv.warpPerspective(image,M2,(int(cols*1.5),int(rows*1.5)))

  if Transformation == "Reflection":
    plt.imshow(image)
    plt.show()
    x_axis = False
    y_axis = True
    rows, cols, dim = image.shape
    x = 0
    y = 0
    val_x = 1
    val_y = 1
    if x_axis and y_axis:
      x = rows
      y = cols
      val_y = -1
      val_x = -1
    elif x_axis:
      x = rows
      val_x = -1
    else:
      y = cols
      val_y = -1
    M = np.float32([[val_y, 0, y],
                    [0, val_x, x],
                    [0, 0, 1]])

    image = cv.warpPerspective(image, M, (int(cols), int(rows)))

  if Transformation == "Rotation":
    rotation_angle = 20
    rows, cols, dim = image.shape
    angle = np.radians(rotation_angle)
    M = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
    rotated_img = cv.warpPerspective(image, M, (int(cols), int(rows)))
    plt.imshow(rotated_img)
    plt.show()
    plt.imsave("lrotated.jpg", rotated_img)
  if Transformation == "Translation":
    M = np.float32([[1, 0, 20], [0, 1, 100], [0, 0, 1]])
    img1 = cv.warpPerspective(image, M, (image.shape[1] * 2, image.shape[0] * 2))

    M = np.float32([[1, 0, 20], [0, 1, -100], [0, 0, 1]])
    img2 = cv.warpPerspective(image, M, (image.shape[1], image.shape[0]))

    M = np.float32([[1, 0, 100], [0, 1, 20], [0, 0, 1]])
    img3 = cv.warpPerspective(image, M, (image.shape[1], image.shape[0]))

    M = np.float32([[1, 0, -100], [0, 1, 20], [0, 0, 1]])
    img4 = cv.warpPerspective(image, M, (image.shape[1], image.shape[0]))
    titles = ['Orig', 'down', 'up', 'To the right', 'left']
    images = [image, img1, img2, img3, img4]
    for i in range(1, 6):
      plt.subplot(2, 3, i)

      plt.imshow(images[i - 1])
      plt.title(titles[i - 1])
      plt.xticks([100]), plt.yticks([100])
    plt.show()

  

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
