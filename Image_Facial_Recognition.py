import face_recognition 

image = face_recognition.load_image_file("img file name") 
face_locations = face_recognition.face_locations(image) 
 
print("I found {} face(s) in this photograph.").format(len(face_locations))
