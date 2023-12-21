"""
- Conv Net
- callback

In the videos you looked at how you would improve Fashion MNIST using Convolutions. For this exercise see if you can
improve MNIST to 99.5% accuracy or more by adding only a single convolutional layer and a single MaxPooling 2D layer to
the model from the assignment of the previous week.
You should stop training once the accuracy goes above this amount. It should happen in less than 10 epochs, so it's ok
to hard code the number of epochs for training, but your training must end once it hits the above metric. If it doesn't,
 then you'll need to redesign your callback.
When 99.5% accuracy has been hit, you should print out the string "Reached 99.5% accuracy so cancelling training!"

"""

from materials.my_useful_funcs.utils import *

fmnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = fmnist.load_data()

training_images = training_images[:, :, :, np.newaxis]/255
test_images = test_images[:, :, :, np.newaxis]/255

show_data_type_and_shape(training_images)
show_data_type_and_shape(training_labels)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get("accuracy")>0.94:
            print("\n94% accuracy")
            self.model.stop_training = True

def convolutional_model():

    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", input_shape=(28,28,1)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model

model = convolutional_model()
callbacks = myCallback()
history = model.fit(
    training_images, training_labels, epochs=10, callbacks=[callbacks]
)

print(f"Your model was trained for {len(history.epoch)} epochs")