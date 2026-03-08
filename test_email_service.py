import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

emails = [
    "vivekanandasahoo34@gmail.com",
    "vivekanandasahoo54@gmail.com"
]

message = Mail(
    from_email="sahoovivekananda8@gmail.com",
    to_emails=emails,
    subject="AI Healthcare Test",
    html_content="<strong>Email system working successfully</strong>"
)

sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

response = sg.send(message)

print("Status Code:", response.status_code)