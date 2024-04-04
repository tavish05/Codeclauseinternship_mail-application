import smtplib
from email.mime.text import MIMEText

def send_email(sender, recipient, subject, body):
    with smtplib.SMTP(current_user.smtp_host, current_user.smtp_port) as s:
        s.starttls()
        s.login(current_user.smtp_username, current_user.smtp_password)
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        s.send_
