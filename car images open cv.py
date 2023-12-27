#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2

# Read the image
image_path = "Car image.jpeg"
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Create a copy of the original image for drawing bounding boxes
    image_with_boxes = image.copy()

    # Define the coordinates of the bounding box manually (x, y, width, height)
    bounding_box = (100, 50, 200, 150)

    # Draw the bounding box on the image
    cv2.rectangle(image_with_boxes, (bounding_box[0], bounding_box[1]),
                  (bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
                  (0, 255, 0), 2)

    # Display the original and modified images
    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Bounding Box", image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[ ]:


import cv2

# Read the image
image_path = "Car image.jpeg"
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Clone the image for drawing
    image_with_boxes = image.copy()

    # Select ROI (Region of Interest) manually
    bounding_box = cv2.selectROI("Select ROI", image_with_boxes, fromCenter=False, showCrosshair=True)

    # Draw the selected bounding box on the image
    cv2.rectangle(image_with_boxes, (int(bounding_box[0]), int(bounding_box[1])),
                  (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3])),
                  (0, 255, 0), 2)

    # Display the image with the drawn bounding box
    cv2.imshow("Image with Bounding Box", image_with_boxes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Print the coordinates of the selected bounding box
    print("Selected Bounding Box Coordinates:", bounding_box)


# In[ ]:


import cv2

# Read the image
image_path = "Car image.jpeg"
image = cv2.imread(image_path)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Clone the image for drawing
    image_with_boxes = image.copy()

    # Select ROI (Region of Interest) manually
    bounding_box = cv2.selectROI("Select ROI", image_with_boxes, fromCenter=False, showCrosshair=True)

    # Draw the selected bounding box on the image
    cv2.rectangle(image_with_boxes, (int(bounding_box[0]), int(bounding_box[1])),
                  (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3])),
                  (0, 255, 0), 2)

    # Display the image with the drawn bounding box
    cv2.imshow("Image with Bounding Box", image_with_boxes)
    
    # Allow resizing and moving the bounding box
    key = cv2.waitKey(0) & 0xFF
    
    # Resize and move the bounding box based on arrow keys
    while key not in [27, 13]:  # Escape or Enter key to exit loop
        if key == 82:  # Up arrow key
            bounding_box = (bounding_box[0], bounding_box[1] - 1, bounding_box[2], bounding_box[3] + 1)
        elif key == 84:  # Down arrow key
            bounding_box = (bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3] + 1)
        elif key == 81:  # Left arrow key
            bounding_box = (bounding_box[0] - 1, bounding_box[1], bounding_box[2] + 1, bounding_box[3])
        elif key == 83:  # Right arrow key
            bounding_box = (bounding_box[0], bounding_box[1], bounding_box[2] + 1, bounding_box[3])
        
        # Draw the updated bounding box on the image
        image_with_boxes = image.copy()
        cv2.rectangle(image_with_boxes, (int(bounding_box[0]), int(bounding_box[1])),
                      (int(bounding_box[0] + bounding_box[2]), int(bounding_box[1] + bounding_box[3])),
                      (0, 255, 0), 2)

        # Display the image with the updated bounding box
        cv2.imshow("Image with Bounding Box", image_with_boxes)
        key = cv2.waitKey(0) & 0xFF

    cv2.destroyAllWindows()

    # Print the final coordinates of the bounding box
    print("Final Bounding Box Coordinates:", bounding_box)


# In[ ]:




