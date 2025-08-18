import gdown
import json
import os
from dotenv import load_dotenv

# Loading environment variables:
load_dotenv(dotenv_path='utils/.env')

# Declaring esential content to load the dataset from Google Drive
    # Declaring IDs to fill the URL - IDs are environmnet variables
tfm_train_dataset_id = os.getenv('TFM_TRAIN_DATASET_ID')
tfm_evaluation_dataset_id = os.getenv('TFM_EVALUATION_DATASET_ID')

    # Declaring the URL of both archives
tfm_train_dataset_url = f'https://drive.google.com/uc?id={tfm_train_dataset_id}'
tfm_evaluation_dataset_url = f'https://drive.google.com/uc?id={tfm_evaluation_dataset_id}'

    # Declaring the file name
tfm_train_dataset_output = 'trustable-feedback-train-dataset.json'
tfm_evaluation_dataset_output = 'trustable-feedback-evaluation-dataset.json'


# Declaring functions:
    # Import the train dataset:
def generate_train_dataset():
    # Download the file from Google Drive
    gdown.download(tfm_train_dataset_url, tfm_train_dataset_output, quiet=False)
    
    # Open the file and creating the dataset
    with open(tfm_train_dataset_output, 'r', encoding='utf-8') as dataset:
        dataset = json.load(dataset)

     # Delete the installed file
    os.remove(tfm_train_dataset_output)
    return dataset

    # Import evaluation dataset:
def generate_evaluate_dataset():
    gdown.download(tfm_evaluation_dataset_url, tfm_evaluation_dataset_output, quiet=False)

    with open(tfm_evaluation_dataset_output, 'r', encoding='utf-8') as dataset:
        dataset = json.load(dataset)
    
    os.remove(tfm_evaluation_dataset_output)
    return dataset

    # Extract the vocabulary of the dataset:
def vocabulary(dataset=generate_train_dataset()):
    SPECIAL = list('0123456789!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`')
    vocabulary = []

    # Interate the dataset
    for dict in dataset:
        review = dict['text'] # Defining the text 'review'

        # List comprehension to clean the text
        new_review = ''.join([letter.lower() for letter in review if letter not in SPECIAL])
        words = new_review.split(' ') # Is a list of the words
        vocabulary.extend(words) # Concat the new words to the vocabulary
    return set(vocabulary)

# Declaring Consts
VOCABULARY = sorted(vocabulary()) # For standard, referees to the train dataset
VOCABULARY_SIZE = len(VOCABULARY)