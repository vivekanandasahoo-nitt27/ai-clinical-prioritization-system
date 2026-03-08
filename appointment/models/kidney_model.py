import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

MODEL_PATH = "appointment/models/kidney_disease.h5"

# load model once
model = tf.keras.models.load_model(MODEL_PATH, compile=False,safe_mode=False)
if isinstance(model.input, list):
    model = tf.keras.Model(inputs=model.input[0], outputs=model.output)


def predict_kidney(image_path):

    # Load image and force RGB
    img = image.load_img(image_path, target_size=(224, 224), color_mode="rgb")

    # Convert to array
    img_array = image.img_to_array(img)

    # Normalize
    img_array = img_array / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Model prediction
    prediction = model.predict(img_array)[0]

    confidence = float(np.max(prediction))
    label = int(np.argmax(prediction))

    if label == 1:
        disease = "Kidney Disease"
    else:
        disease = "Normal Kidney"

    return disease, confidence