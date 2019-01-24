from flask import Flask, render_template, redirect, session, request, flash
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]+$')

# "^(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
# "^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]+$"

app=Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['Post'])
def register():
    correct_info=True
    if len(request.form['email']) < 1:
        flash("Email can not be blank", "not_correct")
        correct_info=False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "not_correct")
        correct_info=False
    
    if len(request.form['first_name']) < 1:
        flash("First Name can not be blank", "not_correct")
        correct_info=False
    while len(request.form['first_name']) > 1:
        if not request.form['first_name'].isalpha():
            flash("First Name can not contain numbers", "not_correct")
            correct_info=False

    if len(request.form['last_name']) < 1:
        flash("Last Name can not be blank", "not_correct")
        correct_info=False
    while len(request.form['last_name']) > 1:
        if not request.form['last_name'].isalpha():
            flash("Last Name can not contain numbers", "not_correct")
            correct_info=False

    if len(request.form['password']) < 1:
        flash("Password can not be blank", "not_correct")
        correct_info=False
    elif len(request.form['password']) <= 8:
        flash("Password should be more than 8 characters!", "not_correct")
        correct_info=False
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash("Password should have at least 1 uppercase letter and 1 numeric value", "not_correct")
        correct_info=False

    if len(request.form['confirm_password']) < 1:
        flash("Confirm Password can not be blank", "not_correct")
        correct_info=False
    if request.form['password'] != request.form['confirm_password']:
        flash("Password and Confirm Password do not match", "not_correct")  
        correct_info=False

    if len(request.form['birth_date']) < 1:
        flash("Birth Date can not be blank", "not_correct")
        correct_info=False
    else:
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d')
        current_date = datetime.now()
        if birth_date > current_date:
            flash("Birth Date should be in the past", "not_correct")
            correct_info=False

    #can not get the following if statement running
    if correct_info==True:
        flash("Thank you", "correct")
    return redirect("/")
    


if __name__=="__main__":
    app.run(debug=True)
