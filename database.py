from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    reports = relationship("Report", back_populates="user")


class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    file_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reports")
    

# ---------------------------
# DOCTOR TABLE
# ---------------------------
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)  # Orthopedic, Pulmonologist, Nephrologist, General
    email = Column(String)
    max_slots_per_day = Column(Integer, default=8)
    created_at = Column(DateTime, default=datetime.utcnow)


# ---------------------------
# APPOINTMENT TABLE
# ---------------------------
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    severity_score = Column(Integer)
    model_confidence = Column(String)

    symptom_level = Column(String)   
    duration = Column(String)        

    appointment_date = Column(String)
    time_slot = Column(String)

    payment_status = Column(String, default="Pending")
    status = Column(String, default="Pending")  # Pending / Confirmed / Emergency

    created_at = Column(DateTime, default=datetime.utcnow)
    

def get_latest_report_by_user_id(user_id):

    session = SessionLocal()

    report = (
        session.query(Report)
        .filter(Report.user_id == user_id)
        .order_by(Report.created_at.desc())
        .first()
    )

    session.close()

    if report:
        return report.file_path

    return None
def get_user_by_id(user_id):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

def get_doctor_by_id(doctor_id):
    session = SessionLocal()
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).first()
    session.close()
    return doctor
def init_db():
    Base.metadata.create_all(bind=engine)