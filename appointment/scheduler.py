from database import SessionLocal, Appointment, Doctor


def get_available_slots(doctor_id, date):
    db = SessionLocal()

    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        db.close()
        return []

    booked = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.appointment_date == date,
        Appointment.status != "Cancelled"
    ).all()

    booked_slots = [a.time_slot for a in booked]

    # Example fixed slots
    all_slots = [
        "09:00-09:30",
        "09:30-10:00",
        "10:00-10:30",
        "10:30-11:00",
        "11:00-11:30",
        "11:30-12:00",
    ]

    available = [slot for slot in all_slots if slot not in booked_slots]

    db.close()
    return available


def book_slot(patient_id, doctor_id, severity, confidence,
              symptom_level, duration,
              date, time_slot):

    db = SessionLocal()

    existing = db.query(Appointment).filter(
        Appointment.doctor_id == doctor_id,
        Appointment.appointment_date == date,
        Appointment.time_slot == time_slot
    ).first()

    if existing:
        db.close()
        return False, "Slot already booked"

    appointment = Appointment(
        patient_id=patient_id,
        doctor_id=doctor_id,
        severity_score=severity,
        model_confidence=str(confidence),
        symptom_level=symptom_level,
        duration=duration,
        appointment_date=date,
        time_slot=time_slot,
        payment_status="Paid",
        status="Confirmed"
    )

    db.add(appointment)
    db.commit()
    db.close()

    return True, "Appointment Confirmed"


