from flask import Flask, request, jsonify
import joblib
from all_func import HOGFeatureExtractor, resize_images, convert_to_grayscale
import requests
from PIL import Image
from io import BytesIO
import numpy as np

app = Flask(__name__)

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
    hog_extractor = HOGFeatureExtractor(orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    image = hog_extractor.prepare_data(image)
    image = pca.transform(image)

    # Make prediction
    prediction = best_model.predict(image)  # Replace image_data with preprocessed image data

    return jsonify({'prediction': prediction.tolist()}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
