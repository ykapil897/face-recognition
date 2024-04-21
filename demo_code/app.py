from flask import Flask, request, jsonify
import joblib
from all_func import prepare_data, resize_images, convert_to_grayscale, read_labels_from_file
import requests
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import numpy as np
from sklearn.decomposition import PCA

app = Flask(__name__)
CORS(app)

# Load the pre-trained model
best_model = joblib.load('best_svm_model_hog_pca.pkl')
pca = joblib.load('pca_hog.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    image = None

    # Check if image file is uploaded
    if 'image' in request.files:
        image = request.files['image']
        image = Image.open(image)
    elif 'imageUrl' in request.form:
        image_url = request.form['imageUrl']
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    else:
        return jsonify({'error': 'No image provided'}), 400

    image = resize_images(image)

    image = convert_to_grayscale(image)

    image, image_data = prepare_data(image)

    image = pca.transform([image])
    # Make prediction
    prediction = best_model.predict(image) 

    prediction = read_labels_from_file("names_labels.txt", prediction[0])
    print(jsonify({'prediction': prediction}))
    return jsonify({'prediction': prediction}), 200

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)


