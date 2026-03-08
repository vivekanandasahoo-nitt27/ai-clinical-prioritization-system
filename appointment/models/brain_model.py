import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
MODEL_PATH = "appointment/models/brain_tumor_model.h5"

# Load model once
model = load_model(MODEL_PATH, compile=False,safe_mode=False)
if isinstance(model.input, list):
    model = tf.keras.Model(inputs=model.input[0], outputs=model.output)

class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

IMAGE_SIZE = 224


def predict_brain_tumor(img_path):

    # Load image and ensure RGB
    img = image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE), color_mode="rgb")

    # Convert to array
    img_array = image.img_to_array(img)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array, verbose=0)

    predicted_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    predicted_label = class_labels[predicted_index]

    if predicted_label == "notumor":
        disease = "No Brain Tumor"
    else:
        disease = f"Brain Tumor ({predicted_label})"

    return disease, confidence