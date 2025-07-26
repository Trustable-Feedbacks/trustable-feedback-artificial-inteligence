from keras.preprocessing import sequence
import tensorflow as tf
import numpy as np
from data_input import generate_train_dataset
from data_input import VOCABULARY

# Create training dataset
raw_train_dataset = generate_train_dataset()

# Clean the text: convert to lowercase and remove special characters
SPECIAL = list('0123456789!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`')

clean_text_list = []
for dict in raw_train_dataset:
    text = ''
    for letter in dict['text']:
        if letter not in SPECIAL:
            text += str(letter).lower()
    clean_text_list.append(text)

# Tokenization function
def tokenize(text):
    words = str(text).lower().split()
    return np.array([VOCABULARY.index(word) for word in words if word in VOCABULARY])

# Apply padding to tokenized sequences (max length = 50)
PADDED_TEXT_SEQUENCE = tf.keras.preprocessing.sequence.pad_sequences(
    [tokenize(text) for text in clean_text_list],
    padding='post',
    maxlen=50,
    dtype='int32',
    truncating='post'
)

# Encode grade labels
ENCODED_LABEL_GRADE = np.array([int(dict['grade']) - 1 for dict in raw_train_dataset])

# Encode fair labels (True -> 1, False -> 0)
ENCODED_LABEL_FAIR = np.array([1 if str(dict['fair']).strip().lower() == 'true' else 0 
                               for dict in raw_train_dataset])
