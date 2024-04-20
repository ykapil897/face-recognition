from flask import Flask, request, jsonify
import joblib
from all_func import prepare_data, resize_images, convert_to_grayscale, read_labels_from_file
import requests
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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
    
    if isinstance(image, np.ndarray):
        print("ye it is numpy arrya")
    else : 
        print("no it is not numpy array")
    print(image)
    image = resize_images(image)
    print(image)
    print(image.shape)
    image = convert_to_grayscale(image)
    # plt.imshow(image)
    image, image_data = prepare_data(image)
    # plt.imshow(image_data)
    image = pca.transform([image])
    print(image.shape)
    # Make prediction
    prediction = best_model.predict(image) 
    print(type(prediction))
    print(prediction.shape)
    print(prediction)
    prediction = read_labels_from_file("names_labels.txt", prediction[0])
    print(prediction)
    print(jsonify({'prediction': prediction}))
    return jsonify({'prediction': prediction}), 200

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

