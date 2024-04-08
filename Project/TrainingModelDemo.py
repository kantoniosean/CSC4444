from tensorflow.keras.models import load_model
import tensorflow as tf

img = tf.io.read_file("test/myCar.jpg")

img = tf.image.decode_image(img)

img = img[:, :, :3]

img = tf.image.resize(img, [240, 240])

img = img / 255

new_model = load_model('image_class_model.keras')

pred = new_model.predict(tf.expand_dims(img, axis=0))
img_class = pred[0].argmax()

if (img_class == 0):
    print("This image is a car")
elif (img_class == 1):
    print("This image is a merge sign")
elif(img_class == 2):
    print("This image is a stop sign")
elif(img_class == 3):
    print("This image is a traffic cone")
elif(img_class == 4):
    print("This image is a traffic light")
