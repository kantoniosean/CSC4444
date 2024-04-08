import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.optimizers import Adam
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2
import imghdr
import random
import shutil
import pathlib

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
                print('image not in list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e:
            print('issue with image {}'.format(image_path))

data = tf.keras.utils.image_dataset_from_directory('data')
data_it = data.as_numpy_iterator()

batch = data_it.next()

fig, ax = plt.subplots(ncols = 5, figsize = (20, 20))
for idx, img in enumerate(batch[0][:5]):
    ax[idx].imshow(img.astype(int))
    ax[idx].title.set_text(batch[1][idx])

def split_data(directory, train_size, test_size):
  
  rng = random.Random(42)

  for root, folders, page in os.walk(directory):
    for folder in folders:
     
      files = []
      for file_name in os.listdir(root + folder + "/"):
        files.append(file_name)

      rng.shuffle(files)

      train_files = files[:int(len(files) * train_size)]
      test_files = files[int(len(files) * train_size) : int(len(files) * (train_size + test_size))]
      val_files = files[int(len(files) * (train_size + test_size)):]

      for one_file in train_files:

        dest_dir = "dir/train/" + folder + "/"
        os.makedirs(dest_dir, exist_ok = True)

        shutil.copy2(src=(root + folder + "/" + one_file),
                    dst = (dest_dir + one_file))
      print("Folder " + folder + ". Train data copied." + str(len(train_files)) + " files")

      for one_file in test_files:
        
        dest_dir = "dir/test/" + folder + "/"
        os.makedirs(dest_dir, exist_ok = True)

        shutil.copy2(src = (root + folder + "/" + one_file),
                    dst = (dest_dir + one_file))
      print("Folder " + folder + ". Test data copied." + str(len(test_files)) + " files")

      for one_file in val_files:

        dest_dir = "dir/validation/" + folder + "/"
        os.makedirs(dest_dir, exist_ok = True)

        shutil.copy2(src = (root + folder + "/" + one_file),
                    dst = (dest_dir + one_file))
      print("Folder " + folder + ". Validation data copied." + str(len(val_files)) + " files")

def get_names(directory):
  data_dir = pathlib.Path(directory)
  class_names = np.array(sorted([item.name for item in data_dir.glob("*")])) 
  print(class_names)
  return class_names

split_data(directory = "data/", train_size = 0.7, test_size = 0.2)
class_names = get_names(directory = "dir/train/")

train_imgen = ImageDataGenerator(rescale=1/255.)
test_imgen = ImageDataGenerator(rescale=1/255.)
val_imgen = ImageDataGenerator(rescale=1/255.)

train_data = train_imgen.flow_from_directory(directory = "dir/train", target_size = (240, 240), batch_size = 32, class_mode = "categorical")

test_data = test_imgen.flow_from_directory(directory = "dir/test", target_size = (240, 240), batch_size = 32, class_mode = "categorical")

validation_data = val_imgen.flow_from_directory(directory = "dir/validation", target_size = (240, 240), batch_size = 32, class_mode = "categorical")

tf.random.set_seed(42)

model = Sequential([])

model.add(Conv2D(32, 3, activation = 'relu', input_shape = (240, 240, 3)))
model.add(MaxPool2D(pool_size = 2))

model.add(Conv2D(64, 3, activation = 'relu'))
model.add(MaxPool2D(pool_size = 2))

model.add(Conv2D(128, 3, activation = 'relu'))
model.add(MaxPool2D(pool_size = 2))

model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation = 'softmax'))

model.compile(loss="categorical_crossentropy", optimizer=Adam(), metrics = ["accuracy"])

history = model.fit(train_data, batch_size = 32, epochs = 5, steps_per_epoch = len(train_data), validation_data = validation_data, validation_steps = len(validation_data))

model.save('ImageClassifier.keras')