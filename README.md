# Automated Email Response System

A Python-based web application that allows customers to submit queries through a web interface and automatically sends acknowledgment emails to them.

---

## Features

- **Customer Query Form**: Users can submit their queries via a web form.  
- **Database Storage**: Queries are stored in an SQLite database.  
- **Automated Email Replies**: Sends acknowledgment emails to customers after submitting a query.  
- **Styled Web Interface**: Clean and responsive UI for query submission.  
- **Secure Credentials**: Uses `.env` to store sensitive email credentials safely.  


---

## Technologies Used

- **Python 3**
- **Flask** - Web framework
- **SQLite3** - Database
- **SMTP / smtplib** - Sending emails
- **dotenv** - Loading environment variables
- **HTML/CSS** - Frontend styling

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/dalinaveen/Automated-Email-Response.git
cd Automated-Email-Response


## Create a virtual environment

python -m venv venv
venv\Scripts\activate


##Install dependencies
pip install -r requirements.txt

##Create a .env file in the project root:

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

#Run the Flask app

python app.py
