import os
from appointment.models.predictor_router import predict_disease
from appointment.severity_engine import calculate_severity

from appointment.appointment_report import generate_appointment_report
from voice_of_the_patient import transcribe_with_groq

from appointment.doctor_router import get_doctor_for_disease
from appointment.scheduler import get_available_slots
import gradio as gr



def process_patient_submission(user_id,problem_type, voice_path, image_path):

    # Voice → text
    if voice_path:
        patient_text = transcribe_with_groq(voice_path)
    else:
        patient_text = "No voice description provided."

    # Default values
    slots = ["No slots available"]
    doctor_id = None
    severity = 0

    # Image → model prediction
    if image_path and problem_type != "General":

        disease, confidence = predict_disease(image_path, problem_type)

        # Doctor routing
        doctor_id, doctor_name, doctor_email = get_doctor_for_disease(problem_type)

        # Severity score
        severity, emergency_flag = calculate_severity(
        age=40,
        symptom_level="Moderate",
        duration="1-3 days",
        model_confidence=confidence,
        existing_conditions=None
    )

        # Load slots
        appointment_date = "2026-03-10"
        slots = get_available_slots(doctor_id, appointment_date)

    else:

        disease = "General Consultation"
        confidence = 0.0

    # Generate PDF report
    pdf_path = generate_appointment_report(
        user_id=user_id,
        disease_type=problem_type,
        prediction=disease,
        confidence=confidence,
        patient_voice_text=patient_text,
        image_path=image_path
    )

    prediction_text = f"""
    ### AI Prediction

    Detected Condition: **{disease}**

    Confidence Score: **{confidence:.2f}**

    Severity Score: **{severity}**
    """

    return prediction_text, "", pdf_path,gr.update(choices=slots, value=None), doctor_id