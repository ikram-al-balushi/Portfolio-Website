from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            # Email Configuration
            # WARNING: You must use an "App Password" if using Gmail. 
            # Regular passwords won't work due to security settings.
            # Go to Google Account > Security > 2-Step Verification > App Passwords
            SENDER_EMAIL = "ikrambaloch112001@gmail.com"
            SENDER_PASSWORD = "" # <--- REPLACE THIS WITH YOUR APP PASSWORD
            RECEIVER_EMAIL = "ikrambaloch112001@gmail.com"

            subject = f"Portfolio Contact from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            email_text = f"Subject: {subject}\n\n{body}"

            # SMTP Server Setup (for Gmail)
            # import smtplib inside function or at top
            import smtplib
            
            # NOTE: This block is commented out until you provide an App Password.
            # Uncomment the lines below and fill in SENDER_PASSWORD to make it work.
            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(SENDER_EMAIL, SENDER_PASSWORD)
                server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_text)
            
            print(f"Backend Log: Email logic ready. Need App Password to actually send.\nData: {name}, {email}, {message}")
            return render_template('index.html', success=True, name=name)
            
        except Exception as e:
            print(f"Error sending email: {e}")
            return render_template('index.html', success=False, error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
