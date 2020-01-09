import PIL.Image
import PIL.ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("/Users/himsaragallage/Documents/Face Detection Linkedin /TestFaces/winker3.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

# Create a PIL drawing object to be able to draw lines later
draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for face_landmarks in face_landmarks_list:

    for name, list_of_points in face_landmarks.items():

        # Print the location of each facial feature in this image
        if (name == "left_eye") | (name == "right_eye"):

            # print("The {} in this face has the following points: {}".format(name, list_of_points))
            draw.line(list_of_points, fill="red", width=2)
            draw.point(list_of_points)
            # print(list_of_points)
            upper = ((list_of_points[2])[1])
            downer = ((list_of_points[4])[1])
            difference = downer - upper
            print(difference)
            if difference <= 2 :
                print("The {} in this face is closed". format(name))
            else:
                print("The {} in this face is Open". format(name))

        # Let's trace out each facial feature in the image with a line!

pil_image.show()
# chin, left_eyebrow, right_eyebrow, nose_bridge, nose_tip, left_eye, right_eye, top_lip, bottom_lip
# Above mentioned are the names of the features given by the variable name
