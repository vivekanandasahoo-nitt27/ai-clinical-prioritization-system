# check_users.py
from database import SessionLocal, User

session = SessionLocal()

users = session.query(User).all()

for u in users:
    print("ID:", u.id)
    print("EMAIL:", u.email)
    print("------")

session.close()