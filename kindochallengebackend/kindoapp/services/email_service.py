import re
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
    """
        Sends a payment success email to the customer.

        This function composes and sends a confirmation email to the given recipient
        email address upon successful completion of a payment transaction. The email
        typically includes details such as the transaction ID and the payment amount.

        Args:
            transaction_id (int): The unique ID of the successful transaction.
            amount (float): The amount that was successfully charged.
            email (str): The recipient's email address.

        Raises:
            ValueError: If the email address is invalid.
            Exception: For any unexpected errors during the email sending process.

        Returns:
            None
        """
    email_regex = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    if not re.match(email_regex, email):
        raise ValueError(f"Invalid email address: {email}")
    sender = "payment@microcodie.co"
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
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(sender, recipient, msg.as_string())
        print("Email sent")
    except Exception as e:
        print(f"send_payment_success_email Unexpected error: {e}")
        raise