"""
- Densely connected NN
- Callbacks



In the course you learned how to do classification using Fashion MNIST, a data set containing items of clothing. There's
another, similar dataset called MNIST which has items of handwriting -- the digits 0 through 9.

Write an MNIST classifier that trains to 99% accuracy and stops once this threshold is achieved. In the lecture you saw
how this was done for the loss but here you will be using accuracy instead.

Some notes:
Your network should succeed in less than 9 epochs.
When it reaches 99% or greater it should print out the string "Reached 99% accuracy so cancelling training!" and stop
training. If you add any additional variables, make sure you use the same names as the ones used in the class. This is
important for the function signatures (the parameters and names) of the callbacks.
"""

from tensorflow import keras
from materials.my_useful_funcs.utils import *

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

show_data_type_and_shape(x_train)
show_data_type_and_shape(y_train)
show_data_type_and_shape(x_test)

if x_train.dtype == np.uint8:
    x_train = x_train/255
    x_test = x_test/255
    print("Data normalized")


class myCallback(tf.keras.callbacks.Callback):
    """
    You can create a callback by defining a class that inherits the tf.keras.callbacks.Callback base class. From there,
    you can define available methods to set where the callback will be executed. For instance below, you will use the
    on_epoch_end() method to check the loss at each training epoch.
    """

    def on_epoch_end(self, epoch, logs={}):
        if (logs.get("accuracy") >= 0.99):
            print("\n reached 99% accuracy")
            self.model.stop_training = True

callbacks = myCallback()

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",  # https://stackoverflow.com/questions/58565394/what-is-the-difference-between-sparse-categorical-crossentropy-and-categorical-c
    metrics=["accuracy"]
)

history = model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])

