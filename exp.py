from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import smtplib
import traceback
import time
from datetime import datetime
from pytz import timezone
import pytz

f = open("emailCredentials.txt", "r")
x = str((f.readlines(1)))
email = (x[2:(len(x)-4)])
x = str((f.readlines(2)))
password = (x[2:(len(x)-4)])
x = str((f.readlines(3)))
admin = (x[2:(len(x)-4)])
f.close()



DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


#Find the curent file location/chdir to current location

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('email', validators=[validators.required()])
    message = TextField('message', validators=[validators.required()])


@app.route("/", methods=['GET', 'POST'])
def hello_world():
    form = ReusableForm(request.form)


    if request.method == 'POST':
        name=request.form['name']
        sender=request.form['email']
        text=request.form['message']


        if form.validate():

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

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
