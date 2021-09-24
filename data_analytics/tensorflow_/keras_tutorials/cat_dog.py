import numpy as np
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
from tensorflow.keras.callbacks import TensorBoard
# python included:
import random
import os
import pickle
import time

model_name = 'Cats-vs-dogs-cnn-64x2-{}'.format(int(time.time()))

tensorboard = TensorBoard(log_dir='logs/{}'.format(model_name))

# get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('dark_background')
# plt.rcParams['figure.figsize'] = [13, 8]
plt.rcParams['axes.facecolor'] = '#121417'
plt.rcParams['figure.facecolor'] = '#282C34'

data_dir = 'C:\\Users\\Martin\\Dev\\keras_tutorial\\02_data'
categories = ['Dog', 'Cat']
img_size = 50

training_data = []
dataset_size = 100

def create_training_data():
    for category in categories:
        path = os.path.join(data_dir, category)
        class_num = categories.index(category)
        for img in os.listdir(path)[:dataset_size]:
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                resized_img_array = cv2.resize(img_array, (img_size, img_size))
                training_data.append([resized_img_array, class_num])
            except Exception as e: # why does it need to be capital Exception?
                pass
            
create_training_data()

random.shuffle(training_data)

X = [] # Capital bequause it is a feature
y = [] # lowercase, because its a lable

for feature, label in training_data:
    X.append(feature)
    y.append(label)
    
X = np.array(X).reshape(-1, img_size, img_size, 1)
X = X / 255.0

model = Sequential()

# Layer 1
model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Layer 2
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# Layer 3
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))

# Layer 4
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs=3, validation_split=0.1, callbacks=[tensorboard])

