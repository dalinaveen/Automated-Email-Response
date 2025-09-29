import os
import smtplib
from email.mime.text import MIMEText



def send_email_reply(name,email,query_text):
    sender_mail=os.environ.get("EMAIL_USER")
    sender_password=os.environ.get("EMAIL_PASS")

    subject ='Your Query Received'
    body = f"""Hello {name},\n\nWe have received your query:\n"{query_text}"\n\nOur team will respond soon."""

    msg =MIMEText(body)
    msg['Subject']=subject

    msg["From"] = sender_mail
    msg["To"] = email

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_mail, sender_password)
        server.sendmail(sender_mail,email, msg.as_string())
        server.quit()
        print(f"✅ Email sent to {email}")
    except Exception as e:
        print(f"❌ Failed to send email to {email}: {e}")