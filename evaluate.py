from preprocess import preprocess
from model import MODEL
from data_input import generate_evaluate_dataset

# Create the constants:
padded_text_sequence, encoded_grade_lable, encoded_fairly_lable = preprocess(generate_evaluate_dataset())

# Load the model:
MODEL.load_weights('./utils/trustable_feedbacks_ai_callback.h5')

# Evaluate the model:
history = MODEL.evaluate(x=[padded_text_sequence, encoded_grade_lable],
                         y=encoded_fairly_lable,
                         batch_size=64,
                         return_dict=True
                         )