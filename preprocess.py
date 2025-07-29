from keras.preprocessing import sequence
import tensorflow as tf
import numpy as np
from data_input import generate_train_dataset
from data_input import generate_evaluate_dataset
from data_input import VOCABULARY

# Clean the text: convert to lowercase and remove special characters
SPECIAL = list('0123456789!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`')
def clean_text(dataset):
    clean_text_list = []
    for dict in dataset:
        text = ''
        for letter in dict['text']:
            if letter not in SPECIAL:
                text += str(letter).lower()
        clean_text_list.append(text)
    return clean_text_list

# Tokenization function
def tokenize(text):
    words = str(text).lower().split()
    return np.array([VOCABULARY.index(word) for word in words if word in VOCABULARY])

# Function to apply padding to tokenized sequences (max length = 50)
def generate_padded_text_sequence(text_list):
    return tf.keras.preprocessing.sequence.pad_sequences(
        [tokenize(text) for text in text_list],
        padding='post',
        maxlen=50,
        dtype='int32',
        truncating='post'
    )

# Function to encode grade labels
def generate_encoded_grade_lable(dataset):
    return np.array([int(dict['grade']) - 1 for dict in dataset])

# Function to encode fair labels (True -> 1, False -> 0)
def generate_encoded_fairly_lable(dataset):
    return np.array([1 if str(dict['fair']).strip().lower() == 'true' else 0 
                               for dict in dataset])

# Function to preprocess the dataset:
def preprocess(dataset, isConsult=False):
    text_list = clean_text(dataset)
    if (isConsult):
        return generate_padded_text_sequence(text_list), generate_encoded_grade_lable(dataset)
    return generate_padded_text_sequence(text_list), generate_encoded_grade_lable(dataset), generate_encoded_fairly_lable(dataset)