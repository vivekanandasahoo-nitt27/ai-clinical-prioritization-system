from appointment.scheduler import book_slot
from database import get_user_by_id, get_doctor_by_id
from notifications.email_service import send_appointment_email



def confirm_booking(user_id, doctor_id, slot):

    if not user_id:
        return "Please login before booking appointment."

    if slot == "No slots available":
        return "No slots available. Please try another date."

    success, message = book_slot(
        patient_id=user_id,
        doctor_id=doctor_id,
        severity=50,
        confidence=0.8,
        symptom_level="Moderate",
        duration="2 days",
        date="2026-03-10",
        time_slot=slot
    )

    if success:

        patient = get_user_by_id(user_id)
        doctor = get_doctor_by_id(doctor_id)

        patient_email = patient.email
        doctor_email = doctor.email

        report_path = "storage/appointment_report.pdf"  

        send_appointment_email(
            patient_email,
            doctor_email,
            report_path,
            slot
        )

    return message