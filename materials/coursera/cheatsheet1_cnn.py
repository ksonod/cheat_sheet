import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.inception_v3 import InceptionV3


########## CNN Building by yourself. #####################
model = tf.keras.models.Sequential(
    [
    tf.keras.layers.Conv2D(16, (3, 3), activation="relu", input_shape=(150,150, 3)),  # for RGB
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation="relu"),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid")  # Binary classification.
#    tf.keras.layers.Dense(3, activation="softmax")  # Multi-class classification.
    ]
)

model.compile(
    loss="binary_crossentropy",  # binary classificaiton
    # loss="categorical_crossentropy",  # multi-class classification
    optimizer="adam",
    metrics=["accuracy"]
)

# Data generator and augumentation
train_datagen = ImageDataGenerator(
    rescale=1/255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)
validation_datagen = ImageDataGenerator(rescale=1/255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=target_shape[:2],
    batch_size=128,
    class_mode="binary"
)

validation_generator = validation_datagen.flow_from_directory(
    test_dir,
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



########## CNN Transfer Learning #####################
pre_trained_model = InceptionV3(
    input_shape=target_shape,
    include_top=False,
    weights=None
)

pre_trained_model.load_weights(weight_path)
for layer in pre_trained_model.layers:
    layer.trainable = False

# now, layer stores the last layer.
# last_layer = pre_trained_model.get_layer('mixed10')
last_output = layer.output
x = tf.keras.layers.Flatten()(last_output)
x = tf.keras.layers.Dense(1024, activation='relu')(x)
x = tf.keras.layers.Dropout(0.2)(x)
x = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(pre_trained_model.input, x)

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)



