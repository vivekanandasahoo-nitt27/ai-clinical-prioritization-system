from tensorflow.keras.models import load_model

model = load_model("appointment/models/brain_model.h5", compile=False, safe_mode=False)

print(type(model.input))