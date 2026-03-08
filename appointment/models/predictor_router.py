from .kidney_model import predict_kidney
from .pneumonia_model import predict_pneumonia
from .brain_model import predict_brain_tumor
from .fracture_model import predict_fracture


def predict_disease(image_path, disease_type):

    if disease_type == "Kidney":
        return predict_kidney(image_path)

    elif disease_type == "Pneumonia":
        return predict_pneumonia(image_path)

    elif disease_type == "Brain":
        return predict_brain_tumor(image_path)

    elif disease_type == "Fracture":
        return predict_fracture(image_path)

    else:
        return "Unknown", 0.0