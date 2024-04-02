from matplotlib import pyplot as plt
import tensorflow as tf
import numpy as np
import os
import cv2
import imghdr
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy

process = tf.config.experimental.list_physical_devices('GPU')

for gpu in process:
    tf.config.experimental.set_memory_growth(gpu, True)

tf.config.list_physical_devices('GPU')

data_dir = 'data'

img_type = ['jpeg', 'jpg', 'bmp', 'png']

for image_class in os.listdir(data_dir):
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try:
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in img_type:
                print('Image not in list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e:
            print('Issue with image {}'.format(image_path))
        
data = tf.kreas.utils.image_dataset_from_directory('data')

data_it = data.as_numpy_iterator()

batch = data_it.next()

fig, ax = plt.subplots(ncols = 4, figsize = (20, 20))
for idx, img in enumerate(batch[0][:4]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(batch[1][idx])

data = data.map(lambda x,y: (x/255, y))
data.as_numpy_iterator().next()

train_size = int(len(data) * 0.7)
val_size = int(len(data) * 0.2)
test_size = int(len(data) * 0.1)

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size + val_size).take(test_size)

model = Sequential()

model.add(Conv2D(16, (3, 3), 1, activation = 'relu', input_shape = (256, 256, 3)))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3), 1, activation = 'relu'))
model.add(MaxPooling2D())
model.add(Conv2D(16, (3, 3), 1, activation = 'relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dense(num_classes, activation = 'softmax'))

model.compile('adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

model.summary()

logdir = 'logs'

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir = logdir)

hist = model.fit(train, epochs = 20, validation_data = val, callbacks = [tensorboard_callback])

test_loss, test_accuracy = model.evaluate(test)

img = cv2.imread('car.jpeg')
resize = tf.image.resize(img, (256, 256))
yhat = model.predict(np.expand_dims(resize/255, 0))
yhat

img2 = cv2.imread('cone.jpg')
resize2 = tf.image.resize(img2, (256, 256))
cone = model.predict(np.expand_dims(resize2/255, 0))
cone