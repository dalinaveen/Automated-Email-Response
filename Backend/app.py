from flask import Flask,render_template,request
import sqlite3
from datetime import datetime
from db_setup import init_db
# from automail_function import send_email_threaded
from auto_mail_function import send_email_reply

app =Flask(__name__,template_folder="Frontend/templates",static_folder="Frontend/static")
init_db()
@app.route("/",methods=['GET',"POST"])
def submit_query():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        query_text=request.form["query"]

        conn = sqlite3.connect("customer_queries.db")
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO queries (customer_name, email, query_description, status, created_at) VALUES (?, ?, ?, ?, ?)",
            (name,email,query_text,"New",datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()

        send_email_reply(name, email, query_text)

        return render_template("thank_you.html", name=name)
      
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True)