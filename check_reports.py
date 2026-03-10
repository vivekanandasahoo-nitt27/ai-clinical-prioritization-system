from database import SessionLocal, Report

session = SessionLocal()

reports = session.query(Report).all()

for r in reports:
    print("ID:", r.id)
    print("USER ID:", r.user_id)
    print("PATH:", r.file_path)
    print("TIME:", r.created_at)
    print("------")

session.close()