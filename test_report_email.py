import os
from database import SessionLocal, User, Report
from notifications.email_service import send_appointment_email


USER_EMAIL = "vivekanandasahoo18@gmail.com"


def get_latest_report_for_user(email):

    session = SessionLocal()

    # Find user
    user = session.query(User).filter(User.email == email).first()

    if not user:
        session.close()
        print("❌ User not found")
        return None

    print("User ID:", user.id)
    print("User Email:", user.email)

    # Find latest report
    report = (
        session.query(Report)
        .filter(Report.user_id == user.id)
        .order_by(Report.created_at.desc())
        .first()
    )

    session.close()

    if not report:
        print("❌ No reports found for this user")
        return None

    return report.file_path


def test_email():

    report_path = get_latest_report_for_user(USER_EMAIL)

    print("REPORT PATH:", report_path)

    if not report_path:
        return

    report_path = os.path.normpath(report_path)

    # Check file exists
    if not os.path.exists(report_path):
        print("❌ Report file does not exist on disk")
        return

    print("✅ File exists:", report_path)
    print("📄 File size:", os.path.getsize(report_path), "bytes")

    # Send test email
    status = send_appointment_email(
        patient_email=USER_EMAIL,
        doctor_email=USER_EMAIL,
        report_path=report_path,
        slot="TEST SLOT"
    )

    print("📧 EMAIL STATUS:", status)


if __name__ == "__main__":
    test_email()