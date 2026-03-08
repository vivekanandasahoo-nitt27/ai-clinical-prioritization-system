from database import SessionLocal, Doctor

doctor_map = {
    "Kidney": "Nephrologist",
    "Brain": "Neurologist",
    "Fracture": "Orthopedic",
    "Pneumonia": "Pulmonologist",
    "General": "General"
}


def get_doctor_for_disease(disease_type):

    db = SessionLocal()

    specialization = doctor_map.get(disease_type, "General")

    doctor = db.query(Doctor).filter(
        Doctor.specialization == specialization
    ).first()

    db.close()

    if doctor:
        return doctor.id, doctor.name, doctor.email
    else:
        return None, None, None