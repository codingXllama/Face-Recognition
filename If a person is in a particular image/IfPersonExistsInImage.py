"""
Author: Osama A. 
Purpose: aim to look for obama in a crowd given the appearance of his face
Date: Wed May15,2019

"""

# Importing the required library
import face_recognition

# Storing the image we are trying to find
MainImage = face_recognition.load_image_file("obama1.jpg")

# Storing and loading the image we will be searching on
ImageToSearch = face_recognition.load_image_file("ObamaWithPeeps.jpg")

# encoding the images that will be searched for
obamaEncoding = face_recognition.face_encodings(MainImage)[0]
unkownEncoding = face_recognition.face_encodings(ImageToSearch)[0]

# comparing both of the endcoded images to see if they match/ if the obamaImage exists in the Obama with crowd image
SearchResults = face_recognition.compare_faces([obamaEncoding], unkownEncoding)

# outputting the results
if SearchResults:
    print("Yes, Obama does exist in the crowd! ")
else:
    print("No, Obama does NOT exist in the crowd! ")
