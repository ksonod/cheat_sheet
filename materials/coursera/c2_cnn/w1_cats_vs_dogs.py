
import wget
import os
import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from pathlib import Path
from glob import glob
import random
import numpy as np
from shutil import copyfile
import matplotlib.pyplot as plt

main_dir = Path(r"/materials/coursera/c2_cnn/kagglecatsanddogs_5340/PetImages")
label1 = "Cat"
label2 = "Dog"
split_size = 0.9
skip_split_data = True
target_shape = (150, 150, 3)
rescale_factor = 1/255

def make_dir(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

train_dir1 = main_dir / "training" / label1
train_dir2 = main_dir / "training" / label2
test_dir1 = main_dir / "test" / label1
test_dir2 = main_dir / "test" / label2

make_dir(main_dir / "training")
make_dir(train_dir1)
make_dir(train_dir2)
make_dir(main_dir / "test")
make_dir(test_dir1)
make_dir(test_dir2)


def split_data(source_dir, training_dir, test_dir, split_size):
    img_file_list = glob((source_dir / "*.jpg").__str__())
    random.shuffle(img_file_list)
    total_num = len(img_file_list)

    split_idx = int(np.round(total_num * split_size) )
    train_files = img_file_list[:split_idx]
    test_files = img_file_list[split_idx:]

    for train_file in train_files:
        if os.path.getsize(train_file) != 0:
            copyfile(train_file, training_dir / Path(train_file).name)
        else:
            print(f"zero file size: {train_file}")
    for test_file in test_files:
        if os.path.getsize(test_file) != 0:
            copyfile(test_file, test_dir / Path(test_file).name)
        else:
            print(f"zero file size: {test_file}")


if not skip_split_data:
    split_data(
        source_dir=main_dir / label1,
        training_dir=train_dir1,
        test_dir=test_dir1,
        split_size=split_size
    )

    split_data(
        source_dir=main_dir / label2,
        training_dir=train_dir2,
        test_dir=test_dir2,
        split_size=split_size
    )


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation="relu", input_shape=target_shape),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")
])

model.compile(
    optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
)


train_datagen = ImageDataGenerator(
    rescale=rescale_factor,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)
validation_datagen = ImageDataGenerator(rescale=rescale_factor)

train_generator = train_datagen.flow_from_directory(
    train_dir1.parent,
    target_size=target_shape[:2],
    batch_size=128,
    class_mode="binary"
)

validation_generator = validation_datagen.flow_from_directory(
    test_dir1.parent,
    target_size=target_shape[:2],
    batch_size=32,
    class_mode="binary"
)

history = model.fit(
    train_generator,
    epochs=5,
    steps_per_epoch=10,  # for development purposes
    verbose=1,
    validation_data=validation_generator
)


epochs = np.array(history.epoch)+1
plt.figure()
plt.subplot(211)
plt.plot(epochs, history.history["accuracy"], "b-")
plt.plot(epochs, history.history["val_accuracy"], "r-")

plt.subplot(212)
plt.plot(epochs, history.history["loss"], "b-")
plt.plot(epochs, history.history["val_loss"], "r-")

plt.show()
