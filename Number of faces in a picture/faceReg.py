# Importing the python face recognition library
import face_recognition
from PIL import Image  # importing the python image library

# loading the images we want to recognize
image1 = face_recognition.load_image_file("team2.jpg")
# finding the face locations for the image we want to recognize
face_locations = face_recognition.face_locations(image1)

# displaying result
print("I found {} faces in this photograph,".format(len(face_locations)))


# trying to find all the coordinates for a face.
counter = 0
for face_location in face_locations:
    top, right, bottom, left = face_location
    print(
        "A face Located at pixel Location Top:{}, Left: {}, Bottom: {}, Right: {}".format(
            top, left, bottom, right
        )
    )
    # creating an image from those points
    face_image = image1[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("face_{}.jpg".format(counter))
    counter = counter + 1
