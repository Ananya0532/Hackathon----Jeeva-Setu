from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO  # Optional: Uncomment if you want real-time features

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donation.db'
db = SQLAlchemy(app)

# Optional SocketIO
# socketio = SocketIO(app)

# ---------------------------------------
# Models
# ---------------------------------------
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    city = db.Column(db.String(50))

class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100))
    city = db.Column(db.String(50))

# ---------------------------------------
# Routes
# ---------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


# ---------- Donors ----------
@app.route('/donors')
def donors_list():
    blood_group = request.args.get('blood_group')
    city = request.args.get('city')

    query = Donor.query
    if blood_group:
        query = query.filter(Donor.blood_group.ilike(f'%{blood_group}%'))
    if city:
        query = query.filter(Donor.city.ilike(f'%{city}%'))

    donors = query.all()
    return render_template('donors.html', donors=donors)


@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor():
    if request.method == 'POST':
        donor = Donor(
            name=request.form['name'],
            blood_group=request.form['blood_group'],
            contact=request.form['contact'],
            email=request.form['email'],
            city=request.form['city']
        )
        db.session.add(donor)
        db.session.commit()
        flash('Donor added successfully!', 'success')
        return redirect(url_for('donors_list'))
    return render_template('add_donor.html')


# ---------- Recipients ----------
@app.route('/recipients')
def recipients_list():
    blood_group = request.args.get('blood_group')
    city = request.args.get('city')

    query = Recipient.query
    if blood_group:
        query = query.filter(Recipient.blood_group.ilike(f'%{blood_group}%'))
    if city:
        query = query.filter(Recipient.city.ilike(f'%{city}%'))

    recipients = query.all()
    return render_template('recipients.html', recipients=recipients)


@app.route('/add_recipient', methods=['GET', 'POST'])
def add_recipient():
    if request.method == 'POST':
        recipient = Recipient(
            name=request.form['name'],
            blood_group=request.form['blood_group'],
            contact=request.form['contact'],
            email=request.form['email'],
            city=request.form['city']
        )
        db.session.add(recipient)
        db.session.commit()
        flash('Recipient added successfully!', 'success')
        return redirect(url_for('recipients_list'))
    return render_template('add_recipient.html')


# ---------------------------------------
# Run App
# ---------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not exist

    # If using SocketIO, uncomment below:
    # socketio.run(app, debug=True, port=5000, allow_unsafe_werkzeug=True)

    # Otherwise, normal Flask run:
    app.run(debug=True, port=5000)