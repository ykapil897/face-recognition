async function predictImage(formData) {
    const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData,
    });

    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    } else {
        console.log(response);
    }

    const result = await response.json();
    console.log(result);
    return result;
}

document.getElementById('imageForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    const imageFile = document.getElementById('image').files[0];
    const imageUrl = document.getElementById('imageUrl').value;

    if (imageFile) {
        formData.append('image', imageFile);
    } else if (imageUrl) {
        formData.append('imageUrl', imageUrl);
    } else {
        alert('Please upload an image or enter an image URL.');
        return;
    }
    console.log('Uploading');
    try {
        const prediction = await predictImage(formData);
        console.log(prediction);
        document.getElementById('prediction').innerText = `Prediction: ${prediction.prediction}`;
    } catch (error) {
        console.error('Error predicting image:', error);
        alert('Error predicting image. Please try again.');
    }
});

