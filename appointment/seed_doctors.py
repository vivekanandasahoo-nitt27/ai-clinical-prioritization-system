from database import SessionLocal, Doctor


def seed_doctors():
    db = SessionLocal()

    existing = db.query(Doctor).count()
    if existing > 0:
        db.close()
        return

    doctors = [
        Doctor(
            name="Dr. Rajesh Kumar",
            specialization="Orthopedic",
            email="vivekkunal3432@gmail.com",
            max_slots_per_day=6
        ),
        Doctor(
            name="Dr. Meera Sharma",
            specialization="Pulmonologist",
            email="vivekanandasahoo34@gmail.com",
            max_slots_per_day=6
        ),
        Doctor(
            name="Dr. Arjun Nair",
            specialization="Nephrologist",
            email="vivekanandasahoo317@gmail.com",
            max_slots_per_day=6
        ),
        Doctor(
            name="Dr. Anita Verma",
            specialization="General",
            email="vivekanandasahoo54@gmail.com",
            max_slots_per_day=8
        ),
        Doctor(
            name="Dr. Nirmal Sahoo",
            specialization="Neurologist",
            email="vivekanandasahoo213@gmail.com",
            max_slots_per_day=8
        )
        
    ]

    db.add_all(doctors)
    db.commit()
    db.close()