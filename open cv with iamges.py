#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


path = "img.jpeg"


# In[3]:


img = cv2.imread(path)


# In[4]:


img.shape


# In[8]:


cv2.imshow("window", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[15]:


#brightness of an image in OpenCV
brightness_increase = 50
brightened_image = cv2.add(img, brightness_increase)

# Display the original and brightened images
cv2.imshow("Original", img)
cv2.imshow("Brightened", brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:


# Rotate the image at different angles
angles = [30, 60, 90, 120]
for angle in angles:
    rotated_image = rotate_image(img, angle)

    # Display the rotated image
    cv2.imshow(f"Rotated {angle} degrees", rotated_image)
    cv2.waitKey(1000)  # Wait for 1 second

cv2.destroyAllWindows()


# In[5]:


import cv2
import numpy as np

def rotate_image(image, angle):
    # Get the center and dimensions of the image
    height, width = image.shape[:2]
    center = (width // 2, height // 2)

    # Define the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Apply the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image

# Load the image
path = "img.jpeg"
img = cv2.imread(path)

# Rotate the image at different angles
angles = [30, 60, 90, 120]
for angle in angles:
    rotated_image = rotate_image(img, angle)

    # Display the rotated image
    cv2.imshow(f"Rotated {angle} degrees", rotated_image)
    cv2.waitKey(1000)  # Wait for 1 second

cv2.destroyAllWindows()


# In[12]:


# cv2.imshow("window", gray_scale_img)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()


# In[ ]:


img.shape


# In[ ]:


img[:,:,1] = 0


# In[ ]:


# cv2.imshow("window", img)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()


# In[ ]:


# import cv2
 
# img = cv2.imread('/home/img/python.png', cv2.IMREAD_UNCHANGED)
 
# print('Original Dimensions : ',img.shape)
 
# scale_percent = 60 # percent of original size
width = int(100)
height = int(100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:


# Python program to explain cv2.flip() method 

# importing cv2 
# import cv2 

# path 
# path = r'C:\Users\user\Desktop\geeks14.png'

# Reading an image in default mode 
# src = cv2.imread(path) 

# Window name in which image is displayed 
window_name = 'Image'

# Using cv2.flip() method 
# Use Flip code 0 to flip vertically 
image = cv2.flip(img, -1) 

# Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[5]:


import cv2

path = "img.jpeg"
img = cv2.imread(path)

cropped_image = img[1500:3500, 2000:4000]
 
# Display cropped image
cv2.imshow("cropped", cropped_image)
 
# Save the cropped image
cv2.imwrite("Cropped Image.jpg", cropped_image)
 
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[4]:


img.shape


# In[6]:


cv2.imwrite("Cropped Image.jpg", cropped_image)


# In[1]:


import numpy as np
import cv2
image = np.zeros((512,512,3))


# In[2]:


cv2.imshow("New_image", image)
cv2.waitKey(1000)
cv2.destroyAllWindows()


# In[3]:


cv2.rectangle(image, pt1 = (100,100), pt2 = (300,300), color = (255,0,0), thickness = 3)
cv2.circle(image, center = (100,400), radius = 50, color = (0,255,0), thickness = 3)
cv2.line(image, pt1 = (0,0), pt2 = (256,256), thickness = 3, color = (0,0,255))


# In[4]:


cv2.imshow("drawing", image)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:





# In[1]:


import numpy as np
import cv2


# In[2]:


image = np.zeros((512,512,3))


# In[3]:


def draw(event, x, y, flags, params):
    if event == 1:
          cv2.circle(image, center = (100,400), radius = 50, color = (0,255,0), thickness = 3)
    print(event)
    
cv2.namedWindow(winname = 'Window')
cv2.setMouseCallback("Window", draw)

while True:
    cv2.imshow("Window", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cv2.destroyAllWindows()


# In[ ]:




