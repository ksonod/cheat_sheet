""""
- Densely connected NN
- Callbacks
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

####
num_dense_list = [128, 512, 1024]
include_callback = True
####

fmnist = tf.keras.datasets.fashion_mnist

(training_images, training_labels), (test_images, test_labels) = fmnist.load_data()

print(
    f"training_images: {training_images.shape}. training_labels: {training_labels.shape}. "
    f"test_images: {test_images.shape}. test_labels: {test_labels.shape}"
)

print(f"data type: {training_images.dtype}")

# normalization
training_images = training_images/255
test_images = test_images/255



class myCallback(tf.keras.callbacks.Callback):
    """
    You can create a callback by defining a class that inherits the tf.keras.callbacks.Callback base class. From there,
    you can define available methods to set where the callback will be executed. For instance below, you will use the
    on_epoch_end() method to check the loss at each training epoch.
    """

    def on_epoch_end(self, epoch, logs={}):
        if(logs.get("accuracy") >= 0.7):
            print("\n reached 70% accuracy")
            self.model.stop_training = True


def model_building(num_dense=128, include_callback=True):

    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(num_dense, activation=tf.nn.relu),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ]
    )

    model.compile(
        optimizer=tf.optimizers.Adam(),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    if include_callback:
        callbacks = myCallback()
        model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
    else:
        model.fit(training_images, training_labels, epochs=5)

    return model

results = []
for num_dense in num_dense_list:
    print(num_dense)
    model = model_building(num_dense=num_dense, include_callback=include_callback)
    results.append(model.evaluate(test_images, test_labels))

print(results)


print(0)
