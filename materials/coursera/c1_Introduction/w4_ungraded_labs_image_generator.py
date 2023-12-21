"""
- ImageGenerator

"""

import wget
import os
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# print("Current directory:", os.getcwd())
# wget.download("https://storage.googleapis.com/tensorflow-1-public/course2/week3/horse-or-human.zip")
# wget.download("https://storage.googleapis.com/tensorflow-1-public/course2/week3/validation-horse-or-human.zip")
# input("wait")


# train_horse_dir = os.path.join("./horse-or-human/horses")
# train_human_dir = os.path.join("./horse-or-human/humans")

rescale_factor = 1/255
target_size = (150,150)


model = tf.keras.models.Sequential(
    [
        tf.keras.layers.Conv2D(16, (3, 3), activation="relu", input_shape=(*target_size, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        # tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        # tf.keras.layers.MaxPooling2D(2, 2),
        # tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        # tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ]
)
model.compile(loss="binary_crossentropy", optimizer=RMSprop(learning_rate=0.01), metrics=["accuracy"])

print(model.summary())

train_datagen = ImageDataGenerator(rescale=rescale_factor)
validation_datagen = ImageDataGenerator(rescale=rescale_factor)

train_generator = train_datagen.flow_from_directory(
    "./horse-or-human",
    target_size=target_size,
    batch_size=128,
    class_mode="binary"
)

validation_generator = validation_datagen.flow_from_directory(
    "./horse-or-human",
    target_size=target_size,
    batch_size=32,
    class_mode="binary"
)


history = model.fit(
    train_generator,
    steps_per_epoch=3,
    epochs=4,
    verbose=1,
    validation_data=validation_generator,
    validation_steps=8
)

