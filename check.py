from database import SessionLocal, Doctor
db = SessionLocal()
print(db.query(Doctor).all())