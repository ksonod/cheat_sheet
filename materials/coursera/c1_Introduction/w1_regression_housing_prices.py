"""
A house has a base cost of 50k, and every additional bedroom adds a cost of 50k. This will make a 1 bedroom house cost 100k, a 2 bedroom house cost 150k etc.
How would you create a neural network that learns this relationship so that it would predict a 7 bedroom house as costing close to 400k etc.
Hint: Your network might work better if you scale the house price down. You don't have to give the answer 400...it might be better to create something that predicts the number 4, and then your answer is in the 'hundreds of thousands' etc.
"""

import tensorflow as tf
import numpy as np

def house_model():

    xs = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
    ys = (50 + 50 * xs)/100  # /100 is to scale down the price

    model = tf.keras.Sequential(tf.keras.layers.Dense(units=1, input_shape=[1]))
    model.compile(optimizer="sgd", loss="mean_squared_error")
    model.fit(xs, ys, epochs=1000)
    return model

model = house_model()

new_x = np.array([7.])

print(
    f"prediction for the input {new_x}: {model.predict(new_x)}"
)
