import yagmail
import time as t
import sqlite3
import threading

sender_email="yagihin617@etenx.com"
app_password="Your google app password"
yag=yagmail.SMTP(user=sender_email,password=app_password)

def send_email_later(name,email,query_text):
    t.sleep(30)
    subject=f"Re: Your Query Received - {query_text}"
    body=f"""
    hello {name},

    Thank you for contacting us. We received your query:
    "{query_text}"

    Our support team will get back to you shortly.

    Best regards,
    Support Team
    """

    try:
        yag.send(to=email,subject=subject,contents=body)
        print(f"✅ Email sent to {name} ({email})")

        # Optionally update status in DB
        conn = sqlite3.connect("customer_queries.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE queries SET status='Acknowledged' WHERE email=?", (email,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"❌ Failed to send email to {name}: {e}")

def send_email_threaded(name, email, query_text):
    """
    Run the send_email_later function in a separate thread
    """
    threading.Thread(target=send_email_later, args=(name, email, query_text)).start()









#"oltf bobx grfj qctz"