from flask import Flask, render_template, flash, request, redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import smtplib
import traceback
import time
from datetime import datetime
from pytz import timezone
import pytz
import os


email = "xynicism0@gmail.com"
password = "davgazrgtqjjxljk"
admin = "m.Edwardsonx@gmail.com"
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required(), validators.email()])
    email = TextField('email', validators=[validators.required()])
    message = TextField('message', validators=[validators.required()])


@app.route('/')
def hello():
    return redirect("/contact", code=302)

@app.route("/contact", methods=['GET', 'POST'])
def hello2():
    form = ReusableForm(request.form)


    if request.method == 'POST':
        name=request.form['name']
        sender=request.form['email']
        text=request.form['message']


        if form.validate():
            # Save the comment here.
            try:
                smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login(email, password)
                smtpObj.sendmail(email, admin, "Subject: Contact Form 2 from " + name + ", " + sender + "\n" + text)
                smtpObj.quit()
                flash("Message sent! I'll get back to you soon.")

            except:
                flash("Error: The server is down. Please email me at " + admin + " .")
                print(traceback.format_exc())

            date_format='%m/%d/%Y %H:%M:%S %Z'
            date = datetime.now(tz=pytz.utc)
            date = date.astimezone(timezone('Canada/Pacific'))
            date  = (date.strftime(date_format))
            f = open("logs.txt", "a")
            f.write(date + ": " + sender + ", " + name + ", " + text + "\n")
            f.close()

        else:
            flash('Error: All the form fields are required. ')

    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run()
