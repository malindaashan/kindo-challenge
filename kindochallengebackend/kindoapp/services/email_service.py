import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import FileSystemLoader, Environment

from kindoapp.config import settings

SMTP_USER = settings.SMTP_USER
SMTP_PASS = settings.SMTP_PASS
SMTP_HOST = settings.SMTP_HOST
SMTP_PORT = settings.SMTP_PORT


def send_payment_success_email(transaction_id: int, amount: float, email: str):
    sender = "malinda.ashan@gmail.com"
    recipient = email
    subject = f"Transaction Successful - {transaction_id}"

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('payment_success.html')

    # Render template with data
    html_content = template.render(transaction_id=transaction_id, amount=amount)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    part = MIMEText(html_content, 'html')
    msg.attach(part)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(sender, recipient, msg.as_string())
    print("Email sent")
