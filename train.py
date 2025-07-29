import tensorflow as tf
import os
from keras.callbacks import ModelCheckpoint
from preprocess import preprocess
from model import MODEL
from data_input import generate_train_dataset

# Defining constants:
PADDED_TEXT_SEQUENCE, ENCODED_LABEL_GRADE, ENCODED_LABEL_FAIR = preprocess(generate_train_dataset())

# Define training dataset:
text_tensor = tf.data.Dataset.from_tensor_slices(tf.convert_to_tensor(PADDED_TEXT_SEQUENCE))
grade_tensor = tf.data.Dataset.from_tensor_slices(tf.convert_to_tensor(ENCODED_LABEL_GRADE))
lables_tensor = tf.data.Dataset.from_tensor_slices(tf.convert_to_tensor(ENCODED_LABEL_FAIR))

    # Zip datasets:
dataset = tf.data.Dataset.zip(((text_tensor, grade_tensor), lables_tensor))


# Create Batchs:
BATCH_SIZE = 64
EPOCHS = 10
BUFFER_SIZE = 10000

data = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# Create Checkpoint:
CHECKPOINT_DIR = './utils/'
CHECKPOINT_PREFIX = os.path.join(CHECKPOINT_DIR, 'trustable_feedbacks_ai_callback')

checkpoint_callback = ModelCheckpoint(
    filepath=CHECKPOINT_PREFIX + '.h5',
    save_best_only=True,
    monitor='loss',
    mode='max',
    save_freq='epoch',
    save_weights_only=True
)

# Training:
history = MODEL.fit(data, epochs=EPOCHS, callbacks=[checkpoint_callback])