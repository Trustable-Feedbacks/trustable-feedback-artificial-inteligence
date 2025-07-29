from flask import Flask, request, jsonify
from evaluate import history
from model import create_model
from preprocess import preprocess

# Initialize and load model weights
model = create_model()
model.load_weights(filepath='./utils/trustable_feedbacks_ai_callback.h5')

# Prediction function
def predict(json_data):
    padded_text_sequence, encoded_grade_lable = preprocess(json_data, isConsult=True)
    predicted = model.predict(x=[padded_text_sequence, encoded_grade_lable])
    predicted = predicted[0].item()  # Convert to Python float
    return {
        'is_fair': True if round(predicted) == 1 else False,
        'chance': round(predicted, 2) * 100,  # Confidence percentage
        'ai_version': 'preview',
        'accuracy': history['accuracy']
    }

# Flask app setup
app = Flask(__name__)

# Endpoint for AI consultation
@app.route('/consulta', methods=['POST'])
def receive_data():
    data = request.get_json()
    resposta = predict([data])
    return jsonify(resposta), 200

# Run server if executed directly
if __name__ == '__consult.py__':
    app.run(debug=True)