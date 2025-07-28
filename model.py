import tensorflow as tf
from data_input import VOCABULARY_SIZE

# Function to create the model:
def create_model():
    # Creates the inputs:
    text_input = tf.keras.Input(shape=(50,))
    grade_input = tf.keras.Input(shape=(1,))
    
    # Creates the layers for each input:
        # For the text:
    text_layer = tf.keras.layers.Embedding(input_dim=VOCABULARY_SIZE, output_dim=50,
                                                   input_length=50, trainable=True)(text_input)
    text_layer = tf.keras.layers.LSTM(units=48)(text_layer)

        # For the grades:
    grade_layer = tf.keras.layers.Dense(units=5)(grade_input)

    # Concatenates the layers:
    concatenated = tf.keras.layers.concatenate([text_layer, grade_layer]) 

    # Continues the model:
    output = tf.keras.layers.Dense(units=150, activation='relu')(concatenated)
    output = tf.keras.layers.Dense(units=150, activation='relu')(output)
    output = tf.keras.layers.Dense(units=50, activation='relu')(output)
    output = tf.keras.layers.Dense(units=1, activation='sigmoid')(output)
    
    # Builds and returns the model
    return tf.keras.Model(
        inputs=[text_input, grade_input],
        outputs=output
    )

MODEL = create_model()

# Compiles the model:
MODEL.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)