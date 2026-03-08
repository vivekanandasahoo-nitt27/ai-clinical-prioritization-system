import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

MODEL_PATH = "appointment/models/pneumonia.h5"

# Load model once
model = tf.keras.models.load_model(MODEL_PATH, compile=False,safe_mode=False)
if isinstance(model.input, list):
    model = tf.keras.Model(inputs=model.input[0], outputs=model.output)


def predict_pneumonia(image_path):

    # Load image (force RGB and correct size)
    img = image.load_img(image_path, target_size=(224, 224), color_mode="rgb")

    # Convert image to array
    img_array = image.img_to_array(img)

    # Normalize pixel values
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)[0]

    confidence = float(np.max(prediction))
    label = int(np.argmax(prediction))

    if label == 1:
        disease = "Pneumonia"
    else:
        disease = "Normal Chest"

    return disease, confidence